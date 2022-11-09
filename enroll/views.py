from django.shortcuts import render, redirect
from  django.http import HttpResponse
from .forms import StudentForm, EditForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(req):
	return render(req,"home.html")

def signup(req):
	if req.method == "POST":
		fm = StudentForm(req.POST)
		if fm.is_valid():
			fm.save()
			return HttpResponse('''<h2> Account Created Successfully</h2>
				<button> <a href="/signin"> Click here to login again  </a></button>''')
	else:  
 	    fm = StudentForm()
	return render(req,"signup.html", {'form': fm})


def signin(req):
	if req.method == "POST":
		fm = AuthenticationForm(req, data=req.POST)
		if fm.is_valid():
			unm = fm.cleaned_data['username']
			pwd = fm.cleaned_data['password']
			user = authenticate(username=unm, password=pwd)
			if user is not None:
				login(req, user)
				return redirect('/profile')
	else:
		fm = AuthenticationForm()
	return render(req,"signin.html",{'form': fm})


def profile(req):
	if req.user.is_authenticated:
		if req.method == 'POST':
			fm = EditForm(req.POST,instance=req.user)
			if fm.is_valid():
				fm.save()
				return HttpResponse('''<h2> Account Created Successfully</h2>
				<button> <a href="/profile"> Click here to login again  </a></button>''')
		else:
			fm = EditForm(instance=req.user)
			return render(req,"profile.html",{'name':req.user, 'form':fm})
	else:
		return redirect('/signin')
	

def log_out(req):
	logout(req)
	return redirect('/signin')

#change password with old password
def changepass(req):
	if req.user.is_authenticated:
		if req.method == "POST":
			fm = PasswordChangeForm(user=req.user, data=req.POST)
			if fm.is_valid:
				fm.save()
				return HttpResponse("<h2> Password Changed Successfully</h2>")
		else:
			fm = PasswordChangeForm(user=req.user)
		return render(req,"change1.html",{'form': fm})
	else:
		return redirect('/signin')

#change password without old password

def changepass1(req):
	if req.user.is_authenticated:
		if req.method == "POST":
			fm = SetPasswordForm(user=req.user, data=req.POST)
			if fm.is_valid:
				fm.save()
				return HttpResponse("<h2> Password Changed Successfully</h2>")
		else:
			fm = SetPasswordForm(user=req.user)
		return render(req,"change2.html",{'form': fm})
	else:
		return redirect('/signin')

def info(req):
	x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = req.META.get('REMOTE_ADDR')

	device_type = ""
	browser_type = ""
	browser_version = ""
	os_type = ""
	os_version = ""

	if req.user_agent.is_mobile:
		device_type ="Mobile"
	if req.user_agent.is_tablet:
		device_type = "Tablet"
	if req.user_agent.is_pc:
		device_type = "PC"

	browser_type = req.user_agent.browser.family
	browser_version = req.user_agent.browser.version_string
	os_type = req.user_agent.os.family
	os_version = req.user_agent.os.version_string

	context = {
	         "ip": ip,
	         "device_type": device_type,
	         "browser_type": browser_type,
	         "browser_version": browser_version,
	         "os_type": os_type,
	         "os_version": os_version,
	}
	return render(req, "profile1.html", context)

	