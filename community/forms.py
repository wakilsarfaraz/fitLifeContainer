from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share your progress'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content is required.")
        return content

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError("Category is required.")
        return category