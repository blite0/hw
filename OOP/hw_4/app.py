import models
from datetime import datetime
import traceback
import sys


def main():
    recruiter = models.Recruiter('Sam', 'Serioussam', 150)
    programmer_phyton = models.Programmer('Hitman', 'hitmanovich@gmail.com', 200)
    programmer_java = models.Programmer('Putin', 'putinvv@gmail.com', 1)
    candidate_phyton = models.Candidate('Eric Davidovich', 'ericdavidovich@gmail.com', 'programming',
                                        'phyton', 'junior')
    candidate_phyton2 = models.Candidate('Vladimir Zelencskiy', 'vladimirgreen@gmail.com', 'phyton',
                                         'programming', 'senior')
    candidate_phyton3 = models.Candidate('Petr Poroshenko', 'roshen@gmail.com', 'phyton',
                                         'programming', 'junior')
    vacancy_first = models.Vacancy("Phyton", 'django', 'senior')
    vacancy_second = models.Vacancy("Phyton", 'django', 'junior')
    print(f'{recruiter}\n{programmer_phyton}\n{programmer_java}\n{candidate_phyton}'
          f'\n{candidate_phyton2}\n{candidate_phyton3}\n{vacancy_first}\n{vacancy_second}')


logs = open("logs.py", 'a')
date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
try:
    models.candidate_phyton()
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    logs.write(f"date: time: {date_time}, exception type: {exc_type.__name__}, "
               f"full traceback: {repr(traceback.format_tb(exc_traceback))}\n")
logs.close()