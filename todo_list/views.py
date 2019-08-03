from django.shortcuts import render,redirect
from .models import List,Data
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect



# Create your views here.


def home(request):
	if 'username' not in request.session:
		return redirect('log')
	else:

		if request.method=="POST":
			title = request.POST.get('item')
			users=request.POST.get('user')
			usernames=Data.objects.all()
			type(users)

			form=List(item=title,users=users)
			try:
				form.save()
				all_items=List.objects.all()
				user_name=request.session['username']
				
				messages.success(request, "successfully added")
				return redirect('home')
			except :#SQLDecodeError
				messages.success(request, "Task Already exists")
				return redirect('home')
		else:
			user_name=request.session['username']
			messages.warning(request, "Welcome, "+user_name)
			all_items=List.objects.all()
			usernames=Data.objects.all()
			return render(request,'home.html',{'all_items':all_items,'user':user_name,'usernames':usernames})
			

			'''form.save()
				all_items=List.objects.all
				messages.success(request, "successfully added")
				return render(request,'home.html',{'all_items':all_items})'''


def delete(request,list_id):
	if 'username' in request.session:
		item=List.objects.get(pk=list_id)
		item.delete()
		messages.success(request, "Task deleted")
		return redirect('home')
	else:
		messages.warning(request, "login first#### ")
		return redirect('log')

def signup(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('psw')
		profile=request.POST.get('picture')
		print(profile)
		form=Data(username=username,password=password,profile=profile)
		try:
			form.save()
			messages.success(request, "successfully added")
			return redirect('log')
		except:
			messages.success(request, "Username Already Exists")
			return redirect('log')
	
def edit(request,list_id):
	message="edit_msg/"+list_id+"/"
	messages.error(request, message)
	return redirect('home')

def edit_msg(request,list_id):
	if 'username' in request.session:

		item=List.objects.get(pk=list_id)
		item.item=request.POST.get('edit')

		try:
			item.save()
			all_items=List.objects.all
			messages.success(request, "successfully edited")
			return redirect('home')
		except :
			messages.success(request, "Task Already exists")
			return redirect('home')
	else:
		messages.warning(request, "login first +++++")
		return redirect('log')




def uncross(request,list_id):
	if 'username' in request.session:
		item=List.objects.get(pk=list_id)
		if(item.completed=="Not Started"):
			item.completed="In Process"
		elif(item.completed=="In Process"):
			item.completed="Completed"
		elif(item.completed=="Completed"):
			item.completed="In Process"
		item.updated_at= datetime.datetime.utcnow()
		item.save()
		return redirect('home')
	else:
		messages.warning(request, "login first----- ")
		return redirect('log')

def log(request):
	return render(request, "login.html",{})

def login(request):
	
	
	if request.method=="POST":
		user_name=request.POST.get('user_name')
		password=request.POST.get('Password')

		try:
			item=Data.objects.get(username=user_name,password=password)
		
			request.session['username']=user_name

			all_items=List.objects.all
			if 'username' in request.session:
				return redirect('home')
		except:
			messages.warning(request, "Invalid Credentials ")
			return redirect('log')
	else:
			return redirect('log')


def logout(request):
	
	user=request.session['username']
	key_variable = request.session.pop('username')
	
	#del request.session['username']
	messages.success(request, key_variable+" logged out")
	return redirect('log')
   

	