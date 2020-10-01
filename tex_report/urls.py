"""tex_report URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reports import views
from pdf import views as pdfviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ReportForm, name='report'),
    path('createpdf', pdfviews.createPDF, name='createPDF'),
    path('dopdf', pdfviews.testPDF, name='doPDF'),
    path('invoice', pdfviews.get, name='invoice'),
]

from .tasks import build_pdf
from background_task import background
import datetime
#from datetime import timezone
build_pdf(repeat=120)

#print("calling build_pdf")