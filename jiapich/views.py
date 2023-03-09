from django.shortcuts import render, get_object_or_404, redirect

from jiapich.models import submitForm
from jiapich.forms import Form

def lists(request):
    submitForm_list = submitForm.objects.order_by('-created_time')
    context = {'submitForm_list' : submitForm_list}
    return render(request, 'jiapich/form_list.html', context)

def detail(request,submitForm_id):
    submitForm_detail=get_object_or_404(submitForm, pk=submitForm_id)
    context = {'submitForm_detail':submitForm_detail}
    return render(request,'jiapich/form_detail.html',context)

# def submitForm_create(request,submitForm_id):
#     submitForm_create = get_object_or_404(submitModel, pk=submitForm_id)
#     submitForm_create.save()
#     return redirect('jiapich:submitForm_create',submitForm_id=submitForm_create.id)

def form_create(request):
    form=Form()
    return render(request,'jiapich/form_insert.html',{'form':form})