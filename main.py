import datetime

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
  print("Сегодняшняя дата:", datetime.date.today())
  print("Сотрудники:")
  get_employees()
  print("Зарплата сотрудников:")
  print(calculate_salary(40, 10))

  