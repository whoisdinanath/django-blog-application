from django.forms import ModelForm
from .models import *
from django import forms

class BlogCreation(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'overview', 'thumbnail', 'content', 'featured' ]
        widgets = {
            
            'thumbnail': forms.FileInput()
        }


    def __init__(self, *args, **kwargs):
        super(BlogCreation, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control mr-0'})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'comment']


    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class ContactForm(ModelForm):
    class Meta:
        model= Contact
        fields = ['user_name', 'email', 'subject', 'message']
        labels = {
            'user_name':'Name'
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control mr-0 ml-auto'})