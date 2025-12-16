from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
# from django.conf import 
from .models import chai_stores as ChaiStores, chai_menu as ChaiMenu

# Create your views here.

# def chai_details(request):
#     chai = models.chai_menu.objects.all()
#     return HttpResponse({'chai':chai})

def chai_menu(request):
    chais = ChaiMenu.objects.all()
    chai_list = list(chais.values())
    return JsonResponse({'chai': chai_list}, safe=False)

def chai_stores(request):
    stores = ChaiStores.objects.all()
    store_list = list(stores.values())
    return JsonResponse({'chai_stores': store_list}, safe=False)

def chai_storesById(request, chai_id):
    # store = ChaiStores.objects.get(pk=chai_id)
    # store_data = {
    #     'id': store.id,
    #     'name': store.name,
    #     'description': store.description,
    #     'distance': store.distance,
    #     'type': store.type
    # }
    store = get_object_or_404(ChaiStores, pk=chai_id)
    store_data = {
        'id': store.id,
        'name': store.name,
        'description': store.description,
        'distance': store.distance,
        'type': store.type
    }

    return JsonResponse({'chai_store': store_data}, safe=False)
