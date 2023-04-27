class OrdersInfoException(Exception):
    ...


class OrdersInfoNotFoundError(OrdersInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "orders Info Not Found"


class OrdersInfoInfoAlreadyExistError(OrdersInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "orders Info Already Exists"