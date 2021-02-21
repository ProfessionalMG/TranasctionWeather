# Create your views here.
from django.http import JsonResponse
from django.views.generic import FormView, CreateView, ListView

from .forms import AddressForm, WeatherForm, KeysForm
from .models import Weather, Keys
from .utils import weather


# Requirement 1
class IndexView(FormView):
    template_name = 'weather/index.html'
    form_class = AddressForm
    success_url = '/home'

    def form_valid(self, form):
        # TODO: Get Ajax form to work properly
        if self.request.is_ajax():
            data = weather(form.cleaned_data['address'])
            print(data)
            return JsonResponse(data)
        else:
            return super(IndexView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['forecasts'] = Weather.objects.all()
        return context


# Requirement 2
class StoreDBView(CreateView):
    template_name = 'weather/index.html'
    form_class = WeatherForm
    success_url = 'home/'
    # TODO: Get Ajax to store Results from check


# Requirement 3
class HistoricalListView(ListView):
    template_name = 'weather/index.html'
    queryset = Weather
    # TODO: get button showing all historical saves to work


class KeyView(CreateView):
    template_name = 'weather/keys.html'
    form_class = KeysForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(KeyView, self).get_context_data(**kwargs)
        map = Keys.objects.filter(name='Map')
        climate = Keys.objects.filter(name='Weather')
        if map.exists() or climate.exists():
            context['Map'] = map
            context['Weather'] = climate
        return context
    # TODO: Get form validation that only accepts Map and Weather as names
    # TODO: Fix frontend so everyhting looks good
    # TODO: Dynamically add HTML Elements
