from django import forms
class Chat(forms.Form):
    chat = forms.CharField(max_length=255)