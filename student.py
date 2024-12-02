from datetime import date, timedelta
import requests # to make a api request

class Student:
    """A student class as base for method testing"""

    def __init__(self, first_name, last_name):
        # underscore to show other developers that
        # it shale not be changed, and is read-only method
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today() # Will create time the instance was created
        self.end_date = date.today() + timedelta(days=365) # does not allow for leap years (can be improved)
        self.naughty_list = False


    @property # read-only method
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    
    @property # read-only method
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
    

    def alert_santa(self):
        self.naughty_list = True


    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)


    def course_schedule(self):
        response = requests.get(f"https://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"