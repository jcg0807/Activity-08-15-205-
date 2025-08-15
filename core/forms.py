from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'}),
        }

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        forbidden_words = ['shit', 'fuck', 'bobo']
        for word in forbidden_words:
            if word in username.lower():
                raise ValidationError(f"Username cannot contain the word '{word}'.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords don't match.")
        return cleaned_data

    def save(self, commit=True):
        # Get the unsaved User instance
        user = super().save(commit=False)
        # Hash the password
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
