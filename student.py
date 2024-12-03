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
        # Checks leap year
        if self._start_date.day != self.end_date.day: # Compares start day end day, adds 1 day if they are not equal
            self.end_date += timedelta(days=1)
        self.naughty_list = False
        self.extension = False


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


    def show_start_date(self):
        print(self._start_date)
        return self._start_date
    

    def show_end_date(self):
        print(self.end_date)
        return self.end_date

    
    def check_days_left(self):
        days_left = (self.end_date - self._start_date).days
        print(days_left)
        return days_left

