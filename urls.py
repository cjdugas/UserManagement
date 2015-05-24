from django.conf.urls import include, url
from service import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns


#Create a router and register User ViewSet with it
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

#Initiate patterns for log views
urlpatterns = [
    url(r'^log/$', views.LogList.as_view(), name='logIndex'),
    #pattern for logs based on user_id, formatted as a UUID
    url(r'^log/(?P<userid>([a-f0-9]{8}-[a-f0-9]{4}-[1345][a-f0-9]{3}-[a-f0-9]{4}-[a-f0-9]{12}))/$',
        views.LogDetail.as_view(), name='logDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# The API URLs are determined automatically by the router
urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]
