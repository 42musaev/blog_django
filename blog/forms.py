from django import forms

from blog.models import Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'img']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': CKEditorUploadingWidget()
        }
