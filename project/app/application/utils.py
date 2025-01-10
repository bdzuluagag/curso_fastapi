from fastapi import HTTPException, status, Depends
from typing import Optional
import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, SecurityScopes
import jwt.exceptions
from application.config import get_settings

class UnauthorizdException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)



class UnauthenticatedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication")


class VerifyToken:
    """does all the token verification using the auth0 configuration"""

    def __init__(self):
        self.config = get_settings()

        jwks_url = f'https://{self.config.auth0_domain}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    async def verify(self, 
                    security_scopes: SecurityScopes,
                    token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())
                    ):
        if not token:
            raise UnauthenticatedException()
        
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token.credentials).key
        
        except jwt.exceptions.PyJWKClientError as error:
            raise UnauthorizdException(str(error))
        
        except jwt.exceptions.DecodeError as error:
            raise UnauthorizdException(str(error))
        
        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=self.config.auth0_algorithms,
                audience=self.config.auth0_api_audience,
                issuer=self.config.auth0_issuer
            )

        except Exception as error:
            raise UnauthorizdException(str(error))
        
        return payload