django-qimg
===========

Installation
------------

*REQUIRES*
  PIL : Python Imaging Library

    clone http://github.com/issackelly/django-qimg
    cd django-qimg
    python setup.py install
    
    # in settings.py
    from distutils.sysconfig import get_python_lib;
    QIMG_FONT = get_python_lib() + '/qimg/fonts/CartoGothic-Std/CartoGothicStd-Book.otf'
    
    # add to INSTALLED_APPS
    'qimg'
    
    #any otf or TrueType font will work, just point QIMG_FONT to the file you want to use
    
    # in urls.py
    (r'^qimg/', include('qimg.urls') ),
    
Usage
------

direct via url:

    GET /qimg/250x150
    # The above outputs a png, 250 wide by 150 tall
    GET /qimg/125x125/adblock
    # outputs a 125x125 block with 'adblock' as the text, not '125x125' which is the default
    
in your template:

    {% load qimg %}
    {% qimg [dimens] [class] [text] %}
    
    # dimens: string '125x125' default 150x150 (with quotes, or a string obj)
    # class: string 'someclass' default qimg
    # text: string '125x125' default <dimens>

    
That's it!

Shoutout
--------
Original view based on this blog post by Brad Montgomery:
<http://bradmontgomery.blogspot.com/2008/07/django-generating-image-with-pil.html>

Thanks to j00bar for patiently helping me move from php to django on irc
    
    