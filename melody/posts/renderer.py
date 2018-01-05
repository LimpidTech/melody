import bbcode

from zope import interface


class IRenderable(interface.Interface):
    def render(**context):
        """ renders the object into HTML """


@interface.implementer(IRenderable)
class Renderable(object):
    def html(self, **context):
        return bbcode.render_html(self.body)
