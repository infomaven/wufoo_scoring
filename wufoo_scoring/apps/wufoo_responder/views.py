from django.template import RequestContext
from django.shortcuts import render_to_response
from wufoo_quizzes.libs.pyfoo import * # GIT it: https://github.com/wufoo/pyfoo
from django.views.decorators.csrf import csrf_exempt
import json
import wufoo_quizzes.apps.quizgrader
from models import Entry
#from view_wufoo_catcher import *
from django.db.models import Avg
from django.views.generic import DetailView

from wufoo_quizzes.locals import api_key, wufoo_account, send_user_emails, handshake, quiz_name

@csrf_exempt
def email_response(request):
    """ WEBHOOK - Converts wufoo POST request into response containing HTML
        If this gets messed up, restore from original archive on google docs
     """
    container = request.POST.get('form', None)
    if container:
        data = json.loads(container)
    else:
        data = request.POST.copy()
    try:
        if data['HandshakeKey'] != handshake:
            raise Exception("Handshake bad.")
        field_structure = data['FieldStructure']
        email = _get_email_field(field_structure)
    except KeyError, e:
        return render_to_response('bad_input.html', {},
                context_instance=RequestContext(request))

    # Maybe break this out to a nonblocking call
    api = PyfooAPI(wufoo_account, api_key)
    answers = quizgrader.get_answer_key(quiz_name)
    
    #form = quizgrader.get_form("Decision Criteria For Your App Testing Platform",api.forms)
    form = quizgrader.get_form(quiz_name, api.forms)
    
#    grade = quizgrader.grade_rating_quiz(data, form, answers['scale'],
#            answers['questions'])
    """ calculate audit score """
    grade = quizgrader.grade_quiz(answers,entry, form,"2")
    data['Grade'] = grade  # existing code
    
    """ todo: figure out how to parse the following fields from the wufoo POST  """"
    # for testing only, we are using hard-coded values
    location = "American Fork"
    auditName = "Week 3"
    created = datetime.datetime.now()
    
    entry = Entry(grade=grade, data=data, location=location, auditName=auditName, created=created)
    entry.save()
    average = Entry.objects.aggregate(avg=Avg('grade'))
    data['Avg'] = average['avg']
    
    if send_user_emails:
        quizgrader.send_user_email(form, data)

    return render_to_response('email_response.html',
           {'email' : data[email]},
           context_instance=RequestContext(request)) 

def _get_email_field(fs):
    field_name = None
    try:
        fs['Fields']
    except TypeError, e:
        fs = json.loads(fs)
    for f in fs['Fields']:
        if f['Title'] == 'Email':
            field_name = f['ID']
    return field_name

class EntryView(DetailView):
 """ Generic view that can display QUIZ results in HTML format """   
    model = Entry
    template_name = 'results.html'
