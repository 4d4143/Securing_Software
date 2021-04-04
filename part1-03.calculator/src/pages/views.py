from django.http import HttpResponse


# Create your views here.

def addPageView(request):
	firstTerm = int(request.GET.get('first'))
	secondTerm = int(request.GET.get('second'))
	sumTerms = firstTerm + secondTerm
	return HttpResponse(str(sumTerms))
	

def multiplyPageView(request):
	firstTerm = int(request.GET.get('first'))
	secondTerm = int(request.GET.get('second'))
	productTerms = firstTerm * secondTerm
	return HttpResponse(str(productTerms))
