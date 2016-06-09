from django import forms
from .models import Member, School

# MemberForm class, used to generate the form in the html template used to create the Member model class
class MemberForm(forms.Form):
	memberName = forms.CharField(label='Name', max_length=128)
	memberEmail = forms.CharField(label='Email', max_length=128)
	memberSchool = forms.ModelChoiceField(label='School', queryset=School.objects.all(), to_field_name="name", empty_label=None)

# SchoolForm class, used to generate the form in the html template used to create the School model class
class SchoolForm(forms.Form):
	schoolName = forms.CharField(label='Name', max_length=128)