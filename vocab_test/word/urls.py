from django.urls import path
from . import views

app_name = 'word'

urlpatterns = [
    path("index/", views.index, name="index"),
    path("index/choice/", views.choice, name="choice"),
    path("index/choiceans/<int:question_id>/", views.choiceans, name="choiceans"),
    path("index/write/", views.write, name="write"),
    path("index/writeans/<int:question_id>/", views.writeans, name="writeans"),
    path("<int:wordlist_id>", views.detail, name="detail"),
    path("list/", views.lists, name="list"),
]