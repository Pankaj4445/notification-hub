import re

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

def hash_password(password: str) -> str:
    """
    Convert plain text password into a secure hash.
    """
    return pwd_context.hash(password)

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Compare a plain password with its stored hash.
    """
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def validate_password_strength(
    password: str
) -> None:
    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters."
        )
    if not re.search(r"[A-Z]", password):
        raise ValueError(
            "Password must contain an uppercase letter."
        )
    if not re.search(r"[a-z]", password):
        raise ValueError(
            "Password must contain a lowercase letter."
        )
    if not re.search(r"\d", password):
        raise ValueError(
            "Password must contain a number."
        )
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValueError(
            "Password must contain any of [!@#$%^&*(),.?\":{}|<>] this special character."
        )