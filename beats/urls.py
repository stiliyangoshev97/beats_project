from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.conf.urls import url
from . import views

app_name = "App"

urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.BeatCreateView.as_view(), name = 'create'),
    path('beatslist/', views.BeatListView.as_view(), name = 'beatslist'),
    url(r'^beatslist/(?P<pk>\d+)/$', views.BeatDetailView.as_view(), name = 'b_detail'),
    #path('beatslist/<int:id>/', views.BeatDetailView.as_view(), name = 'b_detail'),
    url(r'^beatslist/update/(?P<pk>\d+)/$', views.BeatUpdateView.as_view(), name = 'update_beat'),
    url(r'^beatslist/delete/(?P<pk>\d+)/$', views.BeatDeleteView.as_view(), name = 'delete_beat'),

]