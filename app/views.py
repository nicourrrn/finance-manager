from django.views import generic
from django.urls import reverse_lazy

from .models import Operation, Category

class IndexPageView(generic.TemplateView):
    template_name = "app/index.html"

class OperationListView(generic.ListView):
    model = Operation
    paginate_by = 100
    context_object_name = "operations"

class OperationDetailView(generic.DetailView):
    model = Operation
    context_object_name = "operation"



class CategoryListView(generic.ListView):
    model = Category 
    paginate_by = 20
    context_object_name = "categories"

class CategoryDetailView(generic.DetailView):
    model = Category 
    context_object_name = "category"

class CategoryCreateView(generic.CreateView):
    model = Category
    success_url = reverse_lazy("categories") 
    fields = "__all__"
    template_name = "app/models_form.html"
