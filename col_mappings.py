# config for the DFG monitoring prep script

from pandas import DataFrame
import pandas as pd

vorlage = {
    'file': '', # file name without path, must be in directory `input_files`
    'sheet': '',
    'skiprows': 0, # give number of rows in xlsx to skip (rows at the beginning of the file that are not part of the data table - the title row IS part of the data table!)
    'filter': '',   # can be left empty; then the input is used without filtering; if filter function is used, give its name without quotes
        # {
        # 'column_name_input' == 'value'
        # 'BELASTETE KST/IA#' enthält die Kostenstelle von der bezahlt wurde
        # Write here ...
        # }
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': '',
        'förderfähig': '',
        'Bemerkung': '', #vrmtl. leer lassen, kein Pflichtfeld
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': '',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': '',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        # Write here ...
    }
}

def pubfonds_2023_filt(df: DataFrame):
    return (df['*Publikationsjahr laut Crossref'].isin(['2023'])) & \
            (df['*DOI'].notna())
# Förderjahr 2023
pubfonds_2023 = {
    'file': 'Antragstabelle_2022-2024.xlsx',
    'sheet': 'Antraege',
    'skiprows': 0,
    'filter': pubfonds_2023_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': '*DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '*Verlag',
        'Publikationsform': '',
        'CC-Lizenz': '*CC-Lizenz',
        'Originalwährung': '*Währung aus Rechnung',
        'Rechnungsbetrag in Originalwährung': '*Rechnungsbetrag',
        'Euro netto': '*Rechnung €',
        'Steuersatz': '',
        'Euro brutto': '', # automatische Berechnung (Excel-Formel)
        'Kostensplitting': '*Kostensplitting extern',
        'Zuschussbetrag DFG': '*Zuschussbetrag DFG',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': 'Rechnungs-Datum',
        'Publikationsjahr': '*Publikationsjahr laut Crossref',
        'Projektnummer/Projekt ID DFG': '*DFG-Projekt-Nr.',
        'DFG-Wissenschaftsbereich': '*Wissenschafts-Bereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Bemerkung': 'Nachmeldung', #Nachmeldung Artikel 2023
        'Publikationsform': 'journal article',
        'Steuersatz': 0.19,
        'Euro brutto': '', # = ['Euro netto'] + (['Euro netto']*['Steuersatz'])
        'Gebührenart': 'gold-oa',
        'Zuordnung zu Transformationsvertrag': 'kein', 
    }
}

def deal_wiley_gold_filt(df: DataFrame):
    return (df['Rechnungsnummer'].isin(['Rechnungsnummer Wiley Q1', 'Rechnungsnummer Wiley Q2', 'Rechnungsnummer Wiley Q3', 'Rechnungsnummer Wiley Q4'])) #Rechnungsnummer Wiley Q1-4 fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_wiley_gold = {
    'file': 'Gesamtliste-Wiley-NEU.xlsx',
    'sheet': 'Wiley-Gesamtliste Neu',
    'skiprows': 0,
    'filter': deal_wiley_gold_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '', 
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': 'Rechnungsbetrag netto',
        'Euro netto': 'Rechnungsbetrag netto',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '', # keine Fälle des Splittings mit Einrichtung außerhalb bekannt
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date',
        'Projektnummer/Projekt ID DFG': 'DFG-Projektnummer',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Wiley',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Steuersatz': 0.07,
        'Euro brutto': '', # = ['Euro netto'] + (['Euro netto']*['Steuersatz'])
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Zuordnung zu Transformationsvertrag': 'Wiley (DEAL) 2024-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
        }
}

def deal_wiley_hybrid_filt(df: DataFrame):
    return (df['Rechnungsnummer'].isin(['Rechnungsnummer PABA hybrid Wiley'])) #Rechnungsnummer PABA hybrid Wiley fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden
   
deal_wiley_hybrid = {
    'file': 'Gesamtliste-Wiley-NEU.xlsx',
    'sheet': 'Wiley-Gesamtliste Neu',
    'skiprows': 0,
    'filter': deal_wiley_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date', #Angabe in Ursprungstabelle TTMMJJJJ
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Wiley',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.07,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Wiley (DEAL) 2024-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
    }
}

