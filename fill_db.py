import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studio_site.settings")
django.setup()

from studio.models import Studio, Rent
from datetime import datetime

studio1 = Studio.objects.create(name="Trap Studio", location="New York", price_per_hour=100)
studio2 = Studio.objects.create(name="Drip Sound", location="Los Angeles", price_per_hour=150)

Rent.objects.create(studio=studio1, rent_date=datetime(2025, 6, 5, 14, 0), rent_hours=3)
Rent.objects.create(studio=studio2, rent_date=datetime(2025, 6, 10, 16, 0), rent_hours=2)

print("Данные успешно добавлены!")
