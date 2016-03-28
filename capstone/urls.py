from django.conf.urls import url
from capstone import views as capstone_view
urlpatterns = [
    url(r'^$',capstone_view.home,name='home'),
    url(r'^upload', capstone_view.upload, name='upload'),
]