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
    features = []
    
    model = Facility.objects.all()
    for item in model :
        # print(item.name)
        feature = {
            'nama' : item.name,
            'tipe' : item.types,
            'harga' : item. price,
            'satuan_harga' : item.price_unit
        }
        features.append(feature)
    print(features)
    return JsonResponse(features, safe = False)
    
    # data = {
    #     'nama':'faiz',
    #     'usia': 28,
    #     'perempuan': False
    #     }
    # return JsonResponse (data)