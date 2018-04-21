import bbcode

from zope import interface


class IRenderable(interface.Interface):
    def render(**context):
        """ renders the object into HTML """


@interface.implementer(IRenderable)
class Renderable(object):
    def html(self, html_field_name='body', **context):
        return bbcode.render_html(getattr(self, html_field_name))
