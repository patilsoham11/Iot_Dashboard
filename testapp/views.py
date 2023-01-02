from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from matplotlib.style import context
from .forms import *
from testapp.models import scan_data, print_data, Alert_Master
from datetime import datetime
from django.db.models import Q
from django.core.mail import send_mail


# Create your views here.


def base(request):
    # reg = Alert_Master.objects.filter(register=0)
    # msg = Alert_Master.objects.filter(alert_massage)
    context = {
        # 'reg':reg,
        # 'msg' :msg,
    }
    # print(reg)
    # return render(request, 'base.html',context)


def first_machine(request):
    return render(request, 'machine1.html')


def second_machine(request):
    return render(request, 'machine2.html')


# def demo(request):
#     return render(request,'demo.html', context)



def home(request):
    # machin_data = scan_data.objects.all()
    machin_data1 = scan_data.objects.filter(ok_signal='(ok)').count()
    machin_data2 = scan_data.objects.filter(ok_signal='None').count()
    machin_data3 = scan_data.objects.filter(ok_signal='(AL)').count()
    machin_data4 = scan_data.objects.filter(ok_signal='(F )').count()
    total = [machin_data1+machin_data2+machin_data3+machin_data4]


    from datetime import datetime
    import mysql.connector
    from django.db import connection
    
    from django.db.models import Count

    
    from datetime import datetime
    from django.db.models import Count
    from django.contrib.auth.models import User
    
    cursor = connection.cursor()

    # ------------------Live Progress Chart-----------------------
    from django.db import connection

    cursor = connection.cursor()
    cursor.execute('''select hour(first_scan_datetime),count(ok_signal) from scan_data where ok_signal= '(ok)' group by hour(first_scan_datetime) order by hour(first_scan_datetime)''')
    row = cursor.fetchall()
    hour,count=zip(*row)
    hour1 = ','.join(map(str,hour))
    count1 = ','.join(map(str,count))
    # print(hour1)
    # print(count1)

    cursor1 = connection.cursor()
    cursor1.execute('''select hour(first_scan_datetime),count(ok_signal) from scan_data where ok_signal= 'None' group by hour(first_scan_datetime) order by hour(first_scan_datetime)''')
    row1 = cursor1.fetchall()
    hour,count=zip(*row1)
    # hour1 = ','.join(map(str,hour))
    count2 = ','.join(map(str,count))
    # print(count2)
    
    # ==============================for notification badge ===========================================================
    
    reg = Alert_Master.objects.filter(register=0)
        
    context = {
        # 'mystring':mystring,
        # 'machin_data':machin_data,
        'machin_data1': machin_data1,
        'machin_data2': machin_data2,
        'machin_data3': machin_data3,
        'total': total,
        'hour1': hour1,
        'count1':count1,
        'count2':count2,
        'reg':reg,
        
    }
    return render(request, 'index.html', context)


# from django.shortcuts import render
# from twilio.rest import Client
# from django.http import HttpResponse

# def msgs(request):
#     reg = Alert_Master.objects.filter(register=0)
#     if reg < 1:
        
#         account_sid = 'ACbf006fd11a72689c80ec0bc8e8012c02'
#         auth_token = 'd128f871cf42beae11e3dae639eadb9d'
#         client = Client(account_sid, auth_token)

#         message = client.messages.create(
#                                     body=f'your Plc register number is {register} and msg is {alert_massage}',
#                                     from_='+13089373173',
#                                     to='+917498335002' 
#                                 )
        
#         return HttpResponse('Message Sent Successfully..')
#     else:
#         return HttpResponse('error')


def data_tabel(request):
    machin_data = scan_data.objects.all()
    context = {
        'machin_data': machin_data,

    }
    return render(request, 'table.html',context)


