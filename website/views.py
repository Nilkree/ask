from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth import get_user_model 
from django.contrib import auth

from website.models import Question, Answer

# Create your views here.

def home(request):
	if request.user.is_authenticated():
		return redirect('site:wall')
	else:
		args = {}
		args.update(csrf(request))
		if request.POST:
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			# print username, password
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('site:wall')
				
			else:
				args['login_error'] = "Пользователь не найден"
				return render_to_response('loginsys/registration.html',args)

		else:
			return render(request, 'website/home.html', args)

	


def wall(request):
	link = 'localhost:8000/' + request.user.email
	context = {'link' : link}
	return render(request, 'website/wall.html', context)

def get_questions(request):
	questions = Question.objects.filter(to_user=request.user, answered = False)
	print(questions)
	context = {'questions' : questions}
	return render(request,'website/questions.html', context)

def make_answer(request, pk):
	question = Question.objects.get(pk=pk)
	if request.method == 'POST':
		answer = Answer(question=question)
		answer.text = request.POST.get('answer')
		answer.save()
		question.answered = True
		question.save()
		return redirect('site:questions')
	else:
		if request.user == question.to_user:
			context = {'question': question}
			context.update(csrf(request))
			return render(request,'website/make_answer.html', context)
		else:
			context = {'error': 'Этот вопрос поставлен не вам'}
			return render(request,'website/make_answer.html', context)
	
def make_question(request, email):
	try:
		user = get_user_model().objects.get(email = email)
	except get_user_model().DoesNotExist:
		context = {'error': 'Такого пользователя не существует'} 
		return render(request,'website/make_question.html', context)		
	if request.method == 'POST':
		question = Question(to_user=user, text=request.POST.get('question'))
		if request.user.is_authenticated():
			question.from_user = request.user
		question.save()
		return redirect('site:wall')
	else:
		questions = Question.objects.filter(to_user=user, answered = True)
		print(questions)
		context = {'to_user': user, 'questions': questions}
		context.update(csrf(request))
		return render(request,'website/make_question.html', context)



