import jwt
import json
from django.http import JsonResponse
from .models import Accounts
from wespace.settings import SECRET_KEY



def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        if "Authorization" not in request.headers:
            return JsonResponse({"error_code":"INVALID_LOGIN"}, status=401)

        encode_token = request.headers["Authorization"]
        print(encode_token)

        try:
            data = jwt.decode(encode_token, SECRET_KEY, algorithm='HS256')
            print(data)
            account = Accounts.objects.get(id=data['id'])
            print(account)
            request.account = account
            print(request.account)
        except jwt.DecodeError:
            return JsonResponse({"error_code":"INVALID_TOKEN"}, status = 401)
        except Accounts.DoesNotExist:
            return JsonResponse({"error_code":"UNKNOWN_USER"}, status = 401)
        return func(self, request, *args, **kwargs)
    return wrapper 
