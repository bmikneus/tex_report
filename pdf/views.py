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

from tex_report.tasks import build_pdf
def get(request):
    pdf = build_pdf()
    return HttpResponse(pdf, content_type='application/pdf')

    