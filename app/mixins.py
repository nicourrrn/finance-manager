from django.views.generic.base import ContextMixin
from django.http import HttpRequest


counter = 0

class CounterMinix(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request: HttpRequest 
        print(self.request) 
        global counter
        counter += 1
        try: 
            context['counter'] = int(self.request.POST['counter']) + 1
        except Exception:
            context['counter'] = counter
        return context
