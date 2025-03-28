import csv
from api.models import Receipt

def import_receipts_from_csv(file_path):
    with open(file_path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Skip the header row
        for row in reader:
            Receipt.objects.create(
                entree=row[0] if row[0] else None,
                plat_principal=row[1],
                garniture=row[2] if row[2] else None,
                produit_laitier_ou_divers=row[3] if row[3] else None,
                dessert=row[4] if row[4] else None,
            )
    print("Importation terminée avec succès.")