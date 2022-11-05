from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import datetime
import demoqa_tests


class Gender(Enum):
    Male = 1
    Female = 2
    Other = 3

class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'

class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Physics'

def format_input_date(date: datetime.date):
    return date.strftime(demoqa_tests.config.datetime_input_format)

@dataclass
class User:
    gender: Gender
    firstname: str
    birthday: datetime.date(1993, 7, 24)
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    subjects: Tuple[Subject] = (Subject.Maths, Subject.History)
    lastname: str = 'alansi'
    picture: str = 'minion.png'
    address: str = 'Tbilisi'
    state: str = 'NCR'
    city: str = 'Delhi'
    email: str = 'nalansi@yahoo.com'
    mobile: str = '0123456789'

sample_female_student = User(firstname='natalya', gender=Gender.Female, birthday=datetime.date(1993, 7, 24))