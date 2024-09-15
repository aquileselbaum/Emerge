from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['location', 'description', 'emergencyForMe', 'emergencyForSomeoneElse']
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'Enter your location'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the emergency'}),
        }