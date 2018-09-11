from django import forms


class LoginForm(forms.Form):
    uphonenumb = forms.IntegerField(
        label='手机号码',
        widget=forms.NumberInput(
            attrs={
                'class':'uText',
            }
        )
    )
    upwd = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(
            attrs={
                'class':'uText',
                'placeholder':'请输入密码'
            }
        )
    )