from django.shortcuts import render, redirect
from Daara.form import DocumentForm
from django.core.files.storage import FileSystemStorage
from .models import Document
from markdown import markdown
# Create your views here.

def home(request):
    return render(request, "Daara/home.html",{})

def upload_file(request):
    context ={}
    if request.method =="POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['upload']
            # print(f"The name of document is {uploaded_file.name}")
            # print(f"The size of document is {uploaded_file.size}")
            form.save()
            return redirect("library")
    else:
        form= DocumentForm()
        context["form"]= form
        return render(request,'Daara/upload.html', context)

def list_of_documents(request):
    documents = Document.objects.all()
    #for doc in documents:
        #print(doc.upload.url)
    return render(request, 'Daara/library.html', {"documents":documents})


def delete_document(request, pk):
    if request.method=='POST':
        document = Document.objects.get(id=pk)
        document.delete()
    return redirect('library')


def summarize(request,pk):
   
    document = Document.objects.get(id=pk)
    document.summarization()
    html = markdown(document.summary)
    print(document.summary)
    return render(request,"Daara/sumarization.html",{
        "document":document,
        "text":html,
    })
