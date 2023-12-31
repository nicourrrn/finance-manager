from django.views.generic.base import ContextMixin


class BaseUrlMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_url'] = self.base_url
        return context
