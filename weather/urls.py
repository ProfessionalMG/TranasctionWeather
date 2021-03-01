from django.urls import path

from .views import IndexView, StoreDBView, KeyView, get_address, get_data, VidView

urlpatterns = [
    path('', KeyView.as_view(), name='keys'),
    path('vid/', VidView.as_view(), name='vid'),
    path('home/', IndexView.as_view(), name='home'),
    path('store/', StoreDBView.as_view(), name='store'),
    path('get_address/', get_address, name='get_address'),
    path('get_data/', get_data, name='get_data'),

]
