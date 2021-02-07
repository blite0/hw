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


Grisha = Programmer("grisha", "grishager@gmail.com", 50)
print(Grisha)
print(Grisha.work())
print(Grisha.check_salary(20))