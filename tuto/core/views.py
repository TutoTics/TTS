from django.views.generic.base import TemplateView


class BasePageView(TemplateView):
    template_name = "core/base.html"


class DashboardPageView(TemplateView):
    template_name = "dashboard/dashboard.html"

class LoginPageView(TemplateView):
    template_name = 'login/sign-in.html'
