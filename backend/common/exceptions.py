

from fastapi import HTTPException, status


class InvalidNameError(HTTPException):

    """ Raised when an invalid name is provided """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )

class InvalidTextError(HTTPException):

    """ Raised when an invalid text is provided """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )

class InvalidPasswordError(HTTPException):

    """ Raised when an invalid password is provided """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )

class Exceptions:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #### USER ####

    user_not_found_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

    user_create_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid user post data"
    )