def charts(request):
    machin_data1 = scan_data.objects.filter(ok_signal='(ok)').count()
    machin_data2 = scan_data.objects.filter(ok_signal='None').count()
    machin_data3 = scan_data.objects.filter(ok_signal='(AL)').count()
    machin_data4 = scan_data.objects.filter(ok_signal='(F )').count()
    total = [machin_data1+machin_data2+machin_data3+machin_data4]
    context = {
        # 'mystring':mystring,
        # 'machin_data':machin_data,
        'machin_data1': machin_data1,
        'machin_data2': machin_data2,
        'machin_data3': machin_data3,
        'total': total,
       
    }
    return render(request, 'charts.html',context)


# login page
def login_user(request):
	# if not request.user.is_authenticated:
	if request.method == 'POST':  # if someone fills out form , Post it
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:  # if user exist
			login(request, user)
			messages.success(request, ('succesfully Login !!!!..'))
			return redirect('home')  # routes to 'home' on successful login
		else:
			messages.error(request, ('Please enter a correct username and password.'))
			return redirect('login')  # re routes to login page upon unsucessful login
	else:
		return render(request, 'login.html', {})
	# else:
	# 	return redirect('home')

# logout page


def logout_user(request):
	logout(request)
	messages.error(request, ('Youre now logged out'))
	return redirect('login')

# register page


def register_user(request):

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# username = form.cleaned_data['username']
			# password = form.cleaned_data['password1']
			# user = authenticate(username=username, password=password)
			# login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('login')
	else:
		form = SignUpForm()

	context = {'form': form}
	return render(request, 'register.html', context)


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = EditUserProfileForm(request.POST, instance= request.user)
            if form.is_valid():
                form.save()
                messages.success(request, ('Your Prifile Updated'))
                return redirect('home')
        else: 		#passes in user information
            form = EditUserProfileForm(instance= request.user)

        context = {'form': form}
        return render(request, 'edit_profile.html',context)
    else:
        return redirect('home')

# this urls used for chagne user password 
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView


def PasswordChangeView(PasswordChangeView):
    from_class = passwordchangingforms
    success_url = reverse_lazy('login')


def forgot_password(request):
    return render(request, 'forgot_password.html')


# MASTERS
######################  Company Information  ######################
def company(request):
    cm = Company_Info.objects.all()
    context = {
		'cm': cm,
 	}
    return render(request, 'masters/company/company.html', context)

def add_company(request):
    if request.method == "POST":
        company_name = request.POST["company_name"]
        company_address = request.POST["company_address"]
        company_logo = request.FILES["company_logo"]
        company_image = request.FILES["company_image"]
        created_date=request.POST["created_date"]
        # updated_date=request.POST["updated_date"]
        # deleted_date=request.POST["deleted_date"]
        info_company = Company_Info.objects.create(
            company_name=company_name, company_address=company_address, created_date=created_date, company_logo=company_logo, company_image=company_image)
        info_company.save()
        return redirect('company')

    return render(request, 'masters/company/add_company.html')