def deal_wiley_optout_filt(df: DataFrame):
    return (df['an MPDL als berechtigt verifiziert'].isin(['ja'])) & \
            (df['In Gesamtliste enthalten'].isin(['nein'])) & \
            (df['Rechnungsnummer'].isin(['Rechnungsnummer PABA hybrid Wiley'])) #Rechnungsnummer PABA hybrid Wiley fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_wiley_optout = {
    'file': 'Gesamtliste-Wiley-NEU.xlsx',
    'sheet': 'Opt Out',
    'skiprows': 0,
    'filter': deal_wiley_optout_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': '',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'nein',
        'Bemerkung': 'DEAL Opt-Out',
        'Name des Verlags, der Plattform, des Server, …': 'Wiley',
        'Publikationsform': 'journal article',
        'CC-Lizenz': 'keine',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.07,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'publication charge',
        'Zuordnung zu Transformationsvertrag': 'Wiley (DEAL) 2024-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
    }
}

def deal_springer_gold_filt(df: DataFrame):
    return (df['Rechnungsnummer'].isin(['Rechnungsnummer Springer Q1', 'Rechnungsnummer Springer Q2', 'Rechnungsnummer Springer Q3', 'Rechnungsnummer Springer Q4'])) & \
            (df['Leistungszeitraum'].isin(['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'])) #Rechnungsnummer Springer Q1-4 fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_springer_gold = {
    'file': 'Gesamtliste-SN-Dashboard+OptOuts.xlsx',
    'sheet': 'Gesamtliste_neu_ab18.3.25',
    'skiprows': 0,
    'filter': deal_springer_gold_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '', 
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '', 
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': 'Rechnungsbetrag netto',
        'Euro netto': 'Rechnungsbetrag netto',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '', # keine Fälle des Splittings mit Einrichtung außerhalb bekannt 
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date',
        'Projektnummer/Projekt ID DFG': 'DFG-Projektnummer',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Springer Nature',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Steuersatz': 0.07,
        'Euro brutto': '', # = ['Euro netto'] + (['Euro netto']*['Steuersatz'])
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'gold-oa',
        'Zuordnung zu Transformationsvertrag': 'Springer (DEAL) 2024-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',      
    }
}

def deal_springer_hybrid_filt(df: DataFrame):
         return (df['Rechnungsnummer'].isin(['Rechnungsnummer PABA hybrid Springer'])) & \
                (df['Artikeltyp'].isin(['OriginalPaper', 'ReviewPaper', 'BriefCommunication'])) #Rechnungsnummer PABA hybrid Springer fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_springer_hybrid = {
    'file': 'Gesamtliste-SN-Dashboard+OptOuts.xlsx',
    'sheet': 'Gesamtliste_neu_ab18.3.25',
    'skiprows': 0,
    'filter': deal_springer_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date', #Angabe in Ursprungstabelle TTMMJJJJ
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Springer Nature',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.07,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Springer (DEAL) 2024-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
    }
}
def deal_springer_hybrid_nonresearch_filt(df: DataFrame):
         return (df['Rechnungsnummer'].isin(['Non Research Article 2024'])) & \
                (df['Artikeltyp'].isin(['EditorialNotes', 'Letter', 'Report', 'BookReview'])) 

deal_springer_hybrid_nonresearch = {
    'file': 'Gesamtliste-SN-Dashboard+OptOuts.xlsx',
    'sheet': 'Gesamtliste_neu_ab18.3.25',
    'skiprows': 0,
    'filter': deal_springer_hybrid_nonresearch_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date', #Angabe in Ursprungstabelle TTMMJJJJ
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'nein',
        'Bemerkung': 'Non-Research-Artikel',
        'Name des Verlags, der Plattform, des Server, …': 'Springer Nature',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.07,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Springer (DEAL) 2024-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
    }
}

