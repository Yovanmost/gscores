from django import forms

class CheckScoreForm(forms.Form):
    sbd = forms.CharField(label="Registration Number", max_length=20)