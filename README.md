# grade_prediction
# grade_prediction
Begrüßung & Einführung

Hallo zusammen,
heute stelle ich euch mein Machine Learning Projekt vor, mit dem wir die Endnote von Schülern basierend auf verschiedenen Merkmalen vorhersagen können. Dabei kombiniere ich eine Webanwendung mit einer Datenbank und einem trainierten Machine Learning Modell.

1. Überblick über das Projekt

Das Projekt besteht aus folgenden Hauptkomponenten:

    Frontend: Ein benutzerfreundliches Webformular, das Schülerdaten abfragt

    Backend: Flask-Webserver, der die Daten entgegennimmt, vorverarbeitet und eine Vorhersage mit dem Machine Learning Modell durchführt

    Datenbank: MariaDB speichert die Trainingsdaten für das Modell

    Docker: Zur einfachen Bereitstellung der Datenbank und später auch des Backends

2. Frontend

Das Frontend ist in HTML und Bootstrap, sowie mit Jinja zum Laden der Templates gestaltet, um ein responsives und übersichtliches Formular bereitzustellen. Dort geben Nutzer Attribute wie Alter, Geschlecht, Schulform, sowie unterstützende Faktoren wie Lernzeit oder Alkoholkonsum ein.

Nach dem Absenden sendet das Formular die Daten per POST an das Backend. Falls eine Vorhersage vorliegt, wird diese direkt unter dem Formular angezeigt, inklusive einer Noteninterpretation.

3. Backend

Das Backend basiert auf Flask, einem leichtgewichtigen Python Web-Framework.

    Es empfängt die Formulardaten im /-Endpunkt.

    Die Funktion preprocess_form bereitet die rohen Formulardaten in ein geeignetes DataFrame-Format um.

    Anschließend wird das Machine Learning Modell geladen (ein Random Forest Regressor), das auf historischen Schülerdaten trainiert wurde.

    Das Modell gibt eine Punktzahl für die voraussichtliche Abschlussnote zurück, die gerundet an das Frontend weitergereicht wird.

4. Datenbank

Die MariaDB-Datenbank enthält die Trainingsdaten.

    Daten aus zwei CSV-Datensätzen (student-mat.csv und student-por.csv) wurden zusammengeführt und in die Tabelle students_training importiert.

    Das Backend liest die Trainingsdaten von dort aus, um das Modell zu trainieren oder zu aktualisieren.

    Die Verbindung erfolgt über MariaDB-Connector in Python.

5. Machine Learning Pipeline

    Die Pipeline umfasst eine Vorverarbeitung mit OneHotEncoding für kategorische Merkmale und die Weitergabe an den Random Forest Regressor.

    Die Daten werden in Trainings- und Testsets aufgeteilt, das Modell wird trainiert und mit MSE und R² validiert.

    Abschließend wird das trainierte Modell als model.pkl gespeichert und bei Anfragen geladen.

6. Docker Setup

    Für eine einfache und reproduzierbare Umgebung läuft die MariaDB Datenbank in einem Docker Container, gesteuert über eine docker-compose.yml.

    Die Docker-Konfiguration sorgt dafür, dass die Datenbank immer auf Port 3306 verfügbar ist, mit persistenter Speicherung via Docker Volumes.

    Das Backend könnte ebenfalls containerisiert werden, um die gesamte Anwendung portabel zu machen.

Zusammenfassung

    Wir haben eine vollständige Webanwendung gebaut, die Benutzereingaben entgegennimmt und eine Notenvorhersage durch Machine Learning macht.

    Die Datenbasis wird über eine MariaDB verwaltet, die in Docker läuft – so ist die Datenbank unabhängig vom Host-System leicht startbar.

    Das Backend nutzt Flask für schnelle API-Integration und bindet das trainierte Modell nahtlos ein.

    Das Frontend ist benutzerfreundlich und visualisiert das Ergebnis klar.
