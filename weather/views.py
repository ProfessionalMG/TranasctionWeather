# Create your views here.
import json
from datetime import datetime

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView, CreateView, TemplateView

from .forms import AddressForm, WeatherForm, KeysForm
from .models import Weather, Keys
from .utils import weather


# Requirement 1
class IndexView(FormView):
    template_name = 'weather/index.html'
    form_class = AddressForm
    success_url = '/home'


class VidView(TemplateView):
    template_name = 'base2.html'


def get_address(request):
    if request.method == 'POST':
        post_text = request.POST.get('address')
        response_data = weather(post_text)
        response_data['date'] = str(response_data['date'])
        response_data['address'] = post_text
        # pprint(response_data)

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    return HttpResponse(
        json.dumps({"nothing to see": "this isn't happening"}),
        content_type="application/json"
    )
    # Requirement 2


def get_data(request):
    if request.method == 'GET':
        climate = serialize('json', Weather.objects.all())
        return HttpResponse(
            json.dumps(climate),
            content_type="application/json"
        )


class StoreDBView(CreateView):
    template_name = 'weather/create.html'
    form_class = WeatherForm
    success_url = 'home/'

    def form_valid(self, form):
        data = self.request.POST['address']
        if data:
            info = weather(data)
            form.instance.address = data
            form.instance.date = datetime.strptime(info['date'], '%A, %d %B %Y %H:%M')
            form.instance.feels_like = int(info['feels'])
            form.save()
            return redirect('home')


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
