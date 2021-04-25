from django import forms
from .models import Teacher

class FormTeacher(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=["firstName", "lastName", "email", "phone"]