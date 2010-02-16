from django.conf.urls.defaults import *

urlpatterns = patterns( 'qimg.views' ,
	url(r'^(?P<width>\d+)x(?P<height>\d+)$', 'qimg', name='qimg'),
	url(r'^(?P<width>\d+)x(?P<height>\d+)/(?P<rtext>[\d\D\s]+)$', 'qimg', name='qimg_text')
)