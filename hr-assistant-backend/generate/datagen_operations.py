import random
import json
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define metadata
job_families = ['Operations']
grades = ['L1', 'L2', 'L3', 'AVP', 'VP', 'Director', 'Executive Director', 'Managing Director']
roles = [
    'Operations Coordinator', 'Loan Operations Specialist', 'Banking Operations Analyst', 'Account Services Coordinator', 
    'Risk Operations Manager', 'Fraud Prevention Specialist', 'Operations Manager', 'Branch Operations Manager', 
    'Trade Operations Manager', 'Risk and Compliance Manager', 'Senior Operations Manager', 'Business Operations Manager', 
    'Head of Operations', 'VP of Operations', 'Director of Banking Operations', 'Chief Operating Officer', 
    'Operations Director', 'Treasury Operations Manager', 'Client Services Manager', 'Business Continuity Manager'
]
role_grade_mapping = {
    'L1': ['Operations Coordinator', 'Loan Operations Specialist', 'Account Services Coordinator'],
    'L2': ['Banking Operations Analyst', 'Fraud Prevention Specialist', 'Risk Operations Manager'],
    'L3': ['Operations Manager', 'Branch Operations Manager', 'Trade Operations Manager'],
    'AVP': ['Senior Operations Manager', 'Business Operations Manager'],
    'VP': ['Head of Operations', 'VP of Operations'],
    'Director': ['Director of Banking Operations', 'Operations Director'],
    'Executive Director': ['Executive Director of Operations'],
    'Managing Director': ['Chief Operating Officer']
}
departments = [
    'Operations', 'Retail Banking Operations', 'Corporate Banking Operations', 'Trade Operations', 'Risk Management', 
    'Compliance', 'Fraud Prevention', 'Treasury', 'Customer Service', 'Business Continuity', 'Client Services', 
    'Financial Crime Prevention', 'Settlement Services'
]
qualifications = ['Bachelors', 'Masters', 'MBA', 'Finance', 'Accounting', 'Economics']
employment_types = ['Full-time', 'Part-time', 'Contract']
skills_list = [
    'Banking Operations', 'Risk Management', 'Compliance', 'Fraud Prevention', 'Loan Servicing', 'Client Onboarding', 
    'Treasury Operations', 'Settlements', 'KYC (Know Your Customer)', 'AML (Anti-Money Laundering)', 'Financial Crime Prevention', 
    'Cash Management', 'Transaction Monitoring', 'Customer Service', 'Business Continuity Planning', 'Financial Analysis'
]
certifications = [
    "Certified Anti-Money Laundering Specialist (CAMS)", "Certified Fraud Examiner (CFE)", "Certified Operations Professional (COP)", 
    "Project Management Professional (PMP)", "Certified Banking Operations Specialist (CBOS)", "Financial Risk Manager (FRM)", 
    "Certified Treasury Professional (CTP)", "Certified Bank Auditor (CBA)", "Certified Financial Services Auditor (CFSA)", 
    "Certified Compliance and Ethics Professional (CCEP)", "Chartered Financial Analyst (CFA)", "Certified Risk Management Professional (CRMP)"
]
skill_certifications_mapping = {
    'Banking Operations': ["Certified Banking Operations Specialist (CBOS)", "Certified Operations Professional (COP)"],
    'Risk Management': ["Certified Risk Management Professional (CRMP)", "Financial Risk Manager (FRM)"],
    'Compliance': ["Certified Compliance and Ethics Professional (CCEP)", "Certified Bank Auditor (CBA)"],
    'Fraud Prevention': ["Certified Fraud Examiner (CFE)", "Certified Anti-Money Laundering Specialist (CAMS)"],
    'Loan Servicing': ["Certified Banking Operations Specialist (CBOS)", "Certified Risk Management Professional (CRMP)"],
    'Client Onboarding': ["Certified Banking Operations Specialist (CBOS)", "Certified Anti-Money Laundering Specialist (CAMS)"],
    'Treasury Operations': ["Certified Treasury Professional (CTP)", "Certified Bank Auditor (CBA)"],
    'Settlements': ["Certified Banking Operations Specialist (CBOS)", "Certified Risk Management Professional (CRMP)"],
    'KYC (Know Your Customer)': ["Certified Anti-Money Laundering Specialist (CAMS)", "Certified Fraud Examiner (CFE)"],
    'AML (Anti-Money Laundering)': ["Certified Anti-Money Laundering Specialist (CAMS)", "Certified Fraud Examiner (CFE)"],
    'Financial Crime Prevention': ["Certified Anti-Money Laundering Specialist (CAMS)", "Certified Fraud Examiner (CFE)"],
    'Cash Management': ["Certified Treasury Professional (CTP)", "Certified Risk Management Professional (CRMP)"],
    'Transaction Monitoring': ["Certified Anti-Money Laundering Specialist (CAMS)", "Certified Risk Management Professional (CRMP)"],
    'Customer Service': ["Certified Customer Service Professional (CCSP)", "Certified Banking Operations Specialist (CBOS)"],
    'Business Continuity Planning': ["Certified Business Continuity Professional (CBCP)", "ISO 22301:2012 Lead Implementer"],
    'Financial Analysis': ["Chartered Financial Analyst (CFA)", "Certified Financial Services Auditor (CFSA)"]
}
region = ['APAC', 'EMEA', 'AMER', 'GLOBAL']

