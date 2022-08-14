from django import forms
from models import User


class UserForm(forms.ModelForm):
    """
        Formulario de registro de un usuario en la base de datos
        Variables:
            - password1: Contraseña
            - password2: Verificacion de la contraseña
    """

    password1 = forms.CharField(
        label= 'Constraseña',
        widget={
            forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su contraseña',
                    'required': 'required',
                }
            )
        }
    )

    password2 = forms.CharField(
        label='Constraseña de confirmación',
        widget={
            forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirme la contraseña',
                    'required': 'required',
                }
            )
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')
        widgets ={
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                    'required': 'required',
                }
            ),
            'username': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre de usuario',
                    'required': 'required',
                }
            ),
            'name': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese primer nombre',
                    'required': 'required',
                }

            ),
            'last_name': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese primer apellido',
                    'required': 'required',
                }

            )
        }