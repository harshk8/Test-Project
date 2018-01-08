from rolepermissions.roles import AbstractUserRole

class client_user(AbstractUserRole):
    available_permissions = {
        'change_password': True,
    }

class admin_user(AbstractUserRole):
    available_permissions = {
        'change_password': False,
    }