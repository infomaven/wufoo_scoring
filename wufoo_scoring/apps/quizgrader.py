#!/usr/bin/python
"""
note: this file has been altered to run on my local machine. to restore, extract from zip
archive and overwrite this file.
"""
#import pyfoo
#from pyfoo import * # GIT it: https://github.com/wufoo/pyfoo
from wufoo_quizzes.libs import pyfoo *
import datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from locals import email_password, api_key, wufoo_account, smtp_host, email_user, admin_email, templates, admin_email_subject, success_message_text_alt, required_score, send_user_emails, send_admin_email, from_email as the_from_email

answers_file = "/Users/admin/DEV/wufooscoring/wufoo_quizzes/answers.txt"
white_paper = "/Users/admin/DEV/wufooscoring/wufoo_quizzes/bestPractices.doc"
try:
    settings.configure(TEMPLATE_DIRS=templates,
    DEBUG=False, TEMPLATE_DEBUG=False, EMAIL_USE_TLS=True, EMAIL_HOST=smtp_host, 
    EMAIL_HOST_USER=email_user, EMAIL_HOST_PASSWORD=email_password,
    EMAIL_PORT=587)
except RuntimeError, e:
    # Setting already configured.
         pass
def get_answer_keys(answers_file="answers.txt"):
    
#    This collects quiz names and answers from a key file
#    in plain text into a dict. The file has a quiz name on the first line
#    followed by answers one per line. The next quiz name appears
#    after the previous quiz's last answer with a line in between.
    
#    You only add the questions you want graded against a specific
#    answer to the answers file. So, don't add name, email, etc.
    
#    Ex.
#    Quiz 1
#    Question 1: Answer 1
#    Question 2: Answer 2
    
#    Quiz 2
#    Question 3: Answer 1
#    Question 4: Answer 2
    
#    becomes:
#    {'Quiz 1' : {'Question 1': 'Answer 1', 'Question 2': 'Answer 2'},
#     'Quiz 2' : {'Question 3': 'Answer 1', 'Question 4': 'Answer 2'}}
    
    quizzes = dict()
    f = open(answers_file, 'r')
    lines = f.readlines()
    lines.append('\n') # in case the file didn't end with a newline, we add one
    
    while len(lines) > 0:
        quiz_name = lines[0].strip() # ignore spaces
        quizzes[quiz_name] = dict()
        for questionAndAnswer in lines[1:lines.index('\n')]:
            lines = lines[lines.index('\n')+1:]
    return quizzes

def get_form(name, quizzes):
""" Retrieve form name from dict """
    for q in quizzes:
        if q.Name == name:
            return q
    raise Exception("Quiz '%s' not found in %s" % (name, [x.Name for x in quizzes]))

def get_answer_key(name):
""" Retrieves values from dict """
    return get_answer_keys()[name]
        
def grade_quiz(answer_key, entry, form, grading_mode):
    """
    Evaluates answers using 2 different scoring styles/modes. 
    1: Answers are multiple choice and there is only one right answer. Each response is worth 1 point.
    2: Answers are YES/NO. NO = 0 points. YES is a user-defined point value
    For both modes - Ignore potential subfields. Return raw score
    """
    num_correct = 0
    perfect_score = 0
    for field in form.fields:
        title = field.Title.strip()
        if grading_mode == "1":
            perfect_score += 1
            # increment actual score by 1 point
            if title in answer_key and answer_key[title] == entry[field.ID]:
                num_correct += 1
        elif grading_mode == "2":
            # increase actual score using pre-determined weight
            perfect_score += answer_key[title]
            if title in answer_key and entry[field.ID] != "No":
                num_correct += answer_key[title]
        else:
            """ incorrect answer gets flagged """
            item = Item(failed=1)
            item.save()
    # return score
    return num_correct    
    
def grade_rating_quiz(entry, form, num_questions, scale):
    """
   Calculates percentage of correct answers in the quiz
    """
    name = form.get_field('Name')
    email = form.get_field('Email')
    exclude = [email.ID, 'HandshakeKey', 'DateCreated', 'FieldStructure',
            'CreatedBy', 'EntryId', 'FormStructure', 'IP',
        'TransactionId', 'LastPage', 'CompleteSubmission', 'Status',
        'LastUpdatedBy', 'PurchaseTotal', 'DateUpdated', 'LastUpdated',
        'Currency', 'UpdatedBy', 'MerchantType']
    if name.ID is None:
        exclude += [sub.ID for sub in name.SubFields]
    else:
        exclude += [name.ID]
    sum = 0
    multiplier = 100/(int(num_questions) * int(scale))
    for field, answer in entry.items():
        if not field in exclude:
            sum += multiplier*int(answer.split('-')[0].strip())
    return sum 
    
# def make_user_email_body(entry, form)
#     """Packages responses into a string for email publishing
#     20140226: nw, Created
#      """
#     myResults = ""
#     for field in form.fields:
#         title = field.Title.string()
#         response = entry[field.ID]
#         myResults += title + ': ' + response + '\n'
#     return myResults
    
def send_admin_email(csv, form, entries, email_field, name_field, location_field):
    """
    send admin email with list of audits
    TODO: send this email once a week 
    """
    plaintext = get_template('weekly-email.txt')
    context = Context({'entry_count':len(entries), 'entries':entries, 'email_field':email_field.ID, 'name_field':name_field.ID, 'location_field':location_field.ID})
    subject, from_email, to = admin_email_subject, admin_email, admin_email
    text_content = plaintext.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to], attachments=[('recent_results.csv', csv, 'text/plain')])
    # msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)

