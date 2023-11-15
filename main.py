import csv

if __name__ == '__main__':
    import csv

    # Daten für das CSV-Dokument
    data = [
        ['Name', 'Alter', 'Beruf'],
        ['Alice', 25, 'Ingenieur'],
        ['Bob', 30, 'Lehrer'],
        ['Charlie', 22, 'Student'],
        ['David', 35, 'Arzt']
    ]

    # Name der CSV-Datei
    csv_file_path = 'beispiel.csv'

    # CSV-Datei schreiben
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'Das CSV-Dokument wurde erfolgreich erstellt: {csv_file_path}')

