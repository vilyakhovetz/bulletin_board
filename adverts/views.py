from django.views.generic import ListView, DetailView
from adverts.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from adverts.forms import AdvertCreateForm


class AdvertListView(ListView):
    model = Advert
    template_name = 'adverts/index.html'
    context_object_name = 'adverts'
    paginate_by = 9


@login_required(login_url='/users/login/')
def adverts_create_view(request):
    cities = ['Москва', 'Санкт-Петербург', 'Владивосток']
    categories = Category.objects.all()
    content = {'categories': categories, 'cities': cities}
    if request.GET.get('category'):
        category_slug = request.GET.get('category')
        selected_category = Category.objects.get(slug=category_slug)
        content['selected_category'] = selected_category
        characteristics = selected_category.characteristics.all()
        content['characteristics'] = characteristics
        if request.method == 'POST':
            form = AdvertCreateForm(request.POST)
            content['form'] = form
            photos = request.FILES.getlist('photos')
            if form.is_valid():
                advert = form.save(commit=False)
                advert.author = User.objects.get(pk=request.user.id)
                advert.category = selected_category
                advert.save()

                for ph in photos:
                    Photo.objects.create(advert=advert, image=ph)

                if not photos:
                    Photo.objects.create(advert=advert, image='no_image.png')

                for ch in characteristics:
                    if request.POST.get(ch.name) != '<не указано>':
                        CharacteristicValue.objects.create(advert=advert, characteristic=ch, value=request.POST.get(ch.name))

                # return redirect('index')
                return redirect('advert_detail', pk=advert.id)
        else:
            form = AdvertCreateForm()
            content['form'] = form
    return render(request, 'adverts/create_advert.html', content)


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'adverts/advert_detail.html'
    context_object_name = 'advert'


class MyAdvertsView(ListView):
    model = Advert
    template_name = 'adverts/index.html'
    context_object_name = 'adverts'

    def get_queryset(self):
        return Advert.objects.filter(author=self.request.user.id)
