from django.conf.urls import url
from capstone import views as capstone_view
urlpatterns = [
    url(r'^$',capstone_view.home,name='home'),
    url(r'^upload', capstone_view.upload, name='upload'),
    url(r'^api/getMajorOrFatal',capstone_view.getMajorFatal),
    url(r'^api/getCrashByCollisionType',capstone_view.getCrashByCollisionType),
    url(r'^api/getCrashByIntersectionType',capstone_view.getCrashByIntersectionType),
    url(r'^api/getCrashByMonth',capstone_view.getCrashSeverityByMonth),
    url(r'^api/getCrashByVehicleAndAge',capstone_view.getCrashByVehicleAndAge)
]