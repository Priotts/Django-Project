from django import forms
from .models import Certificates

class NewCertificates(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = ['code', 'name_certificate', 'note']
    
    def clean_code(self):
        code = self.cleaned_data['code']
        return code
    
    def clean_name_certificate(self):
        name_certificate = self.cleaned_data ['name_certificate']
        if name_certificate:
            name_certificate = name_certificate.strip()
        return name_certificate

    widget = {
        'code' : forms.TextInput(attrs={'class' : 'form-control'}),
        'name_certificate' : forms.TextInput(attrs={'class' : 'form-control'}),
        'note' : forms.TextInput(attrs={'class' : 'form-control'}),
    }