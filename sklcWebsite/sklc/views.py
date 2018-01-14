from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login

from .forms import SignUpForm, LoginForm

def index(request):
	if request.user.is_authenticated:
		return render(request, 'index.html', {})
	else:
		return redirect('login')


def  register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			print('yes')
			form.save()
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'auth/register.html', {'form': form})


@csrf_exempt
def login(request):
	if request.method == 'POST':
		print('===> post')
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			print('===> login')
			return redirect('/')
		# username = request.POST.get('username')
		# password = request.POST.get('password')
		# user = authenticate(request, username=username, password=password)
		# print(user)
		# if user.check_password(password):
		# 	print('===> OK')
		# if user is not None:
		# 	print('====> asdasd')
		# 	# login(request, user)
		# 	# return redirect('/')
	else:
		form = LoginForm()
	return render(request, 'auth/login.html', {})