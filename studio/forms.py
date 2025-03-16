from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from studio.models import Rent

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['rent_date', 'rent_hours']
        widgets = {
            'rent_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'rent_hours': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'rent_date': 'Дата и время',
            'rent_hours': 'Длительность аренды (часы)',
        }
        help_texts = {
            'rent_date': 'Выберите дату и время начала аренды.',
            'rent_hours': 'Укажите, на сколько часов вы хотите арендовать студию.',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        rent = super().save(commit=False)
        rent.user = self.user
        if commit:
            rent.save()
        return rent

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        rent = super().save(commit=False)
        rent.user = self.user
        if commit:
            rent.save()
        return rent