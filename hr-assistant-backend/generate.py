import csv
from faker import Faker
import random

fake = Faker()

def generate_employee_data():
    emp_id = fake.uuid4()
    job_family = fake.job()
    role = fake.job()
    role_desc = fake.text(max_nb_chars=100)
    grade = random.choice(['A', 'B', 'C', 'D', 'E'])
    total_years_exp = random.randint(1, 40)
    years_exp_current_role = random.randint(1, total_years_exp)
    skills = ', '.join(fake.words(nb=random.randint(3, 10)))
    department = fake.company()
    qualifications = ', '.join([fake.job() for _ in range(random.randint(1, 3))])
    certifications = ', '.join([fake.word() for _ in range(random.randint(1, 3))])
    return [
        emp_id, job_family, role, role_desc, grade, total_years_exp,
        years_exp_current_role, skills, department, qualifications, certifications
    ]

def generate_data(num_rows):
    with open('employee_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Emp Id", "Job_family", "Role", "Role Desc", "Grade", "Total yrs exp",
            "Years of exp current role", "Skills", "Department", "Qualifications", "Certifications"
        ])
        for _ in range(num_rows):
            writer.writerow(generate_employee_data())

generate_data(1000)