def deal_springer_optout_filt(df: DataFrame):
    return (df['Online Publication Date'].dt.year == 2024) & \
            (df['Rechnungsnummer'].isin(['Rechnungsnummer PABA hybrid Springer'])) & \
            (df['Rechnungsnummer'].isin(['Non Research Article 2024'])) &\
            (df['in Gesamtliste enthalten'].isin(['nein']))
 #Rechnungsnummer PABA hybrid Springer fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_springer_optout = {
    'file': 'Gesamtliste-SN-Dashboard+OptOuts.xlsx',
    'sheet': 'Opt Outs',
    'skiprows': 0,
    'filter': deal_springer_optout_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': '',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'nein',
        'Bemerkung': 'DEAL Opt-Out',
        'Name des Verlags, der Plattform, des Server, …': 'Springer Nature',
        'Publikationsform': 'journal article',
        'CC-Lizenz': 'keine',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.07,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'publication charge',
        'Zuordnung zu Transformationsvertrag': 'Springer (DEAL) 2024-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
    }
}

def deal_elsevier_gold_filt(df: DataFrame):
    return (df['Rechnungsnummer'].isin(['Rechnungsnummer Elsevier Q1', 'Rechnungsnummer Elsevier Q2', 'Rechnungsnummer Elsevier Q3', 'Rechnungsnummer Elsevier Q4'])) & \
            (df['Leistungszeitraum'].isin(['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'])) #Rechnungsnummer Elsevier Q1-4 fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_elsevier_gold = {
    'file': 'Gesamtliste-Elsevier-Dashboard.xlsx',
    'sheet': 'Gesamt-approved',
    'skiprows': 0,
    'filter': deal_elsevier_gold_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '', 
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '', 
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': 'Rechnungsbetrag netto',
        'Euro netto': 'Rechnungsbetrag netto',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '', # keine Fälle des Splittings mit Einrichtung außerhalb bekannt 
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date',
        'Projektnummer/Projekt ID DFG': 'DFG-Projektnummer',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Elsevier',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Steuersatz': 0.07,
        'Euro brutto': '', # = ['Rechnungsbetrag netto'] + (['Rechnungsbetrag netto']*['MwSt.-Satz'])
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'gold-oa',
        'Zuordnung zu Transformationsvertrag': 'Elsevier (DEAL) 2023-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',      
    }
}

def deal_elsevier_hybrid_filt(df: DataFrame):
         return (df['Rechnungsnummer'].isin(['Rechnungsnummer PABA hybrid Elsevier'])) #Rechnungsnummer PABA hybrid Elsevier fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_elsevier_hybrid = {
    'file': 'Gesamtliste-Elsevier-Dashboard.xlsx',
    'sheet': 'Gesamt-approved',
    'skiprows': 0,
    'filter': deal_elsevier_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date', #Angabe in Ursprungstabelle TTMMJJJJ
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Elsevier',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.07,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Elsevier (DEAL) 2023-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
    }
}

def deal_elsevier_cptl_filt(df: DataFrame):
         return (df['Rechnungsnummer'].isin(['Rechnungsnummer Elsevier CPTL Q2', 'Rechnungsnummer Elsevier CPTL Q3', 'Rechnungsnummer Elsevier CPTL Q4'])) #Rechnungsnummer Elsevier CPTL Q2-4 fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_elsevier_cptl = {
    'file': 'Gesamtliste-Elsevier-Dashboard.xlsx',
    'sheet': 'Gesamt-approved',
    'skiprows': 0,
    'filter': deal_elsevier_cptl_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': 'Rechnungsbetrag netto',
        'Euro netto': 'Rechnungsbetrag netto',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date', #Angabe in Ursprungstabelle TTMMJJJJ
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': 'DFG-Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Elsevier',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Steuersatz': 0.07,
        'Euro brutto': 0.00, # = ['Rechnungsbetrag netto'] + (['Rechnungsbetrag netto']*['MwSt.-Satz'])
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Elsevier (DEAL) 2023-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
    }
}

def deal_elsevier_optout_filt(df: DataFrame):
    return (df['an MPDL als berechtigt verifiziert'].isin(['ja'])) & \
            (df['in Gesamtliste enthalten'].isin(['–'])) & \
            (df['Rechnungsnummer'].isin(['Rechnungsnummer PABA hybrid Elsevier'])) #Rechnungsnummer PABA hybrid Elsevier fungiert als Platzhalter, korrekte Rechnungsnummer muss angegeben werden

