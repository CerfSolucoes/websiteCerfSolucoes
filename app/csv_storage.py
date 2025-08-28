import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, '..', 'services.csv')
CSV_FILE = os.path.abspath(CSV_FILE)

FIELDNAMES = ['image','category','type','title','page']

def ensure_csv_exists():
    """Garante que o CSV exista com cabeçalho."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def read_services():
    """Lê posts do CSV e retorna uma lista de dicionários."""
    ensure_csv_exists()
    services = []
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            services.append({'image': row['image'], 'category': row['category'],'type': row['type'],'title': row['title'],'page': row['page']})
    return services

def append_services(new_service):
    """Acrescenta um post ao CSV sem sobrescrever o arquivo."""
    ensure_csv_exists()
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(new_service)
