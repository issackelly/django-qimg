# Create your views here.
from django.http import HttpResponse, Http404
from django.conf import settings

from PIL import Image, ImageFont, ImageDraw

def qimg(request, width=150, height=150, rtext = None):
    """"
    A View that Returns a PNG Image generated using PIL, arbitrary widht and height
    Fits the width and height into the center of the image
    
    originally baesd on Brad Montgomery"s post
    http://bradmontgomery.blogspot.com/2008/07/django-generating-image-with-pil.html    
    """

    grey = (204,204,204) 
    white = (255,255,255) 
    default_size = 400;

    size = (int(width),int(height))             # size of the image to create
    im = Image.new("RGB", size) # create the image
    draw = ImageDraw.Draw(im)   # create a drawing object that is
    draw.rectangle([0,0,int(width),int(height)],fill=grey)
    
    if not rtext:
        text = width + "x" + height # text to draw
    else:
        text = rtext
    
    # Now, we"ll do the drawing: 
    font = ImageFont.truetype(settings.QIMG_FONT, default_size)
    size = font.getsize(text)
    font_size = int(default_size * 0.7)
    while (size[0]+15) > int(width):
        font = ImageFont.truetype(settings.QIMG_FONT, font_size)
        font_size = int(font_size * 0.7)
        size = font.getsize(text)
    while (size[1]+15) > int(height):
        font = ImageFont.truetype(settings.QIMG_FONT, font_size)
        font_size = int(font_size * 0.7)
        size = font.getsize(text)
    
    text_pos = (((int(width)/2)-(size[0]/2)),(int(height)/2-size[1]*3/8)) # top-left position of our text, centered, 3/8 because of the line-height of the font
    draw.text(text_pos, text, fill=white, font=font)
    del draw # I"m done drawing so I don"t need this anymore

    # We need an HttpResponse object with the correct mimetype
    response = HttpResponse(mimetype="image/png")
    # now, we tell the image to save as a PNG to the 
    # provided file-like object
    im.save(response, "PNG")

    return response # and we"re done!