from datetime import datetime

import pytest
from django.contrib.auth import get_user_model
from studio.models import Studio, Rent


@pytest.fixture
def user(db):
    user = get_user_model().objects.create_user(username='testuser', password='password.123')
    return user

@pytest.fixture
def studio(db):
    studio = Studio.objects.create(name="Test Studio", location="Test City", price_per_hour=200)
    return studio

@pytest.fixture
def rent(db, user, studio):
    rent = Rent.objects.create(studio=studio,
                               user=user,
                               rent_date=datetime(2025, 6, 5, 14, 0),
                               rent_hours=3
                               )
    return rent
