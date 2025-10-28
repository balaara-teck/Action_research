from django.shortcuts import render,redirect,get_object_or_404
from .models import FileModel
from django.http import FileResponse
import os
import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponse
from django.db.models import Q  
from django.http import JsonResponse
from django.core import serializers 

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)

handler404 = custom_404_view


def search_files(request, category=""):
    
    query = category or request.POST.get('q', '').strip()
    if query:
        uploaded_files = FileModel.objects.filter(
            Q(topic__icontains=query) |
            Q(researcher__icontains=query)|
            Q(field__icontains=query)

           
        )
        return render(request, "index.html", {
        "uploaded_files": uploaded_files,}
        )
   
    else:
        return redirect('home')

def field_topics(request,field):
    all_topics = FileModel.objects.filter(
        Q(field__icontains=field)
        ).order_by('-date_uploaded')
    
    return render(request, "field_topics.html", {
        "all_topics": all_topics,
        "field": field
    })

def under_development_view(request):
    html = """
    <html>
        <head>
            <title>Under Development</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
        <h1>Sorry!!!</h1>
            <h2>This resource is still under development. Please check back later.</h2>
            <button onclick="window.history.back()" style="padding: 10px 20px; font-size: 16px; cursor: pointer;">
                Go Back
            </button>
        </body>
    </html>
    """
    return HttpResponse(html)

def about_view(request):
    return render(request, "about.html")


def donate_view(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        method = request.POST.get("method")

        # You can store, log, or email this info
        print(f"Received {amount} GHS via {method}")
        messages.success(request, "Thank you for your donation!")

        return redirect("donate")
    return render(request, "donate.html")

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # You can process the data here (e.g., send email, save to DB)
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        messages.success(request, "Your message has been sent!")
        return redirect('contact')

    return render(request, 'contact.html')

def File_reader(request, pk):
    file_instance = get_object_or_404(FileModel, id=pk)
    if not file_instance.file:
        return redirect("under_development")
    file_path = file_instance.file.path
    file_name = file_instance.file.name
    file_ext = os.path.splitext(file_name)[1].lower()

    mime_types = {
        '.pdf': 'application/pdf',
    }

    response = FileResponse(open(file_path, 'rb'), content_type=mime_types.get(file_ext, 'application/octet-stream'))
    
    response['Content-Disposition'] = f'inline; filename="{file_name}"'
    response['X-Content-Type-Options'] = 'nosniff' 
   
    return response

def Pricing(request):
    return render(request, "price.html")


def Home(request):
    # Fetch all files in random order
    uploaded_files = list(FileModel.objects.all().order_by('?'))

    # Randomly decide whether to show topics or projects
    choice = random.choice(["topics", "projects"])

    # Randomly pick trending topics if choice is topics
    trending_topics = list(FileModel.objects.all().order_by('?'))[:2] if choice == "topics" else []

    return render(request, "index.html", {
        "uploaded_files": uploaded_files,
        "show_topics": choice == "topics",
        "trending_topics": trending_topics
    })



def load_more_files(request):
    import random
    from .models import FileModel

    limit = int(request.GET.get('limit', 5))
    offset = int(request.GET.get('offset', 0))

    # Randomize results each time
    files = list(FileModel.objects.all().order_by('?'))[:limit]

    data = serializers.serialize('json', files)
    return JsonResponse({'files': data})

def all_topics(request):
    fields = ['Science', 'Technology', 'Mathematics', 'English', 'Languages', 'Social']
    grouped_files = {}

    for field in fields:
        grouped_files[field] = FileModel.objects.filter(field=field).order_by('-date_uploaded')

    return render(request, "all_topics.html", {
        "grouped_files": grouped_files
    })


