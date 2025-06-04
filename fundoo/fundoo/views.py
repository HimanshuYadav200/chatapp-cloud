from django.http import JsonResponse, HttpResponse
from django.db import connections
from django.db.utils import OperationalError

# Basic home endpoint

def index(request):
    """
    Basic home endpoint used by urls.py.
    """
    return HttpResponse("Hello from Fundoo!", status=200)

# Health check endpoint

def health(request):
    """
    Simple health check endpoint:
    - Verifies that the default database connection can be opened.
    - Returns HTTP 200 + {"status":"ok"} on success.
    - Returns HTTP 500 + {"status":"error"} if the DB is unreachable.
    """
    try:
        connections['default'].cursor()
    except OperationalError:
        return JsonResponse({'status': 'error', 'detail': 'database unavailable'}, status=500)
    return JsonResponse({'status': 'ok'}, status=200)

# Signup endpoint stub

def Signup(request):
    """
    User signup endpoint stub.
    Replace this with actual signup logic.
    """
    return JsonResponse({'status': 'success', 'message': 'Signup endpoint reached'}, status=200)
