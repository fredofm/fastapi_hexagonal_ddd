from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer

from jwt import PyJWKClient
import jwt

from rhh.shared.logger import RHHLogger

logger = RHHLogger().get_logger(__name__)

oauth_2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="http://localhost:8080/realms/rhh/protocol/openid-connect/token",
    authorizationUrl="http://localhost:8080/realms/rhh/protocol/openid-connect/auth",
    refreshUrl="http://localhost:8080/realms/rhh/openid-connect/token",
)


async def valid_access_token(
    access_token: Annotated[str, Depends(oauth_2_scheme)]
):
    url = "http://localhost:8080/realms/rhh/protocol/openid-connect/certs"
    optional_custom_headers = {"User-agent": "custom-user-agent"}
    jwks_client = PyJWKClient(url, headers=optional_custom_headers)
    
    logger.debug(f"Access token: {access_token}")

    try:
        signing_key = jwks_client.get_signing_key_from_jwt(access_token)
        logger.debug(f"Signing key: {signing_key}")
        
        data = jwt.decode(
            access_token,
            signing_key.key,
            algorithms=["RS256"],
            audience="account",
            options={"verify_aud": False, "verify_exp": True},
        )
        
        logger.debug(f"Token data: {data}")
        
        return data
    except jwt.exceptions.InvalidTokenError as e:
        logger.error(f"Invalid token error: {e}")
        raise HTTPException(status_code=401, detail=f"Not authenticated: {e}")
    
def has_role(role_name: str):
    async def check_role(
        token_data: Annotated[dict, Depends(valid_access_token)]
    ):
        roles = token_data["realm_access"]["roles"]
        if role_name not in roles:
            raise HTTPException(status_code=403, detail=f"Role {roles} not allowed")

    return check_role
