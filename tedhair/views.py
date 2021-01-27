from django.shortcuts import render, redirect
from .forms import userdetails
from .models import applicant
from django.contrib import messages

# Create your views here.
# from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")


def frmUserDetails(request):
    if request.method == 'POST':
        form = userdetails(request.POST, request.FILES)
        if form.is_valid():
            print("First Name: "+form.cleaned_data['FirstName'])
            print("Middle Name: "+form.cleaned_data['MiddleName'])
            print("Last Name: "+form.cleaned_data['LastName'])
            userinfo = applicant(first_name=form.cleaned_data['FirstName'],
                                 middle_name=form.cleaned_data['MiddleName'],
                                 last_name=form.cleaned_data['LastName'],
                                 dob=form.cleaned_data['DateOfBirth'],
                                 PhoneNumber=form.cleaned_data['PhoneNumber'],
                                 email=form.cleaned_data['email'],
                                 ssn=form.cleaned_data['ssn'],
                                 page1=request.FILES['page1'],
                                 page2=request.FILES['page2'],
                                 UtilityBill=request.FILES['UtilityBill']
                                 )
            userinfo.save()
            messages.success(request, 'Form Submission Successful')
            return redirect('home')
    else:
        form = userdetails()
    context = {"userform": form}
    return render(request, "form.html", context)
