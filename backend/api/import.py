import csv
from .models import Receipt

def import_receipt(file):
    with open(file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            print(row)
            Receipt.objects.create(
                entree = row['Entrée'],
                plat_principal = row['Plat principal'],
                garniture = row['Garniture'],
                produit_laitier_ou_divers = row['Produit laitier ou divers'],
                dessert = row['Dessert']
            )
def run(): 
    csv_file_path = "C:\\Users\\vsi.client\\Desktop\\recettes\\backend\\api\\menus.csv"
    import_receipt(csv_file_path)