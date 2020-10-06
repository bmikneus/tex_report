from reports.models import Report
from .utils import render_to_pdf, getDateRangeFromWeek

from background_task import background
from datetime import date

#Background_tasks docs https://django-background-tasks.readthedocs.io/en/latest/
# Explanation https://medium.com/@robinttt333/running-background-tasks-in-django-f4c1d3f6f06e
#@background(schedule=60)
def build_pdf():
    print("Running build_pdf")
    problems = {'Eyes':0, 'Mouth':0, 'Wrist':0, 'Hand':0, 'Arm':0, 'Forearm':0, 'Shoulder':0, 'Neck':0, 'Nod':0, 'Message':0}
 
    
    firstdayofweek, lastdayofweek = getDateRangeFromWeek( str( date.today().isocalendar()[0] ), str( date.today().isocalendar()[1] ) )
    this_week = '{}/{} - {}/{}'.format(firstdayofweek.month, firstdayofweek.day, lastdayofweek.month, lastdayofweek.month)

    reports = Report.objects.filter(problem_datetime__lte=lastdayofweek).filter(problem_datetime__gte=firstdayofweek)
    #reports = Report.objects.all()
    print(reports)
    for report in reports:
        #print(report.problem)
        for issue in report.problem:
            problems[issue] += 1
    print(problems)
    data = {
        'week': this_week, 
        'num_reports': len(reports),
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
        'problems': [('Eyes', problems['Eyes']), ('Mouth', problems['Mouth']), ('Wrist', problems['Wrist']), ('Hand', problems['Hand']), ('Arm', problems['Arm']), ('Forearm', problems['Forearm']) , ('Shoulder', problems['Shoulder']), ('Neck', problems['Neck']) , ('Nod', problems['Nod']), ('Message', problems['Message'])],
        'reports': reports

    }
    pdf = render_to_pdf('pdf/report.html', data)
    return pdf