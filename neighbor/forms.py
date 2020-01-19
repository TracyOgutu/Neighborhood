from django import forms
from . models import Neighborhood,UserProfile,Business,News

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        exclude=['editor']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['editor','area']
        widgets={
            'tags':forms.CheckboxSelectMultiple,
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['editor']
        widgets={
            'tags':forms.CheckboxSelectMultiple,
        }