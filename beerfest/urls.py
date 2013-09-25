from django.conf.urls import patterns, include, url
print "hot here"
urlpatterns = patterns('',
    url(r'^', include('apps.brewkeeper.urls', namespace="brewkeeper", app_name="brewkeeper")),
)