deal_elsevier_optout = {
    'file': 'Gesamtliste-Elsevier-Dashboard.xlsx',
    'sheet': 'Opt_Out_Artikel',
    'skiprows': 0,
    'filter': deal_elsevier_optout_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': '',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online Publication Date',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'nein',
        'Bemerkung': 'DEAL Opt-Out',
        'Name des Verlags, der Plattform, des Server, …': 'Elsevier',
        'Publikationsform': 'journal article',
        'CC-Lizenz': 'keine',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.07,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'publication charge',
        'Zuordnung zu Transformationsvertrag': 'Elsevier (DEAL) 2023-2028',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}

def acs_hybrid_filt(df: DataFrame): #neu!
    return (df ['Publisher Name'].isin(['American Chemical Society']))
   
acs_hybrid = {
    'file': 'ACS_Jahresreport2024_Charité.xlsx',
    'sheet': 'Tabelle1',
    'skiprows': 0,
    'filter': acs_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'Manuscript DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'Product 1 Option 2 Value',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Publication Date',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'ACS',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'ACS (FAK) 2024-2026',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}
def bmj_hybrid_filt(df: DataFrame):
    return (df['Publisher Name'].isin(['BMJ']))
bmj_hybrid = {
    'file': '2024-BMJ-Report.xlsx',
    'sheet': 'Institution Transaction Summary',
    'skiprows': 0,
    'filter': bmj_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'Manuscript DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'Creative Commons License Type',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Publication Date',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'BMJ',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'BMJP (BSB) 2023-2024',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}


def cup_hybrid_filt(df: DataFrame):
    return (df['Institution Identifier - from manuscript metadata'].isin(['ror.org/001w7jn25'])) & \
            (df['OA-Type'].isin(['hybrid-oa']))
    # Filter gesetzt nach ROR-ID und Unterscheidung Hybrid/Gold OA muss vorgenommen werden

cup_hybrid = {
    'file': 'CUP_2024.xlsx',
    'sheet': 'Institution Transaction Summary',
    'skiprows': 0,
    'filter': cup_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'Manuscript DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'Creative Commons License Type',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Publication Date',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'CUP',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'CUP (BSB) 2022-2024',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}

def cup_gold_filt(df: DataFrame):
    return (df['Institution Identifier - from manuscript metadata'].isin(['ror.org/001w7jn25'])) & \
            (df['OA-Type'].isin(['gold-oa']))
    # Filter gesetzt nach ROR-ID und Unterscheidung Hybrid/Gold OA muss vorgenommen werden

cup_gold = {
    'file': 'CUP_2024.xlsx',
    'sheet': 'Institution Transaction Summary',
    'skiprows': 0,
    'filter': cup_gold_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'Manuscript DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'Creative Commons License Type',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Publication Date',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'CUP',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'gold-oa',
        'Zuordnung zu Transformationsvertrag': 'CUP (BSB) 2022-2024',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}

def hogrefe_hybrid_filt(df: DataFrame):
    return (df['Affiliation'].isin(['Humboldt-Universität zu Berlin', 'Charité – Universitätsmedizin Berlin'])) & \
            (df['OA-Type'].isin(['Hybrid']))
        #unklare Angabe der Affiliation im Report, mal HU und mal Charité
    
hogrefe_hybrid = {
    'file': 'Report24-rot-markierte-Charite.xlsx',
    'sheet': '2024',
    'skiprows': 6,
    'filter': hogrefe_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'CC-Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Online veröffentlicht', #Datum liegt vor im Format JJJJ-MM-TT
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Hogrefe',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Hogrefe (SUB Göttingen) 2024-2026',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}
def portland_press_hybrid_filt(df: DataFrame): #keine Artikel in 2024 - Mapping nicht überarbeitet.
    return (df['Publisher Name'].isin(['Portland Press']))