# Function to generate total experience based on grade
def generate_experience(grade):
    if grade == 'L1':
        return random.randint(1, 5)
    elif grade == 'L2':
        return random.randint(3, 7)
    elif grade == 'L3':
        return random.randint(5, 10)
    elif grade == 'AVP':
        return random.randint(8, 15)
    elif grade == 'VP':
        return random.randint(10, 20)
    elif grade == 'Director' or grade == 'Executive Director':
        return random.randint(15, 25)
    elif grade == 'Managing Director':
        return random.randint(15, 35)
    else:
        return random.randint(1, 35)

# Function to generate employee data
def generate_employee(emp_id):
    grade = random.choice(grades)
    role = random.choice(role_grade_mapping[grade])
    department = random.choice(departments)
    skill = random.choice(skills_list)
    cert = random.choice(skill_certifications_mapping.get(skill, [])) if skill in skill_certifications_mapping else " "
    country = fake.country()
    region_choice = random.choice(region)
    compensation_range = {
        'L1': (30000, 80000),
        'L2': (50000, 100000),
        'L3': (80000, 150000),
        'AVP': (120000, 250000),
        'VP': (200000, 500000),
        'Director': (400000, 800000),
        'Executive Director': (600000, 1000000),
        'Managing Director': (800000, 1500000)
    }.get(grade)
    compensation = random.randint(compensation_range[0], compensation_range[1])
    total_exp = generate_experience(grade)
    exp_current_role = random.randint(1, total_exp)
    qualifications_choice = random.choice(qualifications)
    
    return {
        "EMP_ID": emp_id,
        "FIRST_NAME": fake.first_name(),
        "LAST_NAME": fake.last_name(),
        "GENDER": random.choice(['Male', 'Female']),
        "EMAIL": fake.email(),
        "GRADE": grade,
        "JOB_FAMILY": 'Operations',
        "ROLE": role,
        "ROLE_DESCRIPTION": fake.sentence(nb_words=6),
        "TOTAL_EXP": total_exp,
        "EXP_CURRENT_ROLE": exp_current_role,
        "SKILLS": skill,
        "DEPARTMENT": department,
        "QUALIFICATION": qualifications_choice,
        "CERTIFICATIONS": cert,
        "COMPENSATION": compensation,
        "COUNTRY": country,
        "REGION": region_choice,
        "EMPLOYMENT_TYPE": random.choice(['Full-time', 'Part-time', 'Contract'])
    }

# Generate 2000 employee records
employees = [generate_employee(4001 + i) for i in range(2000)]

# Write to JSON file
with open('synthetic_data_operations.json', 'w') as f:
    json.dump(employees, f, indent=4)

print("Employee data generated successfully!")
