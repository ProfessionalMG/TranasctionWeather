# Create your views here.
from django.views.generic import FormView

from .forms import AddressForm


class IndexView(FormView):
    template_name = ''
    form_class = AddressForm
