import json
import bcrypt

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models                import Accounts

class AccountsView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if len(data['password']) < 6 :
                return JsonResponse({'message':'TOO_SHORT'}, status = 400)
            validate_email(data['email'])
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
            
            Accounts(
                    nick_name = data['nick_name'],
                    email     = data['email'],
                    password  = data['password']
                    ).save()
            return JsonResponse({'message':'SUCCESS'}, status = 200)
        
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)

        except IntegrityError:
            return JsonResponse({'message':'EMAIL_ALREADY_EXIST'},status = 400)
        
        except TypeError:
            return JsonResponse({'message':'WRONG_INPUT_VALUE'}, status = 400)
        except ValidationError:
            return JsonResponse({'message':'NOT_AN_EMAIL'}, status = 400)

        
