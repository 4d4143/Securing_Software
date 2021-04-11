from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



@login_required
def addView(request):
	if request.method == 'POST':
		newIban = request.POST['iban']
		currentUser = request.user
		newAccount = Account.objects.create(owner=currentUser, iban=newIban)

	return redirect('/')


@login_required
def homePageView(request):
	currentUser = request.user
	accountsList = Account.objects.filter(owner=currentUser)
	accountsIbans = [x.iban for x in accountsList]
	print(accountsIbans)
	return render(request, 'pages/index.html', {'accounts': accountsIbans})
