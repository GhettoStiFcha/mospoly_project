from django import forms


class MusicForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=1)
    file = forms.FileField()
    image = forms.FileField(allow_empty_file=True)
