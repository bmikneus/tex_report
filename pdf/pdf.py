problems = {'Eyes':0, 'Mouth':0, 'Wrist':0, 'Hand':0, 'Arm':0, 'Forearm':0, 'Shoulder':0, 'Neck':0, 'Nod':0, 'Message':0}

def doPDF(reports):
    filename = 'report.pdf'
    for report in reports:
        for issue in report.problem:
            problems[issue] += 1
     
    data = ['', 'Reports this week', '']

    #data.append([ '', 'Reports this week', ''])
    data.append(['Eyes', problems['Eyes'], 'Mouth', problems['Mouth'], 'Wrist', problems['Wrist'], 'Hand', problems['Hand'], 'Arm', problems['Arm'], 'Forearm', problems['Forearm'] , 'Shoulder', problems['Shoulder'], 'Neck', problems['Neck'] , 'Nod', problems['Nod'], 'Message', problems['Message']])



    from reportlab.platypus import SimpleDocTemplate
    from reportlab.lib.pagesizes import letter

    pdf = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    from reportlab.platypus import Table
    table = Table(data)
    from reportlab.platypus import TableStyle
    from reportlab.lib import colors

    style = TableStyle([
        #('BACKGROUND', (0,0), (3,0), colors.green),
        #('TEXTCOLOR', (0,0), (-1,-1), colors.whitesmoke),

        ('ALIGN', (0,0,),(-1,-1), 'CENTER'),

        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,0), (-1,-1), colors.beige),
    ])
    table.setStyle(style)
    ts = TableStyle(
        [
            ('BOX',(0,0),(-1,-1),2,colors.black),
            ('LINEABOVE', (0,2), (-1,2), 2, colors.red),
        ]
    )
    table.setStyle(ts)
    elems = []
    elems.append(table)
    elems.append(table)

    pdf.build(elems)
