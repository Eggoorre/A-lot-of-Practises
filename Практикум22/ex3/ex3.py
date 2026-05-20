class Date:
    """Auxiliary class for working with dates."""

    def __init__(self, date_str: str):
        self.date_str = date_str

    def __str__(self) -> str:
        day, month, year = self.date_str.split('.')

        months = {
            '01': 'янв', '02': 'фев', '03': 'мар', '04': 'апр',
            '05': 'май', '06': 'июн', '07': 'июл', '08': 'авг',
            '09': 'сен', '10': 'окт', '11': 'ноя', '12': 'дек'
        }

        return f"{int(day)} {months[month]} {year} г."


class User:
    """Employee class."""

    def __init__(
        self,
        id: str,
        nick_name: str,
        first_name: str,
        last_name: str,
        middle_name: str,
        gender: str
    ):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __str__(self) -> str:
        name_parts = [self.first_name]

        if self.last_name:
            name_parts.append(self.last_name)

        if self.middle_name:
            name_parts.append(self.middle_name)

        full_name = " ".join(name_parts)

        return (
            f"ID: {self.id} LOGIN: {self.nick_name} "
            f"NAME: {full_name} GENDER: {self.gender}"
        )


class Meeting:
    """Work meeting class."""

    lst_meeting = []

    def __init__(self, id: str, date: Date, title: str):
        self.id = id
        self.date = date
        self.title = title
        self.employees = []

    def add_person(self, person: User) -> None:
        """Add an employee to the meeting."""
        self.employees.append(person)

    def count(self) -> int:
        """Return the number of employees in the meeting."""
        return len(self.employees)

    @classmethod
    def count_meeting(cls, date: Date) -> int:
        """Return the number of meetings on the specified date."""
        return sum(
            1
            for meeting in cls.lst_meeting
            if meeting.date.date_str == date.date_str
        )

    @classmethod
    def total(cls) -> int:
        """Return the total number of employees for all meetings."""
        return sum(meeting.count() for meeting in cls.lst_meeting)

    def __str__(self) -> str:
        result = [
            f"Рабочая встреча {self.id}",
            f"{self.date} {self.title}"
        ]

        for employee in self.employees:
            result.append(str(employee))

        return "\n".join(result)


class Load:
    """Class for loading data from files."""

    @staticmethod
    def write(
        meetings_file: str,
        persons_file: str,
        pers_meetings_file: str
    ) -> None:
        """Load data from files."""
        Meeting.lst_meeting = []

        users = {}
        meetings = {}

        with open(persons_file, "r", encoding="utf-8") as file:
            next(file)

            for line in file:
                params = line.strip().split(";")

                if params[-1] == "":
                    params = params[:-1]

                if len(params) == 6:
                    users[params[0]] = User(*params)

        with open(meetings_file, "r", encoding="utf-8") as file:
            next(file)

            for line in file:
                params = line.strip().split(";")

                if params[-1] == "":
                    params = params[:-1]

                if len(params) == 3:
                    meeting = Meeting(
                        params[0],
                        Date(params[1]),
                        params[2]
                    )

                    meetings[params[0]] = meeting
                    Meeting.lst_meeting.append(meeting)

        with open(pers_meetings_file, "r", encoding="utf-8") as file:
            next(file)

            for line in file:
                params = line.strip().split(";")

                if params[-1] == "":
                    params = params[:-1]

                if len(params) >= 2:
                    meeting_id = params[0]
                    user_id = params[1]

                    if meeting_id in meetings and user_id in users:
                        meetings[meeting_id].add_person(users[user_id])