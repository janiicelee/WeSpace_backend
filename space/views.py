from django.views import View
from django.http import JsonResponse

from .models import Spaces, Space_Categories


class CategoryView(View):
    def get(self, request):
        try:
            category = Space_Categories.objects.values('id', 'category')

            return JsonResponse({'category': list(category)}, status=200)
        except:
            return JsonResponse({'result': 'error'}, status=400)
