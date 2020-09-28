from django.shortcuts import render
from .models import Report

# Create your views here.
def ReportForm(request):
    if request.method == 'POST':
        if len(request.POST['description']) < 1000 and len(request.POST['other']) < 50 and len(request.POST['reporter']) < 30:
            report = Report()
            issues = []
            for problem in Report.PROBLEM_CHOICES:
                if problem[0] in request.POST:
                    issues.append(problem[0])
            report.problem = issues
            report.other = request.POST['other']
            report.description = request.POST['description']
            report.problem_datetime = request.POST['datetime'].replace('/','-')
            report.reporter = request.POST['reporter']
            report.save()
            return render(request, 'reports/report.html', {'Message':True, 'message':'Submitted'})
        else:
            return render(request, 'reports/report.html', {'Message':True, 'message':'Too long'})
        
    return render(request, 'reports/report.html')