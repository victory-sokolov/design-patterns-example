
class Order:

    def __init__(self, shipper) -> None:
        self._shipper = shipper

    @property
    def shipper(self):
        return self._shiper