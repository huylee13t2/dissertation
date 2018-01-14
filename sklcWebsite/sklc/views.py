from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login

from .forms import SignUpForm

def index(request):
	# Check your logged-in account
	if request.user.is_authenticated:
		return render(request, 'index.html', {})
	else:
		return redirect('login')


def  register(request):
	# check submit register when click button register
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		# check valid form
		if form.is_valid():
			# create account on table User django use function save()
			form.save()
			# After successful register, use redirect to switch to login page
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'auth/register.html', {'form': form})


@csrf_exempt
def login(request):
	# check submit login
	if request.method == 'POST':
		print('===> post')
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			# function login of django
			auth_login(request, user)
			# After successful login, use redirect to switch to home page
			return redirect('/')
	return render(request, 'auth/login.html', {})