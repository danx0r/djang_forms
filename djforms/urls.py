from django.conf.urls import url
import djforms.views as views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
