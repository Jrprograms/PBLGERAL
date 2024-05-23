# myapp/middleware.py
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Aqui você pode inspecionar o conteúdo da requisição
        logger.info(f'Method: {request.method}')
        logger.info(f'Path: {request.path}')
        logger.info(f'Headers: {request.headers}')
        logger.info(f'Body: {request.body.decode("utf-8")}')

        response = self.get_response(request)
        return response
