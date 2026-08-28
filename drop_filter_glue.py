#!/usr/bin/env python
# coding: utf-8

# Elena Gandert, 2023-2025

# Import libraries/modules
import pandas as pd
from os import path
from tkinter import Tk, filedialog, messagebox
import dateparser

# Import mappings for columns of all input files
import col_mappings as cmaps

def read_input(inp: dict, directory: str):
    '''reading input files according to config

    Parameters:
        inp (dict): The input dictionary where the following keys and their values
            must be included: `file`, `sheet`, `skiprows`.
        directory (str): The directory where the file named in the config can be found.

    Returns:
        A DataFrame containing the data from the file and sheet 
            named in the config file for the input parameter `inp`.
    '''
    return pd.read_excel(path.join(directory, inp['file']),
                            sheet_name = inp['sheet'],
                            skiprows = inp['skiprows'],
                            engine = "openpyxl")

def drop_filter_glue():

    # Set input
    input_files_dir = 'input_files'

    # Define function for iterating over the inputs
    def prepare_inputs(x):
        # Create DataFrame from input file
        try:
            print("file: ", x['file'])
            input_df = read_input(x, input_files_dir)
        except Exception as err:
            messagebox.showerror("Fehler beim Lesen der Datei", f"Unexpected error: {err},\n{type(err)}")
            exit(1)

        # Filter input
        curr_filter = x['filter']
        if curr_filter == '':
            filtered_df = input_df
        else:
            filter_map = curr_filter(input_df)
            filtered_df = input_df[filter_map]
        
        # Mapping and keep only final columns    
        cols_mapping = x['mapping']
        mapped_df = pd.DataFrame(columns = cols_mapping.keys())
        for col_name in cols_mapping.keys():
            if cols_mapping[col_name] == '':
                continue
            if cols_mapping[col_name] not in filtered_df.columns:
                continue
            mapped_df[col_name] = filtered_df[cols_mapping[col_name]]

        # Set default values
        cols_default = x['default_values']
        final_df = mapped_df.copy()
        for col_name in cols_default.keys():
            if col_name not in mapped_df.columns:
                continue
            final_df[col_name] = cols_default[col_name]

        # DOIs all to lower case for comparison reasons
        final_df['DOI'] = final_df['DOI'].str.lower()

        return final_df

    # Apply function to inputs
    df_list = [prepare_inputs(x) for x in cmaps.input_list]

    merged_df = pd.concat(df_list)

    # Empty project number fields with dash     # FIXME: should be outsourced
    merged_df.loc[merged_df['Projektnummer/Projekt ID DFG'] == "-", 'Projektnummer/Projekt ID DFG'] = float("nan")

    # Data types
    # TODO: def function date_from_year_or_date
    merged_df['Rechnungsjahr / Lizenzjahr'] = merged_df['Rechnungsjahr / Lizenzjahr'].apply(lambda x: float("nan") if pd.isna(x) else dateparser.parse(f"{int(x)}-01-01") if isinstance(x, (int, float)) and len(str(int(x))) == 4 else dateparser.parse(str(x)))
    merged_df['Publikationsjahr'] = merged_df['Publikationsjahr'].apply(lambda x: float("nan") if pd.isna(x) else dateparser.parse(f"{int(x)}-01-01") if isinstance(x, (int, float)) and len(str(int(x))) == 4 else dateparser.parse(str(x)))

    def eur_brutto(row):
        try:
            eur_brutto = row['Euro netto'] * (1+row['Steuersatz'])
            return round(eur_brutto, 2)
        except Exception:
            print(f"Fehler bei Berechnung Euro brutto von DOI: {row['DOI']}")
            exit(1)

    merged_df['Euro brutto'] = merged_df.apply(eur_brutto, axis=1)
    merged_df['Rechnungsjahr / Lizenzjahr'] = merged_df['Rechnungsjahr / Lizenzjahr'].dt.year
    merged_df['Publikationsjahr'] = merged_df['Publikationsjahr'].dt.year

    # remove articles that were delivered in previous years via DOI match
    previous_years = pd.concat([read_input(year_set, input_files_dir) for year_set in cmaps.previous_years])
    previous_years['DOI'] = previous_years['DOI'].str.lower()
    dedup_df = merged_df[~merged_df['DOI'].isin(previous_years['DOI'])].copy()

    # remove duplicate rows
    dedup_rows_df = dedup_df.drop_duplicates(ignore_index = True)

    output_df = dedup_rows_df.copy()

    # Output file(s)
    output_name = "dfg-prepared"
    output_df.to_excel(f"{output_name}.xlsx", index=False)
    print(f"xlsx erstellt: {output_name}.xlsx")

    messagebox.showinfo("Excel-Datei erstellt", f"""Die Dateien aus 'col_mappings.py' wurden erfolgreich in eine gemeinsame Excel-Datei umgewandelt.

    Dateiname: \"{output_name}.xlsx\""""
    )


if __name__ == "__main__":
    drop_filter_glue()
