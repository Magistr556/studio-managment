import pytest
from studio.models import Studio, Rent
from django.contrib.auth.models import User
from datetime import datetime

@pytest.mark.django_db
def test_create_studio(studio):
    assert studio.name == "Test Studio"
    assert studio.location == "Test City"
    assert studio.price_per_hour == 200


@pytest.mark.django_db
def test_create_rent(rent):
    assert rent.user.username == 'testuser'
    assert rent.studio.name == 'Test Studio'
    assert rent.rent_hours == 3
    assert rent.total_price == 600
    assert rent.rent_date == datetime(2025, 6, 5, 14, 0)
