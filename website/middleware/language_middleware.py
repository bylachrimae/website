from typing import Any
from django.utils.translation import activate

class LanguageMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        language = request.COOKIES.get('language')
        
        if language:
            activate(language)
        
        response = self.get_response(request)
        
        return response