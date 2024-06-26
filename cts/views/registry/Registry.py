from rest_framework.views import APIView
from django.http import JsonResponse
from ...registrycontenthelpers import find_registry

class Registry(APIView):
    
    allowed_methods = ['GET']

    def get(self, request, *args, **kwargs):
        
        category = kwargs.get('category', '')
        if not category:
            return JsonResponse(data=None, safe=False)
        
        include_identities = request.query_params.get('include_identities', '')
        include_identities = True if include_identities and include_identities.lower() == 'true' else False
        registry = find_registry(category, include_identities=include_identities)
                
        return JsonResponse(data=registry, safe=False)
