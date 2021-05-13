

from django.contrib import admin
from django.urls import path
from set.views import (
    set_create_view,
    set_detail_view,
    set_edit_view,
    set_delete_view,
    list_all_sets,
    set_study_view
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'sets' # namespace of app's urls, to not mix up with main urls
urlpatterns = [
    path('', list_all_sets, name='list_sets'),
    path('create/', set_create_view, name='set_create'),
    path('<int:set_id>', set_detail_view, name='set_detail'),
    path('<int:set_id>/edit/', set_edit_view, name='set_edit'),
    path('<int:set_id>/delete/', set_delete_view, name='set_delete'),
    path('<int:set_id>/study/', set_study_view, name='set_study'),

  
]

urlpatterns += staticfiles_urlpatterns()