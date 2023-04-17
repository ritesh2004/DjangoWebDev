from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.edit import FormView
from home.models import File
import PyPDF2 as pd 
import time
# Create your views here.
def index(request):
    if request.method == "POST":
        files = request.FILES.getlist('file')
        file_list = []
        for file in files:
            doc = File(file=file)
            doc.save()
            file_list.append(str(file))
        try:
            print("Merging started...")
            merger = pd.PdfWriter()
            for pdf in file_list:
                pdf = 'C:\\Users\\rites\\Django_WebDev\\file_uploading_sys\\FileUpload\\media\\' + pdf
                pdffile = open(pdf, 'rb')
                print(pdf)
                reader = pd.PdfReader(pdffile)
                merger.append(reader)
            pdffile.close()
            merger.write("C:\\Users\\rites\\Django_WebDev\\file_uploading_sys\\FileUpload\\media\\merged.pdf")
            return redirect('/media/merged.pdf')
        except:
            print("Something went wrong!")
            return render(request, 'index.html', {'error': 'Something went wrong! Check your network connection'})
    return render(request, "index.html")