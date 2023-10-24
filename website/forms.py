from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name',max_length=100)
    email = forms.EmailField(label='Your email',validators=[EmailValidator()])
    message = forms.CharField(label='Your Message',max_length=1000,widget=forms.Textarea)
    