import csv

def export_to_csv(students, filename="results.csv"):
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Marks", "Total", "Average", "Grade"])
        for s in students:
            writer.writerow([
                s['id'], s['name'], s['marks'], s['total'],
                f"{s['average']:.2f}", s['grade']
            ])