portland_press_hybrid = {
    'file': '2023-BMJ-Portland-Report.xlsx',
    'sheet': 'Institution Transaction Summary',
    'skiprows': 0,
    'filter': portland_press_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'Manuscript DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'Creative Commons License Type',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Publication year',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Portland Press',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Portland Press (TIB) 2022-2024',
        'Rechnungsjahr / Lizenzjahr': '2023',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}

def sage_hybrid_filt(df: DataFrame):
    return (df['CA Institution Ringgold Name'].isin(['Charite Universitatsmedizin Berlin', 'Charite Universitatsmedizin Berlin Campus Benjamin Franklin'])) & \
            (df['Journal Type'].isin(['Hybrid'])) &\
            (df['Author open access decision'].isin(['Yes']))
sage_hybrid = {
    'file': 'Sage_Publication_Report_2024_Berlin_HU_+_Charité-korrigiert.xlsx',
    'sheet': 'German Academic Institutions',
    'skiprows': 0,
    'filter': sage_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'License Choice (inc Version)',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'OA Published Date',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
   'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'SAGE',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Sage (BSB) 2024-2025',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}

def iop_hybrid_filt(df: DataFrame):
    return (df['Institution Name'].isin(['Charite University Hospital']))
    
iop_hybrid = {
    'file': 'Germany_TIB_Q4_2024.xlsx',
    'sheet': 'Germany TIB Q4 2024',
    'skiprows': 8,
    'filter': iop_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'Default OA Licence',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Published Date', #Datum liegt vor im Format TT.MM.JJJJ
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'IOP',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'IOP (TIB) 2022-2024',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}

def pubfonds_2024_filt(df: DataFrame):
    return (df['*Publikationsjahr laut Crossref'].isin(['2024'])) & \
            (df['*DOI'].notna())
# Publikationsjahr 2024
pubfonds_2024 = {
    'file': 'Antragstabelle_2022-2024.xlsx',
    'sheet': 'Antraege',
    'skiprows': 0,
    'filter': pubfonds_2024_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': '*DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '*Verlag',
        'Publikationsform': '',
        'CC-Lizenz': '*CC-Lizenz',
        'Originalwährung': '*Währung aus Rechnung',
        'Rechnungsbetrag in Originalwährung': '*Rechnungsbetrag',
        'Euro netto': '*Rechnung €',
        'Steuersatz': '',
        'Euro brutto': '', # automatische Berechnung (Excel-Formel)
        'Kostensplitting': '*Kostensplitting extern',
        'Zuschussbetrag DFG': '*Zuschussbetrag DFG',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': 'Rechnungs-Datum',
        'Publikationsjahr': '*Publikationsjahr laut Crossref',
        'Projektnummer/Projekt ID DFG': '*DFG-Projekt-Nr.',
        'DFG-Wissenschaftsbereich': '*Wissenschafts-Bereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Publikationsform': 'journal article',
        'Steuersatz': 0.19,
        'Euro brutto': '', # = ['Euro netto'] + (['Euro netto']*['Steuersatz'])
        'Gebührenart': 'gold-oa',
        'Zuordnung zu Transformationsvertrag': 'kein', 
    }
}

def pubfonds_2024_PM_filt(df: DataFrame):
    return (df['online publication date'].isin(['2024', 2024])) & \
            (df['DOI'].notna()) & \
            (df['Beleg-\nnummer'].notna()) & \
            (~df['Rechnungsbetr.\nOrig.Währung netto (APC)'].isin([0]))
# Publikationsjahr 2024 - APCs, weitere Gebührenarten in extra Mappings zur besseren Differenzierung
pubfonds_2024_PM = {
    'file': 'Publikationsmanagement_ab2025.xlsx',
    'sheet': 'Tabelle ab 2025',
    'skiprows': 0,
    'filter': pubfonds_2024_PM_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': 'Verlag',
        'Publikationsform': '',
        'CC-Lizenz': 'Lizenz', 
        'Originalwährung': 'Währung',
        'Rechnungsbetrag in Originalwährung': 'Rechnungsbetr.\nOrig.Währung netto (APC)',
        'Euro netto': 'APC € netto',
        'Steuersatz': '',
        'Euro brutto': '', # automatische Berechnung (Excel-Formel)
        'Kostensplitting': 'Kostensplitt-\nextern',
        'Zuschussbetrag DFG': 'Zuschussbetrag DFG',
        'Gebührenart': 'OA-Status',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': 'Transformations-\nvertrag',
        'Rechnungsjahr / Lizenzjahr': 'Rechnungs-\ndatum',
        'Publikationsjahr': 'online publication date',
        'Projektnummer/Projekt ID DFG': 'DFG-Projektnummer',
        'DFG-Wissenschaftsbereich': 'Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Publikationsform': 'journal article',
        'Steuersatz': 0.19,
        'Euro brutto': '', # = ['Euro netto'] + (['Euro netto']*['Steuersatz'])
    }
}

