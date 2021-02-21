from django.urls import path

from .views import IndexView, HistoricalListView, StoreDBView, KeyView

urlpatterns = [
    path('', KeyView.as_view(), name='keys'),
    path('home/', IndexView.as_view(), name='home'),
    path('store/', StoreDBView.as_view(), name='store'),
    path('list/', HistoricalListView.as_view(), name='list'),

]
