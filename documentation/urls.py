from django.urls import path
from .views import search_documentation

urlpatterns = [
    path("search-docs/", search_documentation, name="search_docs"),
]
