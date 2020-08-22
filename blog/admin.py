from django.contrib import admin
from django import forms

from .models import Article

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(
        label="Текс",
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Article
        fields = '__all__'


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['title']
    form = ArticleAdminForm
