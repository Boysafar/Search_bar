from django.shortcuts import render
from .models import Post


def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(title__icontains=query)

    return render(request, 'search_results.html', {'results': results, 'query': query})
