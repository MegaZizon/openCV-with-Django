from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import *
from django.conf import settings
from django.http import HttpResponse ,HttpResponseRedirect
from .cv_functions import cv_detect_face
# Create your views here.
def index(request):
    return render(request,"index.html")

def calculate(request):
    file = request.FILES['fileInput']
    document = Document(file_path=file,file_name="test")
    document2 = Document(file_path=file,file_name="test")
    document.save()
    document2.save()
    context = {'document': document2}
    print(file)
    return render(request,"index.html",context)

def detect(request):
    fid=request.POST['file_id']
    fid=int(fid)
    predeep=Document.objects.get(id=fid-1)
    findeep=Document.objects.get(id=fid)

    cv_detect_face(settings.MEDIA_ROOT_URL + findeep.file_path.url)
    #print(predeep.file_path.path)
    #print(predeep.file_path.url)
    context= {'findeep':findeep, 'document':predeep}
    return render(request, "index.html", context)