from django.urls import path

from . import views

urlpatterns = [
    path('<str:shopname>', views.PresentViews.as_view())
]
