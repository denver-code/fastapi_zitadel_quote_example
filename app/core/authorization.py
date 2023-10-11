from fastapi import HTTPException, Header, Request
from app.core.validator import ValidatorError, ZitadelIntrospectTokenValidator


async def auth_required(req: Request, authorization: str = Header(None)):
    """Check if the user is authorized."""
    if authorization is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split("Bearer ")[1]
    validator = ZitadelIntrospectTokenValidator()
    validator.validate_request(req)
    _token = validator.authenticate_token(token)

    try:
        validator.validate_token(_token, _token.get("scope"), req)
        return _token
    except ValidatorError as e:
        raise HTTPException(status_code=e.status_code, detail=e.error)
