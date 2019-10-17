from django.shortcuts import render
from webapp.models import filtermodel
# Create your views here.
def Wfilterview(request):
	listdata=filtermodel.objects.all()
	return render(request,'myapp/welcome.html',{'listdata':listdata})

def Ufilterview(request):
	listdata=filtermodel.objects.all()
	return render(request,'myapp/upper.html',{'listdata':listdata})

def Lfilterview(request):
	listdata=filtermodel.objects.all()
	return render(request,'myapp/lower.html',{'listdata':listdata})

def Tfilterview(request):
	listdata=filtermodel.objects.all()
	return render(request,'myapp/title.html',{'listdata':listdata})

def Bfilterview(request):
	return render(request,'myapp/base.html')

def Ofilterview(request):
	listdata=filtermodel.objects.all()
	return render(request,'myapp/other.html',{'listdata':listdata})

def Cfilterview(request):
	listdata=filtermodel.objects.all()
	return render(request,'myapp/custom.html',{'listdata':listdata})


