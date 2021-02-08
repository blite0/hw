class Employee(object):
    def __init__(self, name, email, salary_one_day):
        self.name = name
        self.email = email
        self.salary_one_day = salary_one_day

    def work(self):
        print("I come to the office.")

    def check_salary(self, day):
        x = self.salary_one_day * day
        return x


class Recruiter(Employee):
    def work(self):
        super().work()
        return 'I come to the office and start to hiring.'

    def __str__(self):
        return 'Должность: {}, Имя: {}'.format(self.__class__.__name__, self.name)


class Programmer(Employee):
    def work(self):
        super().work()
        return 'I come to the office and start to coding.'

    def __str__(self):
        return 'Должность: {}, Имя: {}'.format(self.__class__.__name__, self.name)





class Candidate (object):
    def __init__(self,full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy(object):
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level


Grisha = Programmer("grisha", "grishager@gmail.com", 50)

print(Grisha)
print(Grisha.work())
print(Grisha.check_salary(20))
