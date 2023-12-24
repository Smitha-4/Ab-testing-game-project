from django import forms


class Contactform(forms.Form):
    from_email= forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message=forms.CharField(widget=forms.Textarea, required=True)