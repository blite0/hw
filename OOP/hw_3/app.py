import models


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
    print(recruiter)


if __name__ == '__main__':
    main()

