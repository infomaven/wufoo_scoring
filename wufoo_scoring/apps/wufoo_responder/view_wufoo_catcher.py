from django.shortcuts import render
from django.http import HttpResponseRedirect
import wufoo_quizzes.apps.quizgrader *


""" 
Parses audit data sent by wufoo.com 
Note: This is largely an experiment. I think everything could be
done in views.py.email_response procedure """

def audit_catcher(request):
     """ load data """
    if request.method == 'POST': #if form was submitted
         form = AuditForm(request.POST)
         if form:
             data = json.loads(form)
         else:
             data = request.POST.copy()
         
         if form.is_valid():
             quizgrader.main()
           
         # create & send user emails using cleaned/converted data
         
         
         # create and send admin email with audit scores (missing locations
         # are identified as such
         
         
         return HttpResponseRedirect('/confirmation/')# confirmation page for testing
         
    else:
        form = AuditForm()  # unbound/blank form
        
    return render(request, form_name, {
        'form': form,
    })