def send_user_email(form, entry):
    """
    send user email containing responses for a single entry using custom markup
    """
    email_field = form.get_field('Email')
    name_field = form.get_field('Name')      
    date_created = form.get_field('Date Created')
    location_field = form.get_field('Location')
    
    # TODO: iterate through entry fields to get the responses
    body_field = build_response(form, entry)
    
    subject, from_email, to = form.Name, the_from_email, entry[email_field.ID] # You may wish to alter this subject for your purposes
    
    # Name might be composed of First and Last subfields
    if name_field.ID is None:
        name = ' '.join([entry[sub.ID] for sub in name_field.SubFields])
    else:
        name = entry[name_field.ID]
    # Just keep the first name
    name = name.split(' ')[0]

# send  message to audit users using a template that knows how to apply the custom formatting (nw)
#    if entry['Grade'] >= required_score
    # invoke the template with this batch of data
    #html = get_template('certificate.html') 
    html = get_template('formatted.html')
    the_date = datetime.datetime.strptime(entry[date_created.ID], "%Y-%m-%d %H:%M:%S")
        
#     context = Context({'name': name.strip(), 'module_name': form.Name, 'date': the_date.strftime("%B %Y")})
    context = Context({'name': name.strip(), 'module_name': form.Name, 'date': the_date.strftime("%B %Y"), 'location': location_field, 'body': body_field})

        
    html_content = html.render(context)
        msg = EmailMultiAlternatives(subject, success_message_text_alt, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        
        print "Sending results to:", entry[email_field.ID]
    """
    else:
        # failure.html is the email template for when the responder did not pass the quiz
        text = get_template('failure.txt')
        context = Context({'name': name.strip(), 'grade' : entry['Grade'], 'avg' : "%.0f" % entry['Avg']})
        content = text.render(context)
    

    html = get_template('failure.html')
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file(white_paper)
    
        
    print "Sending failure message to:", entry[email_field.ID]
    """
    
    # use django and the smtp settings we have to send the message
    msg.send(fail_silently=False)

def show_forms(api):
    """
    Print a list of forms that this API key allows access to.
    """
    for form in api.forms:
        print 'Audit: %s (%s)\n' % (form.Name, form.entry_count)


    
    
def process_quizzes(api, keys):
    """
    Determine which quizzes have corresponding forms and should be graded, then grade those,
    create a CSV of results, and email it.
    - 20140226: added "location" field to models.Entry class
    """ 
    quiz_names = [form.Name for form in api.forms]
    for name, answers in keys.items():
        if name in quiz_names and name in keys.keys(): # we've got a quiz we want to grade
            form = api.forms[0]
            email_field = form.get_field('Email')
            name_field = form.get_field('Name')      
            date_created = form.get_field('Date Created')
            entries = form.get_entries() # By default this returns 100 entries sorted by DateCreated descending
            location = form.get_field('Location')

            print form.Name, 'Audit Results for:' + location
            if not entries:
                print "Score not recorded."
            for entry in entries:
                # Only get entries created in the last N days
                # FIXME specifiable date
                #if datetime.datetime.strptime(entry[date_created.ID], "%Y-%m-%d %H:%M:%S") > (datetime.datetime.now() + relativedelta(weeks=-1)):
                    if 'scale' in answers and 'questions' in answers:
                        grade = grade_rating_quiz(entry, form, answers['questions'], answers['scale'])
                    else:
                        grade = grade_quiz(answers, entry, form)
                    print "%s scored %.2f percent on %s." % (entry[email_field.ID], grade, form.Name)
                    entry["Grade"] = grade

            """Publish results via email"""
            # build formatted email for auditor to pass on to store manager
            # send_formatted_results(entry, form)
            
            """Publish csv file of results"""
            f = open('recent_results.csv', 'w')
            lines = list()
            if entries:
                lines.append(','.join([x.Title for x in form.fields if x.ID in entries[0]] + ['Grade']))
            for entry in entries:
                # Ignoring subfields
                # Only get entries created in the last N days
                # FIXME make the date specifiable
                #if datetime.datetime.strptime(entry[date_created.ID], "%Y-%m-%d %H:%M:%S") > (datetime.datetime.now() + relativedelta(weeks=-1)):
                    line = list()
                    for field in form.fields:
                        if field.ID in entry:
                            if str(entry[field.ID]).count(','):
                                entry[field.ID] = entry[field.ID].replace(',', ' and ') # fix the vexing problem of commas in CSV fields, FIXME should quote the strings
                            line.append(str(entry[field.ID]))
                    line.append(str(entry['Grade']))
                    lines.append(','.join(line))
                    
                    if send_user_emails:
                        send_user_email(form, entry)

            f.write('\n'.join(lines))
            f.close()

            if send_admin_email:
                send_admin_email('\n'.join(lines), form, entries, email_field, name_field)
    
def main():
    """
    Parse the answer key and grade first quiz on Wufoo. Email the results and certificates.
    """
    keys = get_answer_keys(answers_file)
    
    api = PyfooAPI(wufoo_account, api_key)
    
    mode = "2"
    
    #show_forms(api)
    process_quizzes(api, keys, mode)
    
if __name__ == "__main__":
    main()
