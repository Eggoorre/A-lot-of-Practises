class AirTicket:
    """
    The class of the ticket
    """
    def __init__(self, passenger_name: str, _from: str, to: str,
                 date_time: str, flight: str, seat: str,
                 _class: str, gate: str) -> None:
        """
        Initialization of ticket attributes
        """
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __str__(self) -> str:
        """
        A string representation of the ticket for output to the table
        """
        return (f"|{self.passenger_name:<16}|{self._from:<3}|{self.to:<3}|"
                f"{self.date_time:<17}| {self.flight:<19}|"
                f"{self.seat:<3}|{self._class:<3}|{self.gate:<4}|")

class Load:
    """
    A class for managing data loading
    """
    data = []

    @classmethod
    def write(cls, filename: str) -> None:
        """
        Uploads data from the file to the Air ticket list
        """
        cls.data = []
        with open(filename, 'r', encoding='utf-8') as f:
            next(f)
            for line in f:
                if line.strip():
                    params = line.strip().rstrip(';').split(';')
                    cls.data.append(AirTicket(*params))