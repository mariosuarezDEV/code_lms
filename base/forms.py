from allauth.account.forms import LoginForm as AllauthLoginForm, SignupForm as AllauthSignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class LoginForm(AllauthLoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(
            Submit('submit', 'Iniciar sesión', css_class='btn btn-primary'))
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class SignupForm(AllauthSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(
            Submit('submit', 'Registrarse', css_class='btn btn-success'))
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
