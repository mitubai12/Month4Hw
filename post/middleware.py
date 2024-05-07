import time
from django.utils.timezone import now
import logging

# Получаем настроенный логгер
logger = logging.getLogger('django')

class PerformanceMonitoringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        logger.info(f"Request to {request.path} took {duration:.6f} seconds")
        return response