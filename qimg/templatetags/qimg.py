from django import template
from django.core.urlresolvers import reverse
register = template.Library()   
    
@register.simple_tag
def qimg(dimens, some_class="", text=""):
    """
    create a qimg based on the tokens given
    """

    temp = dimens.split("x")
    width = temp[0]
    height = temp[1]

    return u'<img src="%(url)s" width="%(width)s" height="%(height)s" class="%(class)s"/>' % {
        "url": reverse("qimg_text", kwargs=(dict({"width":width, "height":height, "rtext":text}))),
        "width": width,
        "height": height,
        "class": some_class
    }
