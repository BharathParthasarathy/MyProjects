from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import employee_record ,time_off_table, schedule_table,payroll_table
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django.forms import ModelForm

# - Register/create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']

        # -Login a user

class LoginForm(AuthenticationForm):

        username = forms.CharField(widget=TextInput())
        password = forms.CharField(widget=PasswordInput())

        #-create record form

class CreateRecordForm(forms.ModelForm):
        class Meta:
            model = employee_record
            fields=['emp_id','emp_fname','emp_lname','emp_email','emp_phone','emp_address','emp_designation']

class CreateRecord_payrollForm(forms.ModelForm):
        class Meta:
            model = payroll_table
            fields=['fk_emp_id','emp_sin','emp_account_Number','emp_payrate','pay_cycle']

class UpdateRecord_payrollForm(forms.ModelForm):
        class Meta:
            model = payroll_table
            fields=['fk_emp_id','emp_sin','emp_account_Number','emp_payrate','pay_cycle']

class UpdateRecordForm(forms.ModelForm):
        class Meta:
            model = employee_record
            fields=['emp_id','emp_fname','emp_lname','emp_email','emp_phone','emp_address','emp_designation']

class CreateRecordForm_toff(forms.ModelForm):
        class Meta:
            model = time_off_table
            fields=['emp_id','timeoff_available']

class CreateRecordForm_schedule(forms.ModelForm):
        class Meta:
            model = schedule_table
            fields=['emp_id','assigned_schedule','total_hours','emp_designation','timeoff_id','emp_fname','emp_lname']

class UpdateRecordForm_schedule(forms.ModelForm):
        class Meta:
            model = schedule_table
            fields=['emp_id','assigned_schedule','total_hours','emp_designation','timeoff_id','emp_fname','emp_lname']
