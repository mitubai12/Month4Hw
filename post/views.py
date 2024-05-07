from typing import Any
import random

from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Images
from django.db.models import Q

from django.forms.models import BaseModelForm
from django.shortcuts import render, HttpResponse, redirect

from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from post.models import Cars
from post.forms import CarForm2, SearchForm, ImageForm


jokes = [
    "С отправленным на Марс американским марсоходом прервалась связь.\nЧерез неделю его нашли в Узбекистане с перебитыми номерами.",
    "Перед свадьбой думаешь, что лучше ее не бывает, перед разводом, что хужеее не бывает, и каждый раз ошибаешься!",
    "Футболист сборной России Павел Погребняк так долго сидит на скамейкезапасных 'Штутгарта', что к нему стали присматриваться грифы."
]


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')


class AnekdotView(View):
    joke = random.choice(jokes)

    def get(self, request):
        return HttpResponse(self.joke)


class MainView(View):
    template_name = 'main.html'

    def get(self, request):
        return render(self.request, self.template_name)


def post_list_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        category = request.GET.get('category')
        ordering = request.GET.get('ordering')
        page = int(request.GET.get('page', 1))
        search_form = SearchForm(request.GET)
        posts = Cars.objects.all().select_related('user').prefetch_related('category')
        if search:
            posts = posts.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        if category:
            posts = posts.filter(category__id__in=category).distinct()
        if ordering:
            posts = posts.order_by(ordering)
        limit = 3
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)
        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]
        context = {'posts': posts, 'name': "Mitu", 'search_form': search_form, 'max_pages': range(1, max_pages + 1)}
        return render(request, 'post/post_list.html', context)

@login_required
def post(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':

        postForm = CarForm2(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = CarForm2()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'post/post_create.html',
                  {'postForm': postForm, 'formset': formset})


class PostDetailView(DetailView):
    model = Cars
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context['name'] = "Mitubai"
        return context


class PostCreateView(CreateView):
    model = Cars
    form_class = CarForm2
    template_name = 'post/post_create.html'
    success_url = '/posts/'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_view')
        form = self.get_form()
        return self.render_to_response({'form': form})

    def form_valid(self, form: BaseModelForm) -> Any:
        form.instance.author = self.request.user
        self.object = form.save()
        return redirect(self.get_success_url())


class PostUpdateView(UpdateView):
    model = Cars
    form_class = CarForm2
    template_name = 'post/post_update.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
    success_url = '/posts/'

