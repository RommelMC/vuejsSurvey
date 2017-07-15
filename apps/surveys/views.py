from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request,'surveys/index.html')

def info(request):
    if request.method=='POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['lang'] = request.POST['lang']
        request.session['comment'] = request.POST['comment']
        request.session['count'] += 1
        jsonObj = {'text': render(request,'surveys/result.html')}
        return JsonResponse(jsonObj)
    else:
        return redirect('/')

def result(request):
    return render(request, 'surveys/result.html')

def home(request):
    thefile=open('apps/surveys/templates/surveys/survey.html', 'r')
    data=thefile.read().replace('\n','')
    print data
    thefile.close()
    jsonObj = {'text': data}
    return JsonResponse(jsonObj)