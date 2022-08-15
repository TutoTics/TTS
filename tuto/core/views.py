from django.views.generic.base import TemplateView


class BasePageView(TemplateView):
    template_name = "core/base.html"