def pubfonds_2024_PM_weit_Gebuehrenarten_1_filt(df: DataFrame):
    return (df['online publication date'].isin(['2024', 2024])) & \
            (df['DOI'].notna()) & \
            (df['Beleg-\nnummer'].notna()) & \
            (df['Gebühren-\nart #1']).isin([
                'colour charge',
                'cover charge',
                'handling fee',
                'other',
                'other - oa conversation fee',
                'other - promotional fee',
                'other - publication fee',
                'other - repository licensing fee',
                'page charge',
                'payment fee',
                'publication charge',
                'reprint',
                'submission fee'])
# Publikationsjahr 2024 - APCs, weitere Gebührenarten in extra Mappings zur besseren Differenzierung
pubfonds_2024_PM_Gebuehrenart_1 = {
    'file': 'Publikationsmanagement_ab2025.xlsx',
    'sheet': 'Tabelle ab 2025',
    'skiprows': 0,
    'filter': pubfonds_2024_PM_weit_Gebuehrenarten_1_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': 'Verlag',
        'Publikationsform': '',
        'CC-Lizenz': 'Lizenz', 
        'Originalwährung': 'Währung',
        'Rechnungsbetrag in Originalwährung': 'Rechn.betr.\nOrig.Währ. netto (Geb.art #1)',
        'Euro netto': 'Rechn.betr.\n€ netto (Geb.art #1)',
        'Steuersatz': '',
        'Euro brutto': '', # automatische Berechnung (Excel-Formel)
        'Kostensplitting': 'Kostensplitt-\nextern',
        'Zuschussbetrag DFG': 'Zuschussbetrag DFG',
        'Gebührenart': 'Gebühren-\nart #1',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': 'Rechnungs-\ndatum',
        'Publikationsjahr': 'online publication date',
        'Projektnummer/Projekt ID DFG': 'DFG-Projektnummer',
        'DFG-Wissenschaftsbereich': 'Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'nein',
        'Publikationsform': 'journal article',
        'Steuersatz': 0.19,
        'Euro brutto': '', # = ['Euro netto'] + (['Euro netto']*['Steuersatz'])
        'Zuordnung zu Transformationsvertrag': 'kein', 
    }
}

def pubfonds_2024_PM_weit_Gebuehrenarten_2_filt(df: DataFrame):
    return (df['online publication date'].isin(['2024', 2024])) & \
            (df['DOI'].notna()) & \
            (df['Beleg-\nnummer'].notna()) & \
            (df['Gebühren-\nart #2']).isin([
                'colour charge',
                'cover charge',
                'handling fee',
                'other',
                'other - oa conversation fee',
                'other - promotional fee',
                'other - publication fee',
                'other - repository licensing fee',
                'page charge',
                'payment fee',
                'publication charge',
                'reprint',
                'submission fee'])
