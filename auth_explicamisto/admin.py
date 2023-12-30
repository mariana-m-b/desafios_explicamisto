from django.contrib import admin
from .models import User, Aluno, Explicador
from django import forms

# Register your models here.
admin.site.register(User)


class AlunoAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlunoAdminForm, self).__init__(*args, **kwargs)
        # filters users to user_type='aluno'
        self.fields['user'].queryset = User.objects.filter(user_type='aluno')

class AlunoAdmin(admin.ModelAdmin):
    form = AlunoAdminForm

class ExplicadorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExplicadorAdminForm, self).__init__(*args, **kwargs)
        # filters users to user_type='explicador'
        self.fields['user'].queryset = User.objects.filter(user_type='explicador')

class ExplicadorAdmin(admin.ModelAdmin):
    form = ExplicadorAdminForm

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Explicador, ExplicadorAdmin)
