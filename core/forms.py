from django import forms
from .models import ContactMessage


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Name',
                                                                         'id': 'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                            'class': 'form-control',
                                                            'id': 'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'id': 'message',
                                                           'placeholder': 'message'}))

    def save(self):
        data = self.cleaned_data
        contact_message = ContactMessage.objects.create(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )
        return contact_message
