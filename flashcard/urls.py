
from django.urls import path
from flashcard.views import (
    flashcard_create_view,
    flashcard_edit_view,
    flashcard_delete_view,
    flashcard_detail_view,
    flashcard_list_view,
    flashcard_dynamic_create
   
)

app_name = 'flashcards' # namespace of app's urls, to not mix up with main urls
urlpatterns = [
    path('', flashcard_list_view, name='flashcard_list'),
    path('create/', flashcard_create_view, name='flashcard_create'),
    path('dynamic/create/', flashcard_dynamic_create, name='flashcard_dynamic'),
    path('<int:flashcard_id>', flashcard_detail_view, name='flashcard_detail'),
    path('<int:flashcard_id>/edit/', flashcard_edit_view, name='flashcard_edit'),
    path('<int:flashcard_id>/delete/', flashcard_delete_view, name='flashcard_delete'),
]
