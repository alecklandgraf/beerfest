from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('beerfest.apps.brewkeeper.urls', namespace="brewkeeper", app_name="brewkeeper")),
)
