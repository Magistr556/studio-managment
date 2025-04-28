import pytest
from studio.forms import RentForm
from datetime import datetime
from studio.models import Rent

import datetime


@pytest.mark.django_db
def test_create_rent_from_form(client, user, studio):
    client.login(username=user.username, password='password.123')

    data = {
        'rent_date': '2025-06-05T14:00',
        'rent_hours': 4,
    }

    form = RentForm(data=data, user=user)
    assert form.is_valid()

    rent = form.save(commit=False)
    rent.user = user
    rent.studio = studio
    rent.save()

    saved_rent = Rent.objects.first()
    rent_date_utc = saved_rent.rent_date.astimezone(datetime.timezone.utc)  # rent_date в UTC

    assert rent_date_utc == datetime.datetime(2025, 6, 5, 14, 0, tzinfo=datetime.timezone.utc)
    assert saved_rent.rent_hours == 4
    assert saved_rent.studio == studio
    assert saved_rent.user == user


@pytest.mark.django_db
def test_invalid_rent_form(user, studio):
    # Невалидные данные
    data = {
        'rent_date': 'invalid-date',
        #'rent_hours': -4,
    }

    form = RentForm(data=data, user=user)

    assert not form.is_valid()

    assert 'rent_date' in form.errors
    #assert 'rent_hours' in form.errors

    assert 'Enter a valid date/time.' in str(form.errors['rent_date'])

    # rent_hours с отрицательным значением
    #assert 'Ensure this value is greater than or equal to 0' in str(form.errors['rent_hours'])






