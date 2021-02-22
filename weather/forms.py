from django import forms

from weather.models import Weather, Keys


class AddressForm(forms.Form):
    address = forms.CharField(label='Please Enter your address')


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ('address',)


class KeysForm(forms.ModelForm):
    class Meta:
        model = Keys
        fields = '__all__'
