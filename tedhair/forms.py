from django import forms
import datetime


class userdetails(forms.Form):
    FirstName = forms.CharField(
        required=True, label="First Name", max_length=30)
    MiddleName = forms.CharField(
        required=False, label="Middle Name", max_length=30)
    LastName = forms.CharField(required=True, label="Last Name", max_length=30)
    DateOfBirth = forms.DateTimeField(required=True)
    PhoneNumber = forms.CharField(required=True, label="Phone Number")
    email = forms.EmailField(required=True, label="Email Address")
    ssn = forms.CharField(required=True, label="SSN")
    page1 = forms.FileField(required=True,
                            help_text='Max. 42 Megabytes'
                            )
    page2 = forms.FileField(required=True,
                            help_text='Max. 42 Megabytes'
                            )
    UtilityBill = forms.FileField(required=True,
                                  help_text='Max. 42 Megabytes'
                                  )
    FirstName.widget.attrs.update(
        {'placeholder': 'First Name', 'class': 'input--style-5'})
    MiddleName.widget.attrs.update(
        {'placeholder': 'Middle Name', 'class': 'input--style-5'})
    LastName.widget.attrs.update(
        {'placeholder': 'Last Name', 'class': 'input--style-5'})
    DateOfBirth.widget.attrs.update(
        {'class': 'input--style-5', 'placeholder': 'YYYY-MM-DD', 'pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2}'})
    ssn.widget.attrs.update(
        {'class': 'input--style-5', 'placeholder': 'xxx-xx-xxxx', 'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{4}'})
    PhoneNumber.widget.attrs.update(
        {'class': 'input--style-5', 'placeholder': 'xxx-xxx-xxxx', 'pattern': '[0-9]{3}-[0-9]{3}-[0-9]{4}'})
    email.widget.attrs.update(
        {'placeholder': 'Email address', 'class': 'input--style-5'})
    page1.widget.attrs.update(
        {'placeholder': 'Driver License Front Page', 'class': 'input--style-5'})
    page2.widget.attrs.update(
        {'placeholder': 'Driver License Back Page', 'class': 'input--style-5'})
    UtilityBill.widget.attrs.update(
        {'placeholder': 'Utility Bill', 'class': 'input--style-5'})
