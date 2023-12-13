from django.shortcuts import render, redirect,get_object_or_404
from django.core.serializers import serialize  #melakukan serialisasi menghasilkan data geojson
from .models import Facility 
from .forms import FacilityForm
from django.http import HttpResponse ,JsonResponse
import ast

# Create your views here.
def home(request):
    return render(request, 'pages/home.html') 

def home_map_api(request):
    data = serialize('geojson', Facility.objects.all())
    return HttpResponse(data, content_type="json") 

def custom_map_api(request):
    features = {
        'type': 'FeatureCollection',
        'crs' : {
            'type': 'name',
            'properties': {
                'name' : 'EPSG:4326'
            },
        },
        'features' : []
    }
    
    model = Facility.objects.all()
    for item in model :
        # print(item.name)
        # feature = { 
            # 'nama' : item.name,
            # 'tipe' : item.types,
            # 'harga' : item. price,
            # 'satuan_harga' : item.price_unit
        # }
        feature = {
            'type' :'Feature',
            'geometry': ast.literal_eval(item.location.json),
            'properties' : 
                {
                    'nama' : item.name,
                    'tipe' : item.types,
                    'harga' : item.price,
                    'satuan_harga' : item.price_unit
                },
        }
        features['features'].append(feature)
    # print(features)
    return JsonResponse(features, safe = False)
    
    # data = {
    #     'nama':'faiz',
    #     'usia': 28,
    #     'perempuan': False
    #     }
    # return JsonResponse (data)
    
def facility_form_add(request):
    # pass
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            # logic for post data
            data = form.save(commit=False)
            data.operator = request.user
            data.save()
            return redirect('home')
    else :
        form = FacilityForm()
        
    context =  {
       'form' : form 
    }
    return render(request,'pages/facility_add.html', context)

def facility_form_update(request , pk):
    objek = get_object_or_404(Facility, id=pk)
    form = FacilityForm(request.POST or None, request.FILES or None, instance=objek)
    
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.operator = request.user
            data.save()
            return redirect('facility_list')
    context = {
        'form' : form
    }
    return render(request,'pages/facility_update.html', context)
    
def facility_form_delete(request, pk):
    objek = get_object_or_404(Facility, id=pk)
    form = FacilityForm(request.POST or None, request.FILES or None, instance=objek)
    
    if request.method == 'POST':
        objek.delete()
        return redirect('facility_list')
    context = {
        'form' : form
    }
    return render(request, 'pages/facility_delete.html', context)

def facility_list(request):
    context = {
        # 'data' : Facility.objects.all()
        'data' : Facility.objects.filter(operator = request.user)
    }
    return render(request,'pages/facility_list.html', context)