# Publikationsjahr 2024 - APCs, weitere Gebührenarten in extra Mappings zur besseren Differenzierung
pubfonds_2024_PM_Gebuehrenart_2 = {
    'file': 'Publikationsmanagement_ab2025.xlsx',
    'sheet': 'Tabelle ab 2025',
    'skiprows': 0,
    'filter': pubfonds_2024_PM_weit_Gebuehrenarten_2_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': 'Verlag',
        'Publikationsform': '',
        'CC-Lizenz': 'Lizenz', 
        'Originalwährung': 'Währung',
        'Rechnungsbetrag in Originalwährung': 'Rechn.betr.\nOrig.Währ. netto (Geb.art #2)',
        'Euro netto': 'Rechn.betr.\n€ netto (Geb.art #2)',
        'Steuersatz': '',
        'Euro brutto': '', # automatische Berechnung (Excel-Formel)
        'Kostensplitting': 'Kostensplitt-\nextern',
        'Zuschussbetrag DFG': 'Zuschussbetrag DFG',
        'Gebührenart': 'Gebühren-\nart #2',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': 'Rechnungs-\ndatum',
        'Publikationsjahr': 'online publication date',
        'Projektnummer/Projekt ID DFG': 'DFG-Projektnummer',
        'DFG-Wissenschaftsbereich': 'Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'nein',
        'Publikationsform': 'journal article',
        'Steuersatz': 0.19,
        'Euro brutto': '', # = ['Euro netto'] + (['Euro netto']*['Steuersatz'])
        'Zuordnung zu Transformationsvertrag': 'kein', 
    }
}

def taylorandfrancis_gold_filt(df: DataFrame):
    df['Publication Date (Online)'] = pd.to_datetime(
        df[df['Publication Date (Online)'] != '-']['Publication Date (Online)'])
    # print(df.info())
    return (df['Publication Date (Online)'] >= '2024-1-1') & \
            (df['Publication Date (Online)'] <= '2024-12-31') & \
            (df['Publishing Modell'].isin(['Gold']))

taylorandfrancis_gold = {
    'file': 'Taylor&Francis_Gesamtliste.xlsx',
    'sheet': 'zuletzte akt. Juli 25',
    'skiprows': 0,
    'filter': taylorandfrancis_gold_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'Lizenz',
        'Originalwährung': 'Währung',
        'Rechnungsbetrag in Originalwährung': 'Rechnungsbetrag (netto)',
        'Euro netto': 'Rechnungsbetrag (netto)',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': 'Rechnungsdatum',
        'Publikationsjahr': 'Publication Date (Online)',
        'Projektnummer/Projekt ID DFG': 'DFG-Projektnr.',
        'DFG-Wissenschaftsbereich': 'Wissenschaftsbereich',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Taylor & Francis',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Steuersatz': 0.19,
        'Euro brutto': '', # = ['Euro netto'] + (['Euro netto']*['Steuersatz'])
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'gold-oa',
        'Zuordnung zu Transformationsvertrag': 'Taylor & Francis (ZBW) 2024-2026',
    }
}

def taylorandfrancis_hybrid_filt(df: DataFrame):
    df['Publication Date (Online)'] = pd.to_datetime(
        df[df['Publication Date (Online)'] != '-']['Publication Date (Online)'])
    return (df['Publication Date (Online)'] >= '2024-1-1') & \
            (df['Publication Date (Online)'] <= '2024-12-31') & \
            (df['Publishing Modell'].isin(['Hybrid']))

taylorandfrancis_hybrid = {
    'file': 'Taylor&Francis_Gesamtliste.xlsx',
    'sheet': 'zuletzte akt. Juli 25',
    'skiprows': 0,
    'filter': taylorandfrancis_hybrid_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '',
        'Name des Verlags, der Plattform, des Server, …': '',
        'Publikationsform': '',
        'CC-Lizenz': 'Lizenz',
        'Originalwährung': '',
        'Rechnungsbetrag in Originalwährung': '',
        'Euro netto': '',
        'Steuersatz': '',
        'Euro brutto': '',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': '',
        'Publikationsjahr': 'Publication Date (Online)',
        'Projektnummer/Projekt ID DFG': 'DFG-Projektnr.',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        'förderfähig': 'ja',
        'Name des Verlags, der Plattform, des Server, …': 'Taylor & Francis',
        'Publikationsform': 'journal article',
        'Originalwährung': 'EUR',
        'Rechnungsbetrag in Originalwährung': 0.00,
        'Euro netto': 0.00,
        'Steuersatz': 0.19,
        'Euro brutto': 0.00,
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0.00,
        'Gebührenart': 'hybrid-oa',
        'Zuordnung zu Transformationsvertrag': 'Taylor & Francis (ZBW) 2024-2026',
        'Rechnungsjahr / Lizenzjahr': '2024',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften', 
    }
}

