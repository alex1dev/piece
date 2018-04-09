from django.contrib import admin
from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main', views.main),
]
