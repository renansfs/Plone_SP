import cgi
from Products.Archetypes.Renderer import renderer


class ATWidgetWrapper(object):
    """
    Wrap a Products.Archetypes.generator.widget.widget class
    to intercept the Description method.
    """

    def __init__(self, obj):
        self.obj = obj

    def __call__(self, mode, instance, context=None):
        return self.obj(mode, instance, context)

    def __getattr__(self, name):
        if name == 'Description':
            return self.wDescription
        return getattr(self.obj, name)

    def wDescription(self, instance, **kwargs):
        value = self.obj.description
        if value:
            return cgi.escape(value)
        else:
            return value


def widget(self, field_name, mode="view", field=None, **kwargs):
    """Returns the rendered widget.
    """

    if field is None:
        field = self.Schema()[field_name]
    widget = ATWidgetWrapper(field.widget)
    return renderer.render(field_name, mode, widget, self, field=field,
                           **kwargs)
