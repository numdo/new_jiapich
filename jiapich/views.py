from django.shortcuts import render, get_object_or_404, redirect

from jiapich.models import submitForm
from jiapich.forms import Form
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from formtools.wizard.views import SessionWizardView
from .forms import pageStep1,pageStep2,pageStep3,pageStep4,pageStep5,pageStep6
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
class MyFormWizardView(SessionWizardView):
    templates_name = 'form_insert.html'
    form_list = [pageStep1,pageStep2,pageStep3,pageStep4,pageStep5,pageStep6]
    file_storage = None
    success_url = reverse_lazy('form-wizard-done')

    def done(self, form_list, **kwargs):
        # do something with the form data
        return render(self.request, '', {'form_data': [form.cleaned_data for form in form_list]})
