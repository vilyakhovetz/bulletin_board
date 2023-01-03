from django.views.generic import ListView, DetailView, DeleteView
from adverts.models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from adverts.forms import AdvertCreateForm
from django.urls import reverse_lazy


def adverts_list_view(request):
    if request.GET.get('category'):
        category_slug = request.GET.get('category')
        selected_category = Category.objects.get(slug=category_slug)
        adverts = Advert.objects.filter(category=selected_category)
        if selected_category.get_children():
            for child in selected_category.get_children():
                adverts = adverts | Advert.objects.filter(category=child)
    else:
        adverts = Advert.objects.all()
    paginator = Paginator(adverts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'adverts/index.html', {'adverts': adverts, 'page_obj': page_obj})


@login_required(login_url='/users/login/')
def advert_create_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    if request.GET.get('category'):
        category_slug = request.GET.get('category')
        selected_category = Category.objects.get(slug=category_slug)
        context['selected_category'] = selected_category
        characteristics = selected_category.characteristics.all()
        context['characteristics'] = characteristics
        if request.method == 'POST':
            form = AdvertCreateForm(request.POST)
            context['form'] = form
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
                    CharacteristicValue.objects.create(advert=advert, characteristic=ch, value=request.POST.get(ch.name))

                return redirect('advert_detail', pk=advert.id)
        else:
            form = AdvertCreateForm()
            context['form'] = form
    return render(request, 'adverts/create_advert.html', context)


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


def advert_update_view(request, advert_pk):
    advert = Advert.objects.get(pk=advert_pk)
    category = advert.category
    values = advert.values.all()
    photos = request.FILES.getlist('photos')
    if request.method == 'POST':
        form = AdvertCreateForm(request.POST)
        if form.is_valid():
            advert.title = form.cleaned_data['title']
            advert.content = form.cleaned_data['content']
            advert.price = form.cleaned_data['price']
            advert.city = form.cleaned_data['city']
            advert.street = form.cleaned_data['street']
            advert.building_number = form.cleaned_data['building_number']
            advert.save()

            for value in values:
                value.value = request.POST.get(value.characteristic.name)
                value.save()

            for photo in advert.photos.all():
                if not request.POST.get(str(photo.id)):
                    photo.delete()

            for photo in photos:
                Photo.objects.create(advert=advert, image=photo)

            return redirect('advert_detail', pk=advert.id)
    else:
        default_data = {'title': advert.title, 'content': advert.content,
                        'price': advert.price, 'city': advert.city,
                        'street': advert.street, 'building_number': advert.building_number}
        form = AdvertCreateForm(default_data)

    return render(request, 'adverts/update_advert.html',
                  {'form': form, 'category': category, 'values': values, 'advert': advert})


class AdvertDeleteView(DeleteView):
    model = Advert
    template_name = 'adverts/delete_advert.html'
    success_url = reverse_lazy('my_adverts')
