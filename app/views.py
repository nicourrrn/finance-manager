from django.views import generic
from django.urls import reverse_lazy

from .models import Operation, Category
from .mixins import CounterMinix, BaseUrlMixin 

class CounterView(CounterMinix, generic.TemplateView):
    template_name = "app/counter.html"

class IndexPageView(generic.TemplateView):
    template_name = "app/index.html"


class OperationListView(generic.ListView):
    model = Operation
    paginate_by = 100
    context_object_name = "operations"

class OperationCreateView(BaseUrlMixin, generic.CreateView):
    model = Operation 
    success_url = reverse_lazy("operations") 
    base_url = reverse_lazy("create_operation")
    fields = "__all__"
    template_name = "app/models_form.html"

    def get_form(self):
        form = super().get_form()
        form.fields["short_description"].required = False
        form.fields["desctiption"].required = False
        return form


class CategoryListView(generic.ListView):
    model = Category 
    paginate_by = 20
    context_object_name = "categories"

class CategoryCreateView(BaseUrlMixin, generic.CreateView):
    model = Category
    success_url = reverse_lazy("categories") 
    base_url = reverse_lazy("create_category")
    fields = "__all__"
    template_name = "app/models_form.html"


