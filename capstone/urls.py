from django.conf.urls import url, include
from capstone import views as capstone_view
urlpatterns = [
    url(r'^$',capstone_view.home,name='home'),
    url(r'^upload', capstone_view.upload, name='upload'),
    url(r'^crash',capstone_view.crash,name='crash'),
    url(r'^map',capstone_view.google_map,name='google_map'),
]