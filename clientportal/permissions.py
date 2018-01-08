from rolepermissions.permissions import register_object_checker
from clientproject.roles import client_user, admin_user


@register_object_checker()
def access_password_link(role, user):
    if role == client_user:
        return True

    # if user.clinic == clinic:
    #     return True

    return False