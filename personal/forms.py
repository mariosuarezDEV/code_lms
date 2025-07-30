from .models import CustomUser
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'foto_perfil', 'biografia']
        widgets = {
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'foto_perfil': 'Foto de perfil',
            'biografia': 'Biografía',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['foto_perfil'].required = False
        self.fields['biografia'].required = False
        self.helper.layout = Layout(
            Row(
                Column(Field('first_name'),
                       css_class='form-group col-md-6 mb-0'),
                Column(Field('last_name'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Field('foto_perfil'),
            Field('biografia'),
            Submit('submit', 'Actualizar', css_class='btn btn-primary')
        )
