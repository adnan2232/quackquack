from django import forms

from .models import QuackerProfile

class QuackerProfileForm(forms.ModelForm):
    class Meta:
        model = QuackerProfile
        fields = ('avatar',)
