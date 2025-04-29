import pandas as pd
import json
from datetime import datetime, timedelta
from random import seed, randrange

df = pd.read_csv("datacatalog.csv", sep=";")
df = df[["ID", "Datenerhebung/Monitoring", "Fachliche Beschreibung", "Zuständige Person", "Quelle"]]

catalog = []

start_date = datetime.strptime("1999-01-01", "%Y-%m-%d")
seed(42)

for index, row in df.iterrows():
    random_day = randrange(720)
    entry = {
        "adms:status": "published",
        "bv:classification": "none",
        "bv:personalData": "none",
        "bv:archivalValue": False,
        "dct:identifier": row["ID"],
        "dct:title": {
            "de": row["Datenerhebung/Monitoring"]
        },
        "dct:description": {
            "de": row["Fachliche Beschreibung"]
        },
        "dct:issued": (start_date + timedelta(days=random_day)).strftime("%Y-%m-%d"),
        "dct:modified": (start_date + timedelta(days=random_day)).strftime("%Y-%m-%d"),
        "dct:accessRights": "PUBLIC",
        "dct:publisher": "BAFU-OFEV-UFAM-FOEN",
        "dcat:contactPoint": {
            "schema:name": row["Zuständige Person"],
            "schema:email": "bafu@admin.ch"
        },
        "dcat:keyword": [row["Quelle"]]
    }

    catalog.append(entry)

    match row["Quelle"]:
        case "Sektion Digitales":
            entry["schema:image"] = "https://media.istockphoto.com/id/2195043685/photo/internet-infrastructure-concept-abstract-technology-background.jpg?s=2048x2048&w=is&k=20&c=wIRr2zla-OK0gYu-_WlbcoV0MsMNqR4sT14hDbe6Tg4="
        case "Abteilung Recht":
            entry["schema:image"] = "https://media.istockphoto.com/id/2019979263/photo/legal-rights-concept-statue-of-lady-justice-holding-scales-of-justice.jpg?s=2048x2048&w=is&k=20&c=mJ9aVsNTbc9VscTBof7YqBnDZx5csDt2N-lQvDVLuwc="
        case "Abteilung Luftreinhaltung und Chemikalien":
            entry["schema:image"] = "https://media.istockphoto.com/id/1863994348/photo/high-angle-view-looking-up-at-the-trunk-of-a-lush-green-forest-that-helps-in-trapping-dust.jpg?s=2048x2048&w=is&k=20&c=6ephNlfI6dH3dvFX3TmS2ExiiU2ez7pMSN8sSd6tjDo="
        case "Abteilung Boden und Biotechnologie":
            entry["schema:image"] = "https://media.istockphoto.com/id/2193098682/photo/green-plant-growing-in-good-soil-agriculture-organic-gardening-planting-or-ecology-concept.jpg?s=2048x2048&w=is&k=20&c=vJKc13e1ZDDydf_6GLsx0ZIXY9m1EwK34kgIQ3wTG-U="
        case "Abteilung Hydrologie":
            entry["schema:image"] = "https://media.istockphoto.com/id/2202886132/photo/guadalhorce-or-guadalteba-reservoirs.jpg?s=2048x2048&w=is&k=20&c=0d9Q5jLF7xTbydHBF72LM54QIuKzK0KHp3xp5RjkAUQ="
        case "Direktionsbereich Klima":
            entry["schema:image"] = "https://media.istockphoto.com/id/1307794342/photo/climate-change-from-drought-to-green-growth.jpg?s=2048x2048&w=is&k=20&c=Y0oJCkW8NoEYDg0Qq2Xv1wrqw_uGU67sh86UiWqtPEQ="
        case "Abteilung Wasser":
            entry["schema:image"] = "https://media.istockphoto.com/id/2207027410/photo/water-flea-underwater.jpg?s=2048x2048&w=is&k=20&c=TEbKASL993pwuvdx3xx-ucu2CYp3PgBdaK7Hi0BkRdQ="
        case "Abteilung Wald":
            entry["schema:image"] = "https://media.istockphoto.com/id/1158192529/photo/beautiful-way-in-a-deciduous-forest-germany.jpg?s=2048x2048&w=is&k=20&c=zlaRLHY9gZJV43j3h_Sk5C7S37w7ilSpkvfCClWysMs="
        case "Abteilung Lärm & NIS":
            entry["schema:image"] = "https://media.istockphoto.com/id/1405441860/photo/abstract-colourful-music-sound-wave-on-black-background.jpg?s=2048x2048&w=is&k=20&c=NafWmmhGHlL_YrN5Zd5lvGyRR1h_PjwCpUFX79PSEBk="

    if row["ID"] == 22:
        with open(f"{row['ID']}.json", 'w') as json_file:
            json.dump(entry, json_file, indent=4)


with open('cata.json', 'w') as json_file:
    json.dump(catalog, json_file, indent=4)