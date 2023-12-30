from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class adicionar_nota(forms.Form):
    name = forms.CharField(label = "Nome de utilizador", max_length=200)
    nota_primeiro_teste = forms.DecimalField(
        label="Nota do primeiro teste",
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0, message='Valor deve ser igual/superior a 0.'),
            MaxValueValidator(20.0, message='Valor deve ser inferior/igual a 20.')
        ]
    )
