from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	# username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}))
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']



class passwordchangingforms(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        
        

  
class company_form(forms.ModelForm):
    class Meta:
        model = Company_Info
        fields = '__all__'
        # widgets ={
        #     'company_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'company_address': forms.TextInput(attrs={'class':'form-control'}),
        #     'company_logo': forms.FileInput(attrs={'class':'form-control'}),
        #     'company_image': forms.FileInput(attrs={'class':'form-control'}),
        #     'created_date': forms.TextInput(attrs={'class':'form-control'}),
        # }
        # labels={
        #     'company_name': 'Company Name :',
        #     'company_address': 'Company Address :',
        #     'company_logo': 'Created Date :',
        #     'company_image': 'Company Logo :',
        #     'created_date': 'Company Image:',
        # }
  
class device_registration_form(forms.ModelForm):
    class Meta:
        model = Device_Details
        fields = '__all__'
             
class alert_master_form(forms.ModelForm):
    class Meta:
        model = Alert_Master
        fields = '__all__'
        
class user_details_form(forms.ModelForm):
    class Meta:
        model = User_Details
        fields = '__all__'
        
        
