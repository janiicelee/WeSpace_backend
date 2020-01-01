from django.views import View
from django.http import JsonResponse

from .models import *


class CategoryView(View):
    def get(self, request):
        try:
            category = Space_Categories.objects.values('id', 'category')

            return JsonResponse({'category': list(category)}, status=200)
        except:
            return JsonResponse({'result': 'error'}, status=400)


class DetailSpaceView(View):
    def get(self, request, space_id):
        # try:
        arr = []
        space_image = Spaces.objects.prefetch_related(
            'images_set').get(id=space_id)
        space = Spaces.objects.filter(id=space_id).values(
            'title', 'short_intro', 'price', 'long_intro', 'open_time', 'close_time')
        host = Hosts.objects.filter(id=space.values()[0]['host_id'])
        for i in space_image.images_set.all().values():
            arr.append(i['space_image'])
        return JsonResponse(
            {
                'space': list(space),
                'host': list(host.values('nick_name', 'email')),
                'image': arr
            })
        # except:
        #     return JsonResponse({'result': 'error'})
