from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from entries.models import Ad
from django.core.urlresolvers import reverse
from django.template import RequestContext

def home(request):
	return render_to_response('home.html', {})

def entry(request, ad_id):
	a = Ad.objects.get(id=ad_id)
	return render_to_response('entry.html', {'ad': a}, context_instance=RequestContext(request))

def post(request):
    	return render_to_response('post.html', {},
                               context_instance=RequestContext(request))

def saved(request):
	a = Ad.objects.filter(saved=True)
	return render_to_response('saved.html', {'saved_ads': a})

def saved_true(request, ad_id):
	a = get_object_or_404(Ad, pk=ad_id)
	a.saved = True
	a.save()
	url = '/entry/' + str(ad_id) + '/'
	return HttpResponseRedirect(url)

def posted(request):
	ad = Ad(type=request.POST['type'], title=request.POST['title'], description = request.POST['description'], price=request.POST['price'], date=request.POST['date'], image_url=request.POST['image'], saved=False)
	ad.save()
	if ad.type='Bike':
    	return render_to_response('bikes.html', {})
	else if ad.type='Textbook':
		return render_to_response('textbooks.html', {})

def textbooks(request):
	textbook_list = Ad.objects.filter(type='Textbook')
	return render_to_response('textbooks.html', {'textbook_list': textbook_list})

def bikes(request):
	bike_list = Ad.objects.filter(type='Bike')
	return render_to_response('bikes.html', {'bike_list': bike_list})