def infobudget_2024_filt(df: DataFrame):
    return (df['Pubjahr Crossref'].isin(['2022', '2023', '2024']))
infobudget_2024 = {
    'file': 'KOSTENTABELLE_2024_AS_neu_Gt.xlsx',
    'sheet': 'Tabelle1',
    'skiprows': 0,
    'filter': infobudget_2024_filt,
    'mapping': {
        # 'column_name_output': 'column_name_input'
        'DOI': 'DOI',
        'förderfähig': '',
        'Bemerkung': '', #vrmtl. leer lassen, kein Pflichtfeld
        'Name des Verlags, der Plattform, des Server, …': 'Verlag WoS',
        'Publikationsform': '',
        'CC-Lizenz': 'Lizenz nach Abgleich',
        'Originalwährung': 'Original-\nwährung',
        'Rechnungsbetrag in Originalwährung': 'Rechnungsbetrag\nOriginalwährung netto',
        'Euro netto': 'Rechnungsbetrag Euro netto',
        'Steuersatz': 'Steuersatz',
        'Euro brutto': 'Von der Charité gezahlter Betrag € brutto',
        'Kostensplitting': '',
        'Zuschussbetrag DFG': '',
        'Gebührenart': '',
        'Zuordnung zu Mitgliedschaft': '',
        'Zuordnung zu Transformationsvertrag': '',
        'Rechnungsjahr / Lizenzjahr': 'Rechnungsdatum', #Angabe in Ausgangstabelle in TT-MM-JJJJ
        'Publikationsjahr': 'Pubjahr Crossref',
        'Projektnummer/Projekt ID DFG': '',
        'DFG-Wissenschaftsbereich': '',
    },
    'default_values': {
        # 'column_name_output' = value
        # Write here ...
        'förderfähig': 'ja',
        'Publikationsform': 'journal article',
        'Kostensplitting': '-',
        'Zuschussbetrag DFG': 0,
        'Gebührenart': 'gold-oa',
        'Zuordnung zu Transformationsvertrag': 'kein',
        'DFG-Wissenschaftsbereich': 'Lebenswissenschaften',
    }
}

input_list = [
    #pubfonds_2023, # ggf. Nachmeldungen aus 2023
    pubfonds_2024,
    deal_wiley_gold,
    deal_wiley_hybrid,
    deal_wiley_optout,
    deal_springer_gold,
    deal_springer_hybrid,
    deal_springer_hybrid_nonresearch,
    deal_springer_optout,
    deal_elsevier_gold,
    deal_elsevier_hybrid,
    deal_elsevier_cptl,
    deal_elsevier_optout,
    acs_hybrid,
    bmj_hybrid,
    cup_hybrid,
    cup_gold,
    hogrefe_hybrid,
    # portland_press_hybrid, #für Meldung 24 nicht gebraucht, hier aber beibehalten falls nötig für Meldung 25er Artikel
    sage_hybrid,
    iop_hybrid,
    pubfonds_2024_PM,
    pubfonds_2024_PM_Gebuehrenart_1,
    pubfonds_2024_PM_Gebuehrenart_2,
    taylorandfrancis_gold,
    taylorandfrancis_hybrid,
    infobudget_2024,
]

prev_2022 = {
    'file': 'DFG_Foerderprogramm_Meldung_fuer_2022_Charite_Korrigiert.xlsx',
    'sheet': 'mit DOI',
    'skiprows': range(1, 4),
}

prev_2023 = {
    'file': '2023_Charité_-_Universitätsmedizin_Berlin_001w7jn25_korrigiert_final-Rückversand-aus-Jülich.xlsx',
    'sheet': 'mit DOI',
    'skiprows': range(1, 4),
}

previous_years = [
    prev_2022,
    prev_2023,
]


# FIXME: not used at the moment; hard coded in main
output_data_types = {
    #'Steuersatz': 'float64',
    'Förderjahr': 'datetime64',
    'Rechnungsjahr': 'datetime64',
    }
