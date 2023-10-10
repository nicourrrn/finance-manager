from django.urls import path
from .views import (CategoryDetailView, OperationDetailView,
                    OperationListView, CategoryListView,
                    CategoryCreateView,
                    IndexPageView)

urlpatterns = [
    path("", IndexPageView.as_view(), name="index" ),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("categories/create", CategoryCreateView.as_view(), name="create_category"),
    path("categories/<int:pk>", CategoryDetailView.as_view(), name="category"),
    path("operations/", OperationListView.as_view(), name="operations"),
    path("operations/<int:pk>", OperationDetailView.as_view(), name="operation"),
]
