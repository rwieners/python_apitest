import requests
import json
import os

def main():
    url = "https://api.chucknorris.io/jokes/random"  # Hier die URL deiner API einfügen
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}  # Falls erforderlich, füge hier deine Autorisierungsdaten ein

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Wirft eine Fehlerausnahme, wenn die Anfrage fehlschlägt (z.B. Fehlercode 4xx oder 5xx)
        data = response.json()["value"]   # Nur den "value"-Teil der JSON-Antwort erhalten. data = response.json() für gesamtes json

        if not os.path.isfile("api_response.json"):
            with open("api_response.json", "w") as file:
                json.dump([], file)  # Leeres JSON-Array schreiben, wenn die Datei neu ist

        # JSON-Datei einlesen
        with open("api_response.json", "r+") as file:
            json_data = json.load(file)

            # Neuen Eintrag hinzufügen
            json_data.append(data)

            # Zurück zum Anfang der Datei gehen, um das JSON-Array zu überschreiben
            file.seek(0)
            file.truncate()

            # JSON-Array zurück in die Datei schreiben
            json.dump(json_data, file, indent=4)

        print("API-Antwort wurde zum JSON hinzugefügt.")
    except requests.exceptions.RequestException as e:
        print("Fehler beim Abrufen der API:", e)

if __name__ == "__main__":
    main()
