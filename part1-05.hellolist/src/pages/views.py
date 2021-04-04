from django.shortcuts import render

# Create your views here.

def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])

	# handling post request
	if request.method == 'POST':
		item = request.POST.get('content', '').strip()
		if len(item) > 0:
			items.append(item)
		request.session['items'] = items

	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
