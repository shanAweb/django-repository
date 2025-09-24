from django.http import HttpResponse

def home(request):
    return HttpResponse("<h3>This is our project</h3>")