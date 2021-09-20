class EmptyPathError(Exception):
    def __str__(self) -> str:
        return 'The path must not be an empty value.'


class PathNotFoundError(Exception):
    def __init__(self, path) -> None:
        self.path = path
        super().__init__(self.path)

    def __str__(self) -> str:
        return f'The path: {self.path} does not exists.'


class EmptyColor(Exception):
    pass


class WrongTypeError(Exception):
    def __init__(self, expected, given) -> None:
        self.expected = expected
        self.given = given
        super().__init__(self.expected, self.given)

    def __str__(self) -> str:
        return f'Expected {self.expected} but {self.given} is given.'


class EmptyImage(Exception):
    pass


class EmptySizesError(Exception):
    pass


class ImposibleSizeError(Exception):
    pass
