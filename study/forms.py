from django import forms


class InfoForm(forms.Form):
    name = forms.CharField(max_length=20, label="名字")
    age = forms.CharField(max_length=20, label="年龄")