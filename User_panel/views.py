import smtplib
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def home(request):
    if(request.method=="POST"):
        SendMessage(request)
    Blood = BloodCampDetails.objects.all().values()
    Detailslength = len(Blood)
    length = False
    if(Detailslength==0):
        length = True
    return render(request,'index.html', {"details": Blood, "length": length})

def Request(request):
    
    if(request.method=="POST"):
        
        username = request.POST['name']
        password = request.POST['password']
        try:
            obj = LoginDetails.objects.filter(Username=username).values()
            Pass = obj[0]['Password']
            print(check_password(password, Pass))
            if(check_password(password, Pass)):
                request.session['username'] = username
                return redirect('/bloodrequest/')
            else:
                messages.warning(request, "Password is wrong")
                return render(request, "login.html")
        except:
            messages.warning(request, "Please check you have entered the correct username")
            return redirect("/login/")
    else:
        return render(request,"login.html")

def Search(request):
    alldatas = DonorDetails.objects.all().values()
    datas = alldatas
    Total = len(alldatas)
    
    if(request.method=="POST"):
        datas = []
        blood = request.POST['bldgroup']
        state = request.POST['state']
        city = request.POST['city']
        print(blood, state, city)
        if(state=="" and city =="" and blood!=""):
            for i in alldatas:
                if(i['BloodGroup']==blood):
                    datas.append(i)
        elif(state!="" and city !=""):
            for i in alldatas:
                if(state!="" and city !="" and blood!=""):
                    if(i['State']==state and i['District']==city and i['BloodGroup']==blood):
                            datas.append(i)
                elif(i['State']==state and i['District']==city):
                    datas.append(i)
        elif(state!="" and city=="" and blood!=""):
            for i in alldatas:
                if(i['State']==state and i['BloodGroup']==blood):
                    datas.append(i)
        else:
            messages.warning(request, "Select the Option First")
        print(datas)
        length = False
        if(len(datas)==0):
            length = True
        return render(request, "search.html", {"instance": datas, "total": Total, "length": length})
        
    return render(request,"search.html", {"instance":datas, "total": Total})

def Register(request):
    
    if(request.method=="POST"):
        RegName = request.POST['name']
        RegEmail = request.POST['email']
        RegGender = request.POST['gender']
        RegBld = request.POST['bldgroup']
        RegDob = request.POST['dob']
        RegState = request.POST['state']
        RegCity = request.POST['city']
        RegAddress = request.POST['address']
        RegContact = request.POST['phNo']
        
        Donor = DonorDetails.objects.all().values()
        DonorEmail = [y["EmailId"] for y in Donor] 
        
        if(RegState!="" and RegCity !="" and len(RegContact)==10 and (RegEmail not in DonorEmail)):
            RegObject = DonorDetails()
            RegObject.Fullname = RegName   
            RegObject.EmailId = RegEmail   
            RegObject.Gender = RegGender  
            RegObject.BloodGroup = RegBld   
            RegObject.DOB = RegDob 
            RegObject.State = RegState 
            RegObject.District = RegCity 
            RegObject.Address = RegAddress
            RegObject.Contact = RegContact
            RegObject.save()
            messages.success(request, "Donor Successfully Registered")
        else:
            show = True
            if(RegState==""):
                print("Please enter the state details")
                messages.warning(request, "Please Select the State")
            elif(RegCity==""):
                print("Please enter the City details")
                messages.warning(request, "Please select the city")
            elif(RegEmail in DonorEmail):
                print("Email is alreasy registered")
                messages.warning(request, "Email id is Already Registered")
            else:
                print("Please enter the Number Correctly")
                messages.warning(request, "Please check the contact number")
                
    return render(request,"register.html")

def ForgetPass(request):
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['password']
        conformpwd = request.POST['Conpassword']
        
        hashpwd = make_password(pwd)
        hashConformpwd = make_password(conformpwd)
        
        if(pwd==conformpwd):
            try:
                details = LoginDetails.objects.all().values()
                Donor = details.filter(Username=name, EmailId=email).update(Password=hashpwd, ConformPassword = hashConformpwd)
                return redirect('/login/')
            except:
                messages.warning(request, "Please check you have entered the correct username")
                return redirect("/forgetPassword/")
        else:
            messages.warning(request, "Password and the Conform Password should be Same")
                
    return render(request, "forget.html")

