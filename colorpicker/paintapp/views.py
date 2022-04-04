from django.shortcuts import render
from django.views import View

from paintapp.forms import ColorPickerForm

# Create your views here.
class ColorPickerView(View):
    def get(self, request):
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 200,
            'green': 10,
            'blue': 50,
        }

        return render(request, 'paint.html', context=context)