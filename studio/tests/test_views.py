import pytest
from studio.models import Studio, Rent
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_studio_list(client):
    Studio.objects.create(name="Studio One", location="NY", price_per_hour=100)

    url = '/studios/'
    response = client.get(url)

    assert response.status_code == 200
    assert b"Studio One" in response.content


@pytest.mark.django_db
def test_home(client):
    url = '/'
    response = client.get(url)

    assert response.status_code == 200
    assert "Главная" in response.content.decode()


@pytest.mark.django_db
def test_register(client):
    url = '/register/'
    response = client.get(url)
    assert 'Регистрация' in response.content.decode()

    data = {
        'username': 'testuser',
        'password1': 'password.123',
        'password2': 'password.123',
        'email': 'penzabaton@gmail.com'
    }
    response = client.post(url, data)

    assert response.status_code == 302
    assert response.url == '/login/'

    assert User.objects.filter(username='testuser').exists()


@pytest.mark.django_db
def test_logout(client):
    url = '/logout/'
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == '/'
    #assert "Вы больше не рэпер" in str(response.content)


@pytest.mark.django_db
def test_user_profile_and_delete_rent(client, user, studio, rent):
    client.login(username=user.username, password='password.123')

    response = client.get('/accounts/profile/')
    assert response.status_code == 200

    assert b"Test Studio" in response.content

    rent.delete()
    response = client.get('/accounts/profile/')

    assert b"Test Studio" not in response.content
