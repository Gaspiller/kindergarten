from django.contrib import admin
from django.urls import path
from user import views as user_views
from dtoken import views as dtoken_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/users/', user_views.UserViews.as_view()),
    path('v1/tokens',dtoken_views.tokens)
]
