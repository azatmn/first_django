import csv
import os
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        csv_path = os.path.join(settings.BASE_DIR, 'phones.csv')
        
        with open(csv_path, 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for row in phones:
            phone_id = int(row['id'])
            name = row['name'].strip()
            price = float(row['price'].replace(',', '.').strip())
            image = row['image'].strip()
            release_date = datetime.strptime(row['release_date'].strip(), '%Y-%m-%d').date()
            
            lte_raw = row['lte_exists'].strip().lower()
            lte_exists = lte_raw in ('true', '1', 'yes', 'y', 'да')

            Phone.objects.update_or_create(
                id=phone_id,
                defaults={
                    'name': name,
                    'price': price,
                    'image': image,
                    'release_date': release_date,
                    'lte_exists': lte_exists,
                }
            )

        self.stdout.write(self.style.SUCCESS('Импорт завершён'))