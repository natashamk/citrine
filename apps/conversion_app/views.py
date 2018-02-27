from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
  # the index function is called when root is visited
def index(request):
      return render(request, 'conversion_app/index.html')
    
def multiply(request):
    units = request.POST['multiply']
    unit = units.split("*")
    unit_1 = unit[0]
    unit_2 = unit[1]
    unit_name = unit_names.get(unit_1) + "*" + unit_names.get(unit_2)
    multiplication_factor = round( unit_conversion.get(unit_1) / unit_conversion.get(unit_2), 14)
    return_info = unit_name, multiplication_factor
    return JsonResponse(return_info, safe=False)

def divide(request):
    units = request.POST['divide']
    unit = units.split("/")
    unit_1 = unit[0]
    unit_2 = unit[1]
    unit_name = unit_names.get(unit_1) + "/" + unit_names.get(unit_2)
    multiplication_factor = round( unit_conversion.get(unit_1) / unit_conversion.get(unit_2), 14)
    return_info = unit_name, multiplication_factor
    return JsonResponse(return_info, safe=False)

# SI Unit Conversion
unit_conversion = {'minute': 60, 'hour': 3600, 'day': 86400, 'degree': 3.14/180, 
'second': 3.14/648000 , 'hectare': 10000, 'litre': 0.001, 'tonne': 1000, 'h': 3600,
'd': 86400, 'ha':10000 , 'L': 0.001, 't':1000 }
unit_names = {'minute': "s", 'hour': "s", 'day': "s", 'degree': "rad", 
'second': "rad" , 'hectare': "m2", 'litre': "m3", 'tonne': "kg", 'h': "s",
'd': "s",'ha': "m2" , 'L': "m3", 't':"kg"}
