from django.conf.urls.defaults import *

urlpatterns = patterns( 'qimg.views' ,
	url(r'^(?P<width>\d+)x(?P<height>\d+)$', 'qimg'), 
)