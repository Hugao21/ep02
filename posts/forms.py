from django import forms
from django.forms import ModelForm

from .models import Category, Comment, Post


class PostForm(ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.order_by('name'),
        widget=forms.CheckboxSelectMultiple,
        label='Categorias',
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'image_url',
            'categories',
            'content',
        ]
        labels = {
            'title': 'Título',
            'image_url': 'URL da imagem de capa',
            'content': 'Conteúdo (HTML)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['categories'].initial = self.instance.categories.all()

    def save(self, commit=True):
        post = super().save(commit=commit)
        if commit:
            post.categories.set(self.cleaned_data['categories'])
        return post


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Autor',
            'text': 'Comentário',
        }