def Signup(request):
    
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        Phone = request.POST['number']
        pwd = request.POST['password']
        conformpwd = request.POST['Conpassword']
        loginDetails = LoginDetails.objects.all().values()
        loginUsername = [x["Username"] for x in loginDetails]
        loginEmail = [y["EmailId"] for y in loginDetails]   
        
        hashpwd = make_password(pwd)
        hashConformpwd = make_password(conformpwd)
        
        if(pwd==conformpwd):
            
            if((name not in loginUsername) and (email not in loginEmail)):
                loginObj = LoginDetails()
                loginObj.Username = name
                loginObj.EmailId = email
                loginObj.Phonenumber = Phone
                loginObj.Password = hashpwd
                loginObj.ConformPassword = hashConformpwd
                loginObj.save()
                login = User.objects.create_user(username=name,email=email,password=hashpwd)
                login.is_staff = True
                login.save()
                messages.success(request, "Your account has been Created")
                return redirect('login/')
            else:
                messages.warning(request, "Username Is already taken or EmailID is already registered")
        else:
            messages.warning(request, "Password Mismatch...")
            return redirect('signup.html')
        
    return render(request, "signup.html")

def RequestPage(request):
    
    Total = len(DonorDetails.objects.all())
    
    if(request.method=="POST"):
        name = request.POST['name']
        attenderNo = request.POST['attender']
        bldGrp = request.POST['bldGroup']
        units = request.POST['units']
        Reason = request.POST['reason']
        state = request.POST['stateGroup']
        city = request.POST['cityGroup']
        hospital = request.POST['address']
        userid = request.session['username']
        Login = LoginDetails.objects.filter(Username=userid).values()
        userContact = Login[0]['Phonenumber']
        
        if(len(attenderNo)!=10):
            messages.warning(request, "Please enter the valid Phone number")
        elif(bldGrp==""):
            messages.warning(request, "Please enter the valid Blood Group")
        elif(state==""):
            messages.warning(request, "Please Select the state")
        elif(city==""):
            messages.warning(request, "Please Select the City")
        else:
            Details = DonorDetails.objects.filter(District=city, BloodGroup=bldGrp).values()
            EmailList = [x['EmailId'] for x in Details]
            messages.success(request, "Your request has been sent to Our Donors")
            for i in EmailList:
                DonorUser = DonorDetails.objects.filter(EmailId=i).values()
                User = DonorUser[0]['Fullname']
                session = smtplib.SMTP('smtp.gmail.com', 587)
                session.starttls()
                session.ehlo()
                session.login("blood.donor.application@gmail.com","jdoedhfdjoqgvjdu")
                message = f"Hello {User},\n\n----- Blood Needed!!! -----\n\nName: {name}\nAttender Phone number: {attenderNo}\nBlood Group: {bldGrp}\nUnits: {units}\nHospital Details: {hospital}\n\nYou get is details because of you registered in LifeSaver application.\n\nSincerely\n-LifeSaver Team."
                session.sendmail("blood.donor.application@gmail.com",i, message)
                session.quit()
            Request = RequestDetails()
            Request.Patient_Name = name
            Request.Attender_contact_number = attenderNo
            Request.Blood_Group = bldGrp
            Request.Units = units
            Request.Reason = Reason
            Request.State = state
            Request.City = city
            Request.Hospital = hospital
            Request.UserName = userid
            Request.UserPhoneNumber = userContact
            Request.save()
            
    return render(request, "request.html", {"total": Total})

def SendMessage(request):
    
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        thank_message = f"Hi {name},\n\nGreetings from LifeSaver,\nWe wanted to let you know that your Feedback to our application was successfully arrived.\n\nThanks for Using LifeSaver\n\n-Sincerely,\nAdmin"
        
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.ehlo()
        session.login("blood.donor.application@gmail.com","jdoedhfdjoqgvjdu")
        session.sendmail("blood.donor.application@gmail.com", "blood.donor.application@gmail.com", message)
        session.sendmail("blood.donor.application@gmail.com", email, thank_message)
        session.quit()