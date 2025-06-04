# fundoo/views.py
from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError

def health(request):
    """
    Simple health check endpoint.
    - Verifies that the default database connection can be opened.
    - Returns HTTP 200 + {"status":"ok"} on success.
    - Returns HTTP 500 + {"status":"error"} if the DB is unreachable.
    """
    db_conn = connections['default']
    try:
        # Attempt to open a cursor (this will raise if DB is down)
        c = db_conn.cursor()
    except OperationalError:
        return JsonResponse({'status': 'error', 'detail': 'database unavailable'}, status=500)
    return JsonResponse({'status': 'ok'}, status=200)
