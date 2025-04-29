import pandas as pd
import json

df = pd.read_csv("datacatalog.csv", sep=";")
df = df[["ID", "Datenerhebung/Monitoring", "Fachliche Beschreibung", "Zuständige Person"]]

catalog = []

for index, row in df.iterrows():
    entry = {"dct:modified": None, "adms:status": "published", "bv:classification": "none", "bv:personalData": "none",
             "bv:archivalValue": False, "dct:identifier": row["ID"], "dct:title": {
            "de": row["Datenerhebung/Monitoring"]
        }, "dct:description": {
            "de": row["Fachliche Beschreibung"]
        }, "dct:issued": "XXXX-YY-DD", "dct:accessRights": "PUBLIC", "dct:publisher": "BAFU-OFEV-UFAM-FOEN",
             "dcta:contactPoint": {
                 "schema:name": row["Zuständige Person"],
                 "schema:email": "bafu@admin.ch"
             }}

    catalog.append(entry)

    if row["ID"] == 22:
        with open(f"{row['ID']}.json", 'w') as json_file:
            json.dump(entry, json_file, indent=4)


with open('cata.json', 'w') as json_file:
    json.dump(catalog, json_file, indent=4)