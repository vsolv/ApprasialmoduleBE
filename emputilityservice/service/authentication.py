import rest_framework
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from rest_framework import authentication, exceptions
from rest_framework.authtoken.models import Token
from knox.auth import AuthToken,TokenAuthentication

# from userservice.models import Employee


class EmployeeAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = None
        user = None

        # return (user, None)
        try:
            token = request.META['HTTP_AUTHORIZATION']
            token_arr = token.split()
            if not token_arr[0] == 'Token':
                raise exceptions.AuthenticationFailed(('No credentials provided.'))
            token = token_arr[1]
            print(token)
            # pass
            # token = request.session['token']
            # print(token)
            # tok = TokenAuthentication()
            # token.encode("utf-8")
            # tstr = token.encode("utf-8")
            # token_obj = tok.authenticate_credentials(tstr)
            # user = token_obj[0]
            # token = 'cbd6a7926a1788ed7585f48df93bae48ae33dc0ab5b1c63c2215a61ea3fac505'
            # token = request.session['token']
            # print(token)
            # token_obj = Token.objects.get(key=token)
            # user = User.objects.get(id=token_obj.user_id)
            # print("vsy", user.id)
        except KeyError:
            try:
                token = request.META['HTTP_AUTHORIZATION']
                token_arr = token.split()
                if not token_arr[0] == 'Token':
                    raise exceptions.AuthenticationFailed(('No credentials provided.'))
                token = token_arr[1]
                #token_obj = Token.objects.get(key=token)
                tok = TokenAuthentication()
                token.encode("utf-8")
                tstr = token.encode("utf-8")
                token_obj = tok.authenticate_credentials(tstr)
                user = token_obj[0]
                #user = User.objects.get(id=token_obj.user_id)
                # employee = Employee.objects.get(user_id=token_obj.user_id)
                # print(employee)

                # request.user.employee = employee
            except rest_framework.authtoken.models.Token.DoesNotExist:
                raise exceptions.AuthenticationFailed(('Invalid token.'))
            except:
                user = None

        if token is not None:
            #token = request.session['token']
            print(token)
            tok = TokenAuthentication()
            token.encode("utf-8")
            tstr = token.encode("utf-8")
            token_obj = tok.authenticate_credentials(tstr)
            user = token_obj[0]

        else:
            user = None

        if user is None:
            token = request.GET.get('token', None)
            if token is not  None :
                tok = TokenAuthentication()
                token.encode("utf-8")
                tstr = token.encode("utf-8")
                token_obj = tok.authenticate_credentials(tstr)
                user = token_obj[0]

        return (user, None)
        # username = request.data.get('username', None)
        # password = request.data.get('password', None)
        # if not username or not password:
        #     raise exceptions.AuthenticationFailed(('No credentials provided.'))
        #
        # credentials = {
        #     get_user_model().USERNAME_FIELD: username,
        #     'password': password
        # }
        #
        # user = authenticate(**credentials)
        #
        # if user is None:
        #     raise exceptions.AuthenticationFailed(('Invalid username/password.'))
        #
        # if not user.is_active:
        #     raise exceptions.AuthenticationFailed(('User inactive or deleted.'))
        # user = User.objects.get(username='allformani')
        # return (user, None)
