from django import forms #импортируем формы джанго
from .models import Post #импортируем модель поста

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)