# this function will update/delete
def update_data(request, id):
    if request.method == "POST":
        pi = Company_Info.objects.get(pk=id)
        fm = company_form(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('company')
    else:
        pi = Company_Info.objects.get(pk=id)
        fm = company_form(instance=pi)
        
    return render(request, 'masters/company/updatecompany.html', {'form': fm})

# this function will delete
def delete_data(request, id):  
    if request.method == "POST":
        pi = Company_Info.objects.get(pk=id)  
        pi.delete()
        return redirect('company')



#######################  Device Details #########################
def device_details(request):
    cm = Device_Details.objects.all()
    context = {
		'cm': cm,
 	}
    return render(request, 'masters/device/device_details.html', context)

def add_device(request):
    cm = Company_Info.objects.all()
    if request.method == 'POST':
	    form = device_registration_form(request.POST)
	    if form.is_valid():
		    form.save()
		    # messages.success(request,("Employee REsignation Added successful  !!!"))
		    return redirect('device_details')
    else:
	    form = device_registration_form()

    context = {
		'cm': cm,
		'form': form
 	}
    return render(request, 'masters/device/add_device.html', context)

def update_device(request, id):
    if request.method == "POST":
        pi = Device_Details.objects.get(pk=id)
        fm = device_registration_form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('device_details')
    else:
        pi = Device_Details.objects.get(pk=id)
        fm = device_registration_form(instance=pi)
        
    return render(request, 'masters/device/updatedevice.html', {'form': fm})

def delete_device(request, id):  
    if request.method == "POST":
        pi = Device_Details.objects.get(pk=id) 
        pi.delete()
        return redirect('device_details')



####################### Alert Masters ###########################
def alert_details(request):
    cm = Alert_Master.objects.all()
    context = {
		'cm': cm,
 	}
    return render(request, 'masters/alertmaster/alert_details.html', context)

def add_alertmaster(request):
    cm = Device_Details.objects.all()
    if request.method == 'POST':
	    form = alert_master_form(request.POST)
	    if form.is_valid():
		    form.save()
		    # messages.success(request,("Employee REsignation Added successful  !!!"))
		    return redirect('alert_details')
    else:
	    form = alert_master_form()

    context = {
		'cm': cm,
		'form': form
 	}
    return render(request, 'masters/alertmaster/add_alert.html', context)

def update_alert(request, id):
    if request.method == "POST":
        pi = Alert_Master.objects.get(pk=id)
        fm = alert_master_form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('alert_details')
    else:
        pi = Alert_Master.objects.get(pk=id)
        fm = alert_master_form(instance=pi)
        
    return render(request, 'masters/alertmaster/update_alert.html', {'form': fm})


def delete_alert(request, id):  
    if request.method == "POST":
        pi = Alert_Master.objects.get(pk=id) 
        pi.delete()
        return redirect('alert_details')

#################################### User Detials ########################################

def user_details(request):
    cm = User_Details.objects.all()
    context = {
		'cm': cm,
 	}
    return render(request, 'masters/user/user_details.html', context)



def add_user(request):
    cm = Company_Info.objects.all()
    if request.method == 'POST':
	    form = user_details_form(request.POST)
	    if form.is_valid():
		    form.save()
		    # messages.success(request,("Employee REsignation Added successful  !!!"))
		    return redirect('user_details')
    else:
	    form = user_details_form()

    context = {
		'cm': cm,
		'form': form
 	}
    return render(request, 'masters/user/adduser.html', context)



def update_user(request, id):
    if request.method == "POST":
        pi = User_Details.objects.get(pk=id)
        fm = user_details_form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('user_details')
    else:
        pi = User_Details.objects.get(pk=id)
        fm = user_details_form(instance=pi)
    
    context = {
		'form': fm,
 	}
        
    return render(request, 'masters/user/updateuser.html', context)



def deleteuser(request, id):  
    # if request.method == "POST":
        pi = User_Details.objects.get(pk=id)  
        pi.delete()
        return redirect('user_details')

















































































######################## only for practice #############################

# demo templates
# def temp_one(request):
#     cm = Company_Info.objects.all()
#     context={
# 		'cm':cm,
# 		# 'form':form
#  	}
#     return render(request,'demotemp/tempone.html', context)


# only for best practice example(rough)
# def create_stud(request):
#     form = StudForm()
#     if request.method == "POST":
#         form = StudForm(request.POST, request.FILES)

#         if form.is_valid():
#             try:
#                 form.save()
#                 messages.success(request, "Created successful!")
#                 return redirect('/show_stud')
#             except:
#                 message = "Something we are wrong!"
#                 form = StudForm()
#             return render(request, 'create.html',{'message':message,'form':form})
#     else:
#         form = StudForm()
#     return render(request, 'create.html',{'form':form})


# only for best practice example(rough)
# def update_stud(request, id):
#     stud = Stud.objects.get(id=id)
#     if request.method == "POST" :
#         form = StudForm(request.POST, request.FILES, instance = stud)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Update successful!')
#             return redirect("/show_stud")
#         message = 'Something we are wrong!'
#         return render(request, 'edit.html',{'message':message,'stud':form})
#     else:
#         form = Stud.objects.get(id=id)
#         stud = StudForm(instance = form)
#         content = {'stud':stud,'id':id}
#         return render(request, 'edit.html',content)











