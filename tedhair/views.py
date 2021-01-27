from django.shortcuts import render, redirect
from .forms import userdetails
from .models import applicant
from django.contrib import messages
#EMAIL  CONFIGURATION#
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# The mail addresses and password
sender_address = 'tedhair92@gmail.com'
sender_pass = 'Passw0rd@12345'
receiver_address = 'garubamalik@gmail.com'
mail_content = "First Name:{}\nMiddle Name:{}\nLast Name: {}\nDOB:{}\n Phone: {}\n Email: {}\n SSN: {}\n"

# END MAIL CONFIG

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
            print("PAGE2: "+str(request.FILES['page2']))
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
            # sendMail(form.cleaned_data['FirstName'], form.cleaned_data['MiddleName'], form.cleaned_data['LastName'],
            #          form.cleaned_data['DateOfBirth'], form.cleaned_data['PhoneNumber'], form.cleaned_data['email'],
            #          form.cleaned_data['ssn'], request.FILES['page1'], request.FILES['page2'], request.FILES['UtilityBill'])
            userinfo.save()
            messages.success(request, 'Form Submission Successful')
            return redirect('home')
    else:
        form = userdetails()
    context = {"userform": form}
    return render(request, "form.html", context)


def sendMail(fn, mn, ln, dob, phone, email, ssn, page1, page2, utility):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'
    mailcontent = mail_content.format(fn, mn, ln, dob, phone, email, ssn)
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Applicant Information'
    message.attach(MIMEText(mailcontent, 'plain'))
    # attach_page1 = open(str(page1), 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((page1).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment',
                       filename=str(page1))
    message.attach(payload)
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
