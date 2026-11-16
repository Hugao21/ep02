from django.forms import ModelForm

from .models import Comment, Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'image_url',
            'content',
        ]
        labels = {
            'title': 'Título',
            'image_url': 'URL da imagem de capa',
            'content': 'Conteúdo (HTML)',
        }


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
