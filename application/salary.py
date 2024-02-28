#В модуле salary.py функция calculate_salary.

def calculate_salary(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = 40 * rate
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay
  
