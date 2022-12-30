from django.views.generic import ListView
from adverts.models import *


class AdvertListView(ListView):
    model = Advert
    template_name = 'adverts/index.html'
    context_object_name = 'adverts'
    paginate_by = 1
