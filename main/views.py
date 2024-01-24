from django.shortcuts import render, redirect
from . import models

# Asosiy menu oynasiga o`tkazadi va osha yerga ma`lumotlar omboridagi kerakli ma`lumotlarni ham yuboradi
def index(request):
    service = models.Service.objects.all()[:3]
    team = models.Team.objects.all()
    sponsours = models.Sponsour.objects.all()
    portfolio = models.Portfolio.objects.all()
    context = {"team":team, 
               "sponsours":sponsours,
               "service":service,
               "portfolio":portfolio
               }
    return render(request, "index.html", context)

# Murojatlar oynasini ochadi. Agar murojat kelsa uni ma`lumotlar omboriga saqlaydi
def contact(request):
    if request.method == "POST":
        print(1)
        models.Contact.objects.create(
            fullname = request.POST['fullname'],
            number = request.POST['number'],
            email = request.POST['email'],
            massage = request.POST['massage']
        )
        return redirect('index')
    return render(request, "contact.html")

# Xizmatlar oynasiga kerakli barcha ma`lumotlarni ma`lumotlar omboridan olib yuboradi
def services(request):
    service = models.Service.objects.all()
    context = {"service":service,}
    return render(request, "services.html", context)

# Blog oynasiga kerakli barcha ma`lumotlarni ma`lumotlar omboridan olib yuboradi
def blog(request):
    blog = models.Blog.objects.all()
    context = {"blog":blog,}
    return render(request, "blog.html", context)
