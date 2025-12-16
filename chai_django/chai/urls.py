
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('store/', views.chai_stores, name='chai_stores'),
    path('store/<int:chai_id>/', views.chai_storesById, name='chai_store_by_id'),
    path('menu/', views.chai_menu, name='chai_menu')

]

'''
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
user.set_password('new_password')
user.save()

'''