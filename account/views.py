import json
import bcrypt
import jwt

from .models          import Accounts, Hosts
from account.utils    import login_decorator
from wespace.settings import SECRET_KEY

from django.views           import View
from django.http            import JsonResponse, HttpResponse
from django.db              import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class AccountsView(View):
    def _validate(self, data):
        if len(data['password']) < 6:
            return JsonResponse({'message': 'SHORT_PASSWORD'}, status=400)

        if Account.objects.filter(email = data["email"]).exists():
            return JsonResponse({'message': 'DUPLCATE_EMAIL'}, status=400)

        if Account.objects.filter(nick_name = data["nick_name"]).exists():
            return JsonResponse({'message': 'DUPLCATE_NICK'}, status=400)
                                 
        return None

    def post(self, request):
        data = json.loads(request.body)

        try:
            validation_error = self._validate(data)
            
            if validatation_error:
                return validation_error

            validate_email(data['email'])

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            Account(
                nick_name = data['nick_name'],
                email     = data['email'],
                password  = hashed_password.decode('utf-8')
            ).save()

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)
        except ValidationError:
            return JsonResponse({'message': 'NOT_AN_EMAIL'}, status=400)

class AuthView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            user = Accounts.objects.get(email=data['email'])

            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode(
                    {'id': user.id}, SECRET_KEY, algorithm='HS256')
                return JsonResponse({'access_token': access_token.decode('utf-8')}, status=200)
            else:
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)
        except Accounts.DoesNotExist:
            return JsonResponse({'message': 'INVALID_ACCOUNT'}, status=400)

## 위에랑 동일
class HostsView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if len(data['password']) < 6:
                return JsonResponse({'message': 'SHORT_PASSWORD'}, status=400)

            validate_email(data['email'])
            hashed_password = bcrypt.hashpw(
                data['password'].encode('utf-8'), bcrypt.gensalt())

            Hosts(
                nick_name=data['nick_name'],
                email=data['email'],
                password=hashed_password.decode('utf-8')
            ).save()

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

        except IntegrityError:
            return JsonResponse({'message': 'EMAIL_ALREADY_EXIST'}, status=400)

        except TypeError:
            return JsonResponse({'message': 'WRONG_INPUT_VALUE'}, status=400)

        except ValidationError:
            return JsonResponse({'message': 'NOT_AN_EMAIL'}, status=400)

class HostAuthView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if len(data['password']) < 6:
                return JsonResponse({'message': 'SHORT_PASSWORD'}, status=400)

            host = Hosts.objects.get(email=data['email'])
            if bcrypt.checkpw(data['password'].encode('utf-8'), host.password.encode('utf-8')):
                access_token = jwt.encode(
                    {'id': host.id}, SECRET_KEY, algorithm='HS256')
                return JsonResponse({'access_token': access_token.decode('utf-8')}, status=200)
            else:
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

        except Hosts.DoesNotExist:
            return JsonResponse({'message': 'INVALID_ACCOUNT'}, status=400)

        except TypeError:
            return JsonResponse({'message': 'WRONG_INPUT_VALUE'}, status=400)

        except ValidationError:
            return JsonResponse({'message': 'NOT_AN_EMAIL'}, status=400)
