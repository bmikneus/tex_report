from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from reports.models import Report

from xhtml2pdf import pisa
from datetime import date
from background_task import background


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    # Creates file saved at destination with filename
    firstdayofweek, lastdayofweek = getDateRangeFromWeek( str( date.today().isocalendar()[0] ), str( date.today().isocalendar()[1] ) )
    destination = "/Users/Brandon Mikneus/Documents/"
    filename = "{}-{}-{}_tex_report.pdf".format(lastdayofweek.month, lastdayofweek.day, lastdayofweek.year)
    file = open(destination + filename, "w+b")

    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')
    print(destination + filename)
    file.close()
    emailPDF(destination + filename)
    # Displays PDF
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



import datetime
import time
def getDateRangeFromWeek(p_year,p_week):

    firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)
    return firstdayofweek, lastdayofweek

from django.core.mail import send_mail, EmailMessage
from django.conf import settings
def emailPDF(filename):
    email = EmailMessage(
        'Big Tex Incident Report', 'The auto-generated Big Tex Incident Report has been attached to this email', settings.EMAIL_HOST_USER,  ['bmikneus@sroassociates.com'])
    email.attach_file(filename)
    email.send()  

    #subject = 'Thank you for registering to our site'
    #message = ' it  means a world to us '
    #email_from = settings.EMAIL_HOST_USER
    #recipient_list = ['brandon.mikneus@gmail.com',]
    #send_mail( subject, message, email_from, recipient_list )
    #return redirect('redirect to a new page')
#Call function to get dates range 
#firstdate, lastdate =  getDateRangeFromWeek('2019','2')

#print('print function ',firstdate,' ', lastdate)