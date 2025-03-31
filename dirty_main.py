from application.salary import *
from application.db.people import *
from datetime import datetime

if __name__ == '__main__':
    print(f"Дата запуска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    calculate_salary()
    get_employees()
    