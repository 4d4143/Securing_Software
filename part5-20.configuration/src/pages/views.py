from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account


@login_required
@requires_csrf_token
def transferView(request):
	
	if request.method == 'POST':
		userFrom = User.objects.get(username=request.user)
		userTo = User.objects.get(username=request.POST['to'])
		amount = int(request.POST['amount'])

		accountFrom = Account.objects.get(user=userFrom)
		accountTo = Account.objects.get(user=userTo)

		if accountFrom.balance >= amount and amount >= 0:
			accountFrom.balance -= amount
			accountTo.balance += amount

			accountTo.save()
			accountFrom.save()

		else:
			return redirect('/')

	return redirect('/')



@login_required
def homePageView(request):
	accounts = Account.objects.exclude(user_id=request.user.id)
	return render(request, 'pages/index.html', {'accounts': accounts})
