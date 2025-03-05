from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Certificate
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.db.models import Q



def search_results(request):
    query = request.GET.get('q')  # Get the search query from the URL parameter
    if query:
        # Search for certificates with matching serial_no or txId
        certificates = Certificate.objects.filter(
            Q(serial_no__icontains=query) | Q(txId__icontains=query)
        )
        if not certificates.exists():
            messages.info(request, f"No matching certificates found for '{query}'.")
    else:
        certificates = Certificate.objects.none()  # Return no results if no query is provided
        messages.warning(request, "Please enter a valid search query.")

    return render(request, 'pages/verify.html', {'certificates': certificates, 'query': query})