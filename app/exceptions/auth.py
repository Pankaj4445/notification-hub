from fastapi import HTTPException, status

class EmailAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = "This email address is already registered."):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=detail
        )

class UsernameAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = "This username is already taken."):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=detail
        )

class UserAlreadyVerifiedException(HTTPException):
    def __init__(self, detail: str = "This user account is already verified."):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=detail
        )

class UserNotVerifiedException(HTTPException):
    def __init__(self, detail: str = "Please verify your account before logging in."):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail=detail
        )

class InvalidOTPException(HTTPException):
    def __init__(self, detail: str = "The OTP provided is incorrect or has expired."):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=detail
        )

class InvalidCredentialsException(HTTPException):
    def __init__(self, detail: str = "Incorrect email or password."):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )

class UserNotFoundException(HTTPException):
    def __init__(self, detail: str = "Invalid credentials"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=detail
        )

class TokenExpiredException(HTTPException):
    def __init__(self, detail: str = "Your session token has expired. Please log in again."):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=detail
        )

class InvalidTokenException(HTTPException):
    def __init__(self, detail: str = "The authentication token is invalid or malformed."):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=detail
        )
class UserInactiveException(HTTPException):
    def __init__(
        self,
        detail: str = "This account has been deactivated."
    ):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )

class PermissionDeniedException(HTTPException):
    def __init__(
            self,
            detail:str= "403 forbidden"
    ):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )


class PasswordReuseException(HTTPException):
    def __init__(self, detail:str = "400 Bad Request"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)