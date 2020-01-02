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
        space = [
            {
                'id': space.id,
                'title': space.title,
                'short_intro': space.short_intro,
                'long_intro': space.long_intro,
                'price': space.price,
                'location': space.location,
                'open_time': space.open_time,
                'close_time': space.close_time,
                'min_guest': space.min_guest,
                'min_time': space.min_time,
                'space_images': list(space.images_set.values_list('space_image', flat=True)),
                'host': list(Hosts.objects.filter(id=space.host_id).values('id', 'nick_name', 'email', 'phonenumber')),
                'tag': list(space.tags_set.values_list('tag', flat=True)),
                'notice': list(space.notices_set.values_list('notice', flat=True))
            }
            for space in Spaces.objects.filter(id=space_id)]
        return JsonResponse({'result': space}, status=200)
