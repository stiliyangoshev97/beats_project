from django.shortcuts import render, redirect

# import our models
from beats.models import Song
from django.core.paginator import Paginator

from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

@login_required
def index(request):
	paginator = Paginator(Song.objects.all(), 1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'page_obj': page_obj}
	return render(request, 'beats/_musicplayer.html', context)


class BeatCreateView(LoginRequiredMixin, CreateView):
	model = Song
	fields = '__all__'
	template_name = 'beats/beat_form.html'


class BeatUpdateView(LoginRequiredMixin, UpdateView):
	model = Song
	fields = '__all__'
	template_name = 'beats/beat_form.html'


class BeatListView(LoginRequiredMixin, ListView):
	model = Song
	context_object_name = "beats"
	template_name = 'beats/beat_list.html'

class BeatDetailView(LoginRequiredMixin, DetailView):
	model = Song
	context_object_name = 'beat_detail'
	template_name = 'beats/beat_detail.html'

class BeatDeleteView(LoginRequiredMixin, DeleteView):
	model = Song
	success_url = reverse_lazy('App:beatslist')
	template_name = 'beats/beat_confirm_delete.html'



