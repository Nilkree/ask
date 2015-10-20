# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django.conf import settings

from loginsys.forms import UserRegistrationForm
# from api.models import SiteConfiguration

def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		# print username, password
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('site:home')
			
		else:
			args['login_error'] = "Пользователь не найден"
			return render_to_response('loginsys/login.html',args)

	else:
		return render_to_response('loginsys/login.html',args)

def logout(request):
	auth.logout(request)
	return redirect('/')

def registration(request):
	context = {}
	if request.POST:
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			#new_user = form.save()
			username = form.cleaned_data['email']
			try:
				get_user_model().objects.get(username = username)
				context['registration_error'] = 'Ця почтова адреса вже використовується'
			except:
				new_user = User()
				new_user.username = username
				new_user.email = username
				password = form.cleaned_data['password']
				new_user.set_password(password)
				new_user.save()
				user = auth.authenticate(username=new_user.username, password=password)
				#auth.login(request, new_user)
				if user is not None:
					auth.login(request, user)
					return redirect('site:home')
				# return redirect('/auth/login/')

	form = UserRegistrationForm()
	context['form'] =  form
	context.update(csrf(request))            
	return render_to_response("loginsys/registration.html", context)
'''
def agreement(request):
	agreement = SiteConfiguration.objects.get().agreement
	return render_to_response('loginsys/agreement.html', {'agreement' : agreement})				

def agreement_user(request):
	agreement = SiteConfiguration.objects.get().agreement_user
	return render_to_response('loginsys/agreement_user.html', {'agreement' : agreement})	
'''