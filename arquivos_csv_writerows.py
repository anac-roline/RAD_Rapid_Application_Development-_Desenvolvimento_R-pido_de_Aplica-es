import csv

with open('perfis1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    row_list = [
        ["name", "age", "country"],
        ["Ana Caroline", "25", "Brasília"],
        ["Maria Antonia", "40", "Piauí"],
        ["Meirelane", "23", "Samambaia Norte"]
    ]

    writer.writerows(row_list)