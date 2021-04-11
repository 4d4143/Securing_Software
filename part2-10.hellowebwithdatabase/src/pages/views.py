from django.http import HttpResponse
from .models import Message
import random


# Create your views here.

def homePageView(request):
	try:
		messageId = int(request.GET['id'])
		responseMessage = Message.objects.get(pk=messageId).content
	except:
		responseMessage = 'Id not found'

	return HttpResponse(responseMessage)
