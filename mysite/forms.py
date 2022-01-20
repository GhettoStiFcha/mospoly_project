from django import forms


class MusicForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=1)
    file = forms.FileField()
