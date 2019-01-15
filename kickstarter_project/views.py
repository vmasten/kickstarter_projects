from django.shortcuts import render


def home_view(request):
    """Render the home view."""
    return render(request, 'generic/home.html', {'message': 'hello'})
