from django import forms          
from berita.models import Artikel

class ArtikelForm(forms.ModelForm):

    class Meta:
        model = Artikel
        fields = ('judul', 'isi', 'kategori', 'thumbnail')
        widgets = {

            "judul" : forms.TextInput(
                attrs={
                    'class': 'from-control',
                }),
            "isi" : forms.Textarea(
                attrs={
                    'class': 'from-control',
                }),
            "kategori" : forms.Select(
                attrs={
                    'class': 'from-control',
                }),
        }