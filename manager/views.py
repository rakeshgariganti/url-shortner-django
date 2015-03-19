from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from models import Url
import string,random
# Create your views here.

chrs = string.lowercase + string.uppercase + string.digits

def getrand():
	short = ""
	for i in xrange(6):
		short+=chrs[random.randint(1, 62)]
	return short

def index(request):
	if request.method == 'POST':
		url = Url()
		url.longurl = request.POST['longurl']
		url.short = getrand()
		url.save()
		shortend = request.META['HTTP_REFERER']+url.short
		return render(request,'index.html',{'message':'Successfully created','short':shortend})
	else:
		return render(request,'index.html')

def redirect(request,short):
	longurl = get_object_or_404(Url, short = short)
	return HttpResponseRedirect(longurl.longurl)