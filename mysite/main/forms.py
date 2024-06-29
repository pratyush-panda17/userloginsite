from django import forms

class SignUp(forms.Form):
    is_doctor = forms.BooleanField(label = "Are you a doctor?",required=False)
    f_name = forms.CharField(label = "First Name",max_length=50)
    l_name = forms.CharField(label = "Last Name",max_length=50)
    username = forms.CharField(label = "Username",max_length=50)
    password= forms.CharField(label = "Password",max_length=50)
    confirm_password= forms.CharField(label = "Confirm Password",max_length=50)
    address = forms.CharField(label = "Address",max_length=200)

class Login(forms.Form):
    username = forms.CharField(label = "Username",max_length=50)
    password= forms.CharField(label = "Password",max_length=50)