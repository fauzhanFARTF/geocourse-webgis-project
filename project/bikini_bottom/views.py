from django.shortcuts import render
from django.core.serializers import serialize  #melakukan serialisasi menghasilkan data geojson
from .models import Facility 
from django.http import HttpResponse ,JsonResponse

# Create your views here.
def home(request):
    return render(request, 'pages/home.html') 

def home_map_api(request):
    data = serialize('geojson', Facility.objects.all())
    return HttpResponse(data, content_type="json") 

def custom_map_api(request):
    model = Facility.objects.all()
    for item in model :
        print(item.name)
        
    data = {
        'nama':'faiz',
        'usia': 28,
        'perempuan': False
        }
    return JsonResponse (data)