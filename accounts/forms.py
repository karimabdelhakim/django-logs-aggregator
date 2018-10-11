from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            username = username.lower()
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('username already exist')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print(self.cleaned_data)
        if password1 and password2 and password1 == password2:
            return password2
        raise forms.ValidationError("passwords doesn't match")

    def save(self, commit=True):
        user_obj = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        user_obj.set_password(password1)
        if commit:
            user_obj.save()
        return user_obj


class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('wrong username or password')
        self.user = user
        return self.cleaned_data
