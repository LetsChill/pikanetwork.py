class InvalidName(ValueError):
    """Raised when the name given is invalid"""
    pass


class PlayerNotFound(Exception):
    pass


class PlayerWithNoClan(Exception):
    pass
