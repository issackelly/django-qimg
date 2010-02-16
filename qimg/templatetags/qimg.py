from django import template
from django.core.urlresolvers import reverse
register = template.Library()

class QImgNode(template.Node):
    """
    **Processes the QImg Processor Options into Markup**
    """
    argv = dict({
        'url': '/qimg/',
        'class': 'qimg'
    })
    def __init__(self, argv = dict({})):
        self.argv.update(argv)
        
    def render(self, context):
        """
        Renders tag to markup
        """
        return u'<img src="%(url)s" width="%(width)s" height="%(height)s" class="%(class)s"/>' % \
          {'url': reverse('qimg.views.qimg', args=(self.argv['width'], self.argv['height'])), 
          'width': self.argv['width'],
          'height': self.argv['height'],
          'class': self.argv['class']
          }
    
@register.tag
def qimg(parser, token):
    """
    create a qimg based on the tokens given
    """
    text = token.split_contents()
    text.pop(0)
    argv = dict()
    if not text[0]:
        return QImgNode(argv)
    else:
        temp = text[0].split('x')
        argv['width'] = temp[0]
        argv['height'] = temp[1]
        text.pop(0)
    for arg in text:
        if arg.endswith('"') or arg.endswith("'"):
            arg = arg[1:-1]
        if arg.find('=') > -1: #an assignement, not a flag
            item = arg.split('=')
            argv[item[0]] = item[1]
        else:
            argv[item[0]] = True
    return QImgNode(argv)
