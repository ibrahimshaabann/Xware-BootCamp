from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token



# Search about difference between AuthenticationFailed and Permission denied

AuthenticationFailed
class CustomAuthentication(BaseAuthentication):
     
     def get_raw_token(self, header):
        parts = header.split()
        if len(parts) == 0:
            raise AuthenticationFailed(
                ("Authorization header can't be empty"),
                code="bad_authorization_header",
            )
        if len(parts) != 2:
            raise AuthenticationFailed(
                ("Authorization header must contain two space-delimited "
                  "values"),
                code="bad_authorization_header",
            )
        return parts[1]
     
     def authenticate(self, request):
        header = request.META.get("HTTP_AUTHORIZATION")
        if header is None:
            raise AuthenticationFailed("please you must provide token")
        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise AuthenticationFailed("please you must provide token")
        token = Token.objects.filter(key=raw_token).first()
        if token is None:
            raise AuthenticationFailed("invalid token")
        return token.user, token.key
