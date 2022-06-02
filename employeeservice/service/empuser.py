from django.contrib.auth.models import User


def create_user(code):
    try:
        user = User.objects.create_user(username=code, password=code)
        msg={"user_id":user.id,"status":True}

    except:
        msg ={"user_id":None,"status":False}

    return msg
