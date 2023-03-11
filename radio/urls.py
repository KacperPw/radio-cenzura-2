from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    #path('post/<slug:post_slug>/', views.post_details, name='post_details'),
    path('archive/', views.archive, name='archive'),
    path('archive/<slug:category_slug>/', views.subcategories, name='subcategories'),
    path('archive/<slug:category_slug>/<slug:subcategory_slug>/', views.posts_with_audio, name='posts_with_audio'),
    path('postindex/<str:id>', views.post_index_details, name='post_index_details'),
    path('events/', views.events_list, name='events_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
