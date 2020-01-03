import json

from django.views import View
from django.http import JsonResponse

from .models import Spaces, Space_Categories, Images
from account.models import Hosts, Reservations
from account.utils import host_decorator


class CategoryView(View):
    def get(self, request):
        try:
            categories = list(
                Space_Categories.objects.values('id', 'category'))
            return JsonResponse({'Categority': categories}, status=200)
        except:
            return JsonResponse({'result': 'ERROR'}, status=400)


class RecommendView(View):
    def get(self, request):
        spaces = list(Spaces.objects.all())[:5]
        recommend = [{
            'title': space.title,
            'price': space.price,
            'location': space.location,
            'image': list(space.images_set.filter(space_id=space.id).values('space_image'))
        } for space in spaces]

        return JsonResponse({'data': recommend}, status=200)


class EditorView(View):
    def get(self, request):
        spaces = list(Spaces.objects.all())
        editor = [{
            'image': list(space.images_set.filter(space_id=space.id).values('space_image')),
            'tag': list(space.tags_set.filter(space_id=space.id).values('tag')),
            'title': space.title,
            'price': space.price,
            'long_intro': space.long_intro
        } for space in spaces]

        return JsonResponse({'data': editor}, status=200)


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


class Registration(View):
    @host_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            Spaces(
                title=data['title'],
                short_intro=data['short_intro'],
                long_intro=data['long_intro'],
                price=data['price'],
                location=data['location'],
                host_id=request.host.id,
                min_time=data['min_time'],
                min_guest=data['min_guest'],
                open_time=data['open_time'],
                close_time=data['close_time']
            ).save()

            return JsonResponse({'result': 'insert success'}, status=200)
        except KeyError:
            return JsonResponse({'result': 'incorrect key'}, status=400)
        except ValueError:
            return JsonResponse({'result': 'value Error'}, status=400)
        except Hosts.DoesNotExist:
            return JsonResponse({'result': 'does not exist host'}, status=400)
