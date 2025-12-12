
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('history/', views.chai_details, name='chai_details'),
    path('menu/', views.chail_menu, name='chail_menu')

]
