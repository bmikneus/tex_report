from django.shortcuts import render
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reports.models import Report
from .pdf import doPDF
from tex_report.utils import render_to_pdf, getDateRangeFromWeek
import datetime
from datetime import date
def createPDF(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
# Create your views here.

def testPDF(request):
    reports = Report.objects.all()
   
    doPDF(reports)
    return render(request, 'reports/report.html')


def get(request):
    problems = {'Eyes':0, 'Mouth':0, 'Wrist':0, 'Hand':0, 'Arm':0, 'Forearm':0, 'Shoulder':0, 'Neck':0, 'Nod':0, 'Message':0}
    reports = Report.objects.all()
    for report in reports:
        for issue in report.problem:
            problems[issue] += 1
    
    firstdayofweek, lastdayofweek = getDateRangeFromWeek( str( date.today().isocalendar()[0] ), str( date.today().isocalendar()[1] ) )
    this_week = '{}/{} - {}/{}'.format(firstdayofweek.month, firstdayofweek.day, lastdayofweek.month, lastdayofweek.month)

    data = {
        'week': this_week, 
        'num_reports': len(reports),
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
        'problems': [('Eyes', problems['Eyes']), ('Mouth', problems['Mouth']), ('Wrist', problems['Wrist']), ('Hand', problems['Hand']), ('Arm', problems['Arm']), ('Forearm', problems['Forearm']) , ('Shoulder', problems['Shoulder']), ('Neck', problems['Neck']) , ('Nod', problems['Nod']), ('Message', problems['Message'])],
        'reports': reports

    }
    pdf = render_to_pdf('pdf/report.html', data)
    
    return HttpResponse(pdf, content_type='application/pdf')