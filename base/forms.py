from allauth.account.forms import LoginForm as AllauthLoginForm, SignupForm as AllauthSignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django import forms


class LoginForm(AllauthLoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Instancia del helper de crispy
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Diseño personalizado del formulario
        self.helper.layout = Layout(
            Field('login', css_class='form-control',
                  placeholder='Correo o usuario'),
            Field('password', css_class='form-control',
                  placeholder='Contraseña'),
            Submit('submit', 'Iniciar sesión',
                   css_class='btn btn-primary w-100 mt-3')
        )


class SignupForm(AllauthSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Instancia del helper de crispy
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Diseño personalizado del formulario
        self.helper.layout = Layout(
            Field('email', css_class='form-control',
                  placeholder='Correo electrónico'),
            Field('password1', css_class='form-control',
                  placeholder='Contraseña'),
            Field('password2', css_class='form-control',
                  placeholder='Confirmar contraseña'),
            Submit('submit', 'Registrarse',
                   css_class='btn btn-primary w-100 mt-3')
        )
