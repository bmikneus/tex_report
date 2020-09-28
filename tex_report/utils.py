from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
from datetime import date

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)


    firstdayofweek, lastdayofweek = getDateRangeFromWeek( str( date.today().isocalendar()[0] ), str( date.today().isocalendar()[1] ) )
    #print('{}/{} - {}/{}'.format(firstdayofweek.month, firstdayofweek.day, lastdayofweek.month, lastdayofweek.month))
    #print(firstDay.month + '/' + firstDay.day + ' - ' + lastDay.month + '/' + lastDay.day)
    destination = "/Users/Brandon Mikneus/Documents/"
    filename = "{}-{}-{}_tex_report.pdf".format(lastdayofweek.month, lastdayofweek.day, lastdayofweek.year)
    file = open(destination + filename, "w+b")

    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



import datetime
import time
def getDateRangeFromWeek(p_year,p_week):

    firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)
    return firstdayofweek, lastdayofweek


#Call function to get dates range 
#firstdate, lastdate =  getDateRangeFromWeek('2019','2')

#print('print function ',firstdate,' ', lastdate)