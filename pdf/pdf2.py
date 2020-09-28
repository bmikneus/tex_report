from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter


from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

def go():
        Story=[]
        ts=TableStyle([('GRID',(0,0),(-1,-1),0.25,"black"),
                      ('BOX',(0,0),(-1,-1),0.25,"black")]
                     )
        #styles = getSampleStyleSheet()
        doc = SimpleDocTemplate("phello.pdf")
         
        cell=[Paragraph('This is not indented',styles['Normal']),
              Indenter(100,100),
              Paragraph('This should be indented',styles['Normal'])]
         
        Story=cell+[Table([[cell]],style=ts)]
        doc.build(Story)

go()