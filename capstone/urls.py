from django.conf.urls import url
from capstone import views as capstone_view
urlpatterns = [
    url(r'^$',capstone_view.home,name='home'),
    url(r'^upload crash',capstone_view.uploadCrash,name='upload crash'),
    url(r'^upload vehicle',capstone_view.uploadVehicle,name='upload vehicle'),
    url(r'^upload person',capstone_view.uploadPerson,name='upload person'),
    url(r'^clear history',capstone_view.clear_history,name='clear history'),
    url(r'^crash', capstone_view.crash_load,name = 'crash'),
    url(r'^vehicle', capstone_view.uploadVehicle,name = 'vehicle'),
    url(r'^person', capstone_view.uploadPerson,name='person'),
    url(r'^api/getMajorOrFatal',capstone_view.getMajorFatal),
    url(r'^api/getCrashByCollisionType',capstone_view.getCrashByCollisionType),
    url(r'^api/getCrashByIntersectionType',capstone_view.getCrashByIntersectionType),
    url(r'^api/getCrashByMonth',capstone_view.getCrashSeverityByMonth),
    url(r'^api/getCrashByVehicleAndAge',capstone_view.getCrashByVehicleAndAge)
]
