class EmailAlreadyExistsException(Exception):

    pass

class UsernameAlreadyExistsException(Exception):

    pass

class UserAlreadyVerifiedException(Exception):

    pass

class UserNotVerifiedException(Exception):

    pass

class InvalidOTPException(Exception):

    pass

class InvalidCredentialsException(Exception):

    pass

class UserNotFoundException(Exception):

    pass

class TokenExpiredException(Exception):

    pass

class InvalidTokenException(Exception):

    pass