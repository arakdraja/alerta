from flask import Blueprint, request

from alerta.exceptions import ApiError

auth = Blueprint('auth', __name__) 


try:
    import ldap
    from . import basic_ldap
except ImportError:
    from . import basic

from . import github, gitlab, google, keycloak, pingfederate, saml2, userinfo

@auth.before_request
def only_json():
    if request.method in ['POST', 'PUT'] and not request.is_json:
        raise ApiError("POST and PUT requests must set 'Content-type' to 'application/json'", 415)
