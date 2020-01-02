from django.views import View
from django.http import JsonResponse

from .models        import Spaces, Space_Categories, Images
from account.models import Hosts


class CategoryView(View):
    def get(self, request):
        try:
            categories = list(Space_Categories.objects.values('id','category'))
            return JsonResponse({'Categority':categories}, status=200)
        except:
            return JsonResponse({'result':'ERROR'}, status =400)

class RecommendView(View):
    def get(self, request):
        spaces = list(Spaces.objects.all())[:5]
        recommend = [{
            'title'    : space.title,
            'price'    : space.price,
            'location' : space.location,
            'image'    : list(space.images_set.filter(space_id = space.id).values('space_image'))
        } for space in spaces]
           
        return JsonResponse({'data':recommend}, status =200)

class EditorView(View):
    def get(self, request):
        spaces = list(Spaces.objects.all())
        editor = [{
           'image'       : list(space.images_set.filter(space_id = space.id).values('space_image')),
            'tag'        : list(space.tags_set.filter(space_id = space.id).values('tag')),
            'title'      : space.title,
            'price'      : space.price,
            'long_intro' : space.long_intro
            } for space in spaces]
        
        return JsonResponse({'data':editor}, status = 200)


