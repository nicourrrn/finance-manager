from django.urls import path
from .views import (OperationListView, CategoryListView,
                    CategoryCreateView, OperationCreateView,
                    IndexPageView, CounterView)

urlpatterns = [
    path("", IndexPageView.as_view(), name="index" ),
    path("counter", CounterView.as_view(), name="counter"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("categories/create", CategoryCreateView.as_view(), name="create_category"),
    path("operations/", OperationListView.as_view(), name="operations"),
    path("operations/create", OperationCreateView.as_view(), name="create_operation"),
]
