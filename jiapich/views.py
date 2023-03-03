from django.shortcuts import render

from jiapich.models import Form


def hello(request):
    print(request)
    return render(request, '/jiapich/hello.html',{'title':'hello', 'body':'world'})

def lists(request):
    models = Form.objects.all()
    Form.objects.__str__()
    return render(request, 'jiapich/formList.html',{'models':models})