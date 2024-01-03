from django import forms
from .models import Post, Category

categorys = [i for i in Category.objects.all().values_list('name', 'name')]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Title"}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': "", 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=categorys, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Big Text"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Title"}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Big Text"}),
        }
