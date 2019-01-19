from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.conf import settings
from .models import Project


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def project_list_view(request):
    projects = get_list_or_404(Project)
    paginator = Paginator(projects, 10)

    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects,
    }

    return render(request, 'projects/project_list.html', context)


def project_detail_view(request, pk):
    context = {
        'projects': get_object_or_404(Project, pk=pk)
    }

    return render(request, 'projects/project_detail.html', context)
