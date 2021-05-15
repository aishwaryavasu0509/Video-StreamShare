from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.http import StreamingHttpResponse
from django.core.files.storage import FileSystemStorage
import requests
c=0
filename=[]
@csrf_exempt
def index(request):
    global filename,c
    folder= "/Users/moukthika/mysite/rand_app/static"
    if request.method == 'POST':
        #Recieving and extracting video details
        myfile = request.FILES['messageFile']
        fs = FileSystemStorage(location=folder) 
        #Saving file in static folder
        filename = fs.save(myfile.name, myfile)
        file_url = "http:/"+fs.url(filename)
        if(len(filename)!=0):
            c=1
            return HttpResponse("Video recieved")
            
            
    elif c==0 and request.method == 'GET':
        return HttpResponse("Yet to recieve video")
    else:
        print(filename)
        context={"video":filename}
        #Embedding the video in html file
        return render(request,"index.html",context)

