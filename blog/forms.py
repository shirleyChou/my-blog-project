<<<<<<< HEAD
from .models import Post
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
=======
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()

>>>>>>> d44f324b1a5eb179f6418777b59e2892a1ab4cc8
