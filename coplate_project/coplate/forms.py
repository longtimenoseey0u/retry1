from django import forms
from .models import User

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["nickname"]
	
	def signup(self, request, user):
		user.nickname = self.cleaned_data['nickname'] #추가적인 필드에 대한 값
		user.save()