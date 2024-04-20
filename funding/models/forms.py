from django import forms

class SignUpForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(label="Contraseña", required=True)
    password2 = forms.CharField(label="Confirmar Contraseña", required=True)

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            self.add_error('password2', "Las contraseñas no coinciden")

        return cleaned_data
