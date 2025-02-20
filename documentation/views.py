from django.http import JsonResponse
from django.db.models import Q

from .models import DocumentationPage

from bs4 import BeautifulSoup


def search_documentation(request):
    query = request.GET.get("query")
    if query:
        pages = DocumentationPage.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )[0:5]
        response = {
            "query": query,
            "pages": [
                {
                    "id": page.id,
                    "title": page.title,
                    "body": get_body_overview_by_query(page.body, query),
                    "url": page.url,
                }
                for page in pages
            ],
        }
        return JsonResponse(response)
    return JsonResponse({"query": query, "pages": []})


def get_body_overview_by_query(body, query):
    body = BeautifulSoup(body).get_text(" ")
    query_index = body.lower().find(query.lower())
    if query_index == -1:
        if len(body) < 64:
            return body
        return body[:64] + "..."
    if query_index < 32:
        return body[:64] + "..."
    if query_index > len(body) - 32:
        return "..." + body[-64:]
    return "..." + body[query_index - 32 : query_index + 32] + "..."
