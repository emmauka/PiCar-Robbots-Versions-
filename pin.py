class Pin:
    def __init__(self, pin):
        self._dict = {
            'P0': 0,  # Replace with actual pin mapping from your documentation
            'P1': 1,
            'P2': 2,
            'P3': 3,
            'P4': 4,
            'P5': 5,
            'P6': 6,
            'P7': 7,
            'P8': 8,
            'P9': 9
            # Add more pin mappings as necessary
        }
        if isinstance(pin, str):
            try:
                self._pin = self._dict[pin]
            except KeyError:
                raise ValueError(f"Invalid pin identifier: {pin}. Available pins: {list(self._dict.keys())}")
        elif isinstance(pin, int):
            self._pin = pin
        else:
            raise TypeError("Pin identifier must be a string or integer.")

    def dict(self):
        return self._dict

    def get_pin(self):
        return self._pin
