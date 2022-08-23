from django import forms
from models import User, Student, Teacher


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


class StudentForm(forms.ModelForm):
    """
        Formulario de registro de estudiantes en la base de datos
        Variables:
    """
    class Meta:
        model = Student
        fields = ('code', 'phone_number', 'address', 'photo')
        widgets = {
            'code': forms.CharField(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'phone_number': forms.CharField(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'address': forms.CharField(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }

            ),
            'photo': forms.FileField(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }

            )
        }


class TeacherForm(forms.ModelForm):
    """
        Formulario de registro de profesores en la base de datos
        Variables:
    """
    class Meta:
        model = Teacher
        fields = ('document', 'address', 'photo', 'phone_number')
        widgets = {
            'document': forms.CharField(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'phone_number': forms.CharField(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'address': forms.CharField(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }

            ),
            'photo': forms.FileField(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }

            )
        }
