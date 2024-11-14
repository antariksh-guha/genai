import json
import random
from faker import Faker

fake = Faker()

# Metadata Arrays
job_families = ['Risk Management']

grades = ['L1', 'L2', 'L3', 'AVP', 'VP', 'Director', 'Executive Director', 'Managing Director']

roles = [
    'Risk Analyst', 'Risk Operations Coordinator', 'Credit Risk Analyst', 'Market Risk Analyst',
    'Operational Risk Analyst', 'Risk Management Specialist', 'Compliance Officer', 'Risk Manager',
    'Risk and Compliance Analyst', 'Senior Risk Analyst', 'Risk and Compliance Manager',
    'Senior Risk Manager', 'Head of Risk', 'VP of Risk Management', 'Director of Risk Management',
    'Chief Risk Officer', 'Operational Risk Director', 'Enterprise Risk Manager', 'Head of Compliance'
]

role_grade_mapping = {
    'L1': ['Risk Analyst', 'Risk Operations Coordinator', 'Credit Risk Analyst'],
    'L2': ['Market Risk Analyst', 'Operational Risk Analyst', 'Risk Management Specialist'],
    'L3': ['Risk Manager', 'Risk and Compliance Analyst', 'Senior Risk Analyst'],
    'AVP': ['Risk and Compliance Manager', 'Senior Risk Manager'],
    'VP': ['Head of Risk', 'VP of Risk Management'],
    'Director': ['Director of Risk Management', 'Operational Risk Director'],
    'Executive Director': ['Chief Risk Officer'],
    'Managing Director': ['Chief Risk Officer']
}

departments = [
    'Risk Management', 'Credit Risk', 'Market Risk', 'Operational Risk', 'Enterprise Risk',
    'Compliance', 'Financial Crime Risk', 'Risk Analytics', 'Treasury Risk', 'Model Risk',
    'Regulatory Risk', 'Risk and Compliance', 'Internal Audit', 'Risk Reporting', 'Stress Testing'
]

qualifications = ['Bachelors in Risk Management', 'Masters in Risk Management', 'MBA in Finance', 'Finance', 'Economics', 'Mathematics', 'Accounting']

employment_types = ['Full-time', 'Part-time', 'Contract']

skills = [
    'Risk Management', 'Credit Risk Analysis', 'Market Risk Analysis', 'Operational Risk Management',
    'Compliance', 'AML (Anti-Money Laundering)', 'KYC (Know Your Customer)', 'Financial Crime Prevention',
    'Risk Analytics', 'Regulatory Compliance', 'Risk Reporting', 'Risk Control', 'Financial Modeling',
    'Stress Testing', 'Liquidity Risk Management', 'Enterprise Risk Management', 'Risk Assessment'
]

certifications = [
    "Certified Risk Management Professional (CRMP)", "Financial Risk Manager (FRM)", "Certified Anti-Money Laundering Specialist (CAMS)",
    "Certified Fraud Examiner (CFE)", "Certified Compliance and Ethics Professional (CCEP)", "Certified Credit Risk Analyst (CCRA)",
    "Chartered Financial Analyst (CFA)", "Certified Financial Services Auditor (CFSA)", "Certified Risk Professional (CRP)",
    "Certified Treasury Professional (CTP)", "Certified Bank Auditor (CBA)", "Certified Regulatory Compliance Manager (CRCM)",
    "Certified Financial Crime Specialist (CFCS)", "Certified Market Risk Analyst (CMRA)", "Certified Operational Risk Manager (CORM)",
    "Certified Enterprise Risk Manager (CERM)", "Project Management Professional (PMP)", "Certified Internal Auditor (CIA)"
]

skill_certifications_mapping = {
    'Risk Management': ["Certified Risk Management Professional (CRMP)", "Certified Risk Professional (CRP)"],
    'Credit Risk Analysis': ["Certified Credit Risk Analyst (CCRA)", "Financial Risk Manager (FRM)"],
    'Market Risk Analysis': ["Certified Market Risk Analyst (CMRA)", "Financial Risk Manager (FRM)"],
    'Operational Risk Management': ["Certified Operational Risk Manager (CORM)", "Certified Risk Management Professional (CRMP)"],
    'Compliance': ["Certified Compliance and Ethics Professional (CCEP)", "Certified Regulatory Compliance Manager (CRCM)"],
    'AML (Anti-Money Laundering)': ["Certified Anti-Money Laundering Specialist (CAMS)", "Certified Fraud Examiner (CFE)"],
    'KYC (Know Your Customer)': ["Certified Anti-Money Laundering Specialist (CAMS)", "Certified Fraud Examiner (CFE)"],
    'Financial Crime Prevention': ["Certified Anti-Money Laundering Specialist (CAMS)", "Certified Fraud Examiner (CFE)"],
    'Risk Analytics': ["Certified Risk Professional (CRP)", "Certified Risk Management Professional (CRMP)"],
    'Regulatory Compliance': ["Certified Regulatory Compliance Manager (CRCM)", "Certified Compliance and Ethics Professional (CCEP)"],
    'Risk Reporting': ["Certified Risk Management Professional (CRMP)", "Certified Financial Services Auditor (CFSA)"],
    'Risk Control': ["Certified Risk Management Professional (CRMP)", "Certified Financial Risk Manager (FRM)"],
    'Financial Modeling': ["Chartered Financial Analyst (CFA)", "Certified Financial Services Auditor (CFSA)"],
    'Stress Testing': ["Certified Financial Risk Manager (FRM)", "Certified Credit Risk Analyst (CCRA)"],
    'Liquidity Risk Management': ["Certified Treasury Professional (CTP)", "Certified Financial Services Auditor (CFSA)"],
    'Enterprise Risk Management': ["Certified Enterprise Risk Manager (CERM)", "Certified Risk Management Professional (CRMP)"],
    'Risk Assessment': ["Certified Risk Management Professional (CRMP)", "Certified Risk Professional (CRP)"]
}

region = ['APAC', 'EMEA', 'AMER', 'GLOBAL']

# Helper functions
def get_random_exp(grade):
    exp_range = {
        'L1': (1, 5),
        'L2': (3, 7),
        'L3': (5, 10),
        'AVP': (8, 15),
        'VP': (10, 20),
        'Director': (15, 25),
        'Executive Director': (15, 25),
        'Managing Director': (15, 35)
    }
    min_exp, max_exp = exp_range.get(grade, (1, 35))
    return random.randint(min_exp, max_exp)

def get_random_compensation(grade):
    comp_range = {
        'L1': (30000, 80000),
        'L2': (50000, 100000),
        'L3': (80000, 150000),
        'AVP': (120000, 250000),
        'VP': (200000, 500000),
        'Director': (400000, 800000),
        'Executive Director': (600000, 1000000),
        'Managing Director': (800000, 1500000)
    }
    min_comp, max_comp = comp_range.get(grade, (1000, 30000))
    return random.randint(min_comp, max_comp)

def get_random_certifications(skills):
    certifications_list = []
    for skill in skills:
        certifications_list.extend(skill_certifications_mapping.get(skill, []))
    return list(set(certifications_list))  # Ensure no duplicates

def generate_employee(emp_id):
    grade = random.choice(grades)
    role = random.choice(role_grade_mapping[grade])
    department = random.choice(departments)
    skills_for_role = random.sample(skills, random.randint(3, 5))  # Select 3-5 skills
    certifications_for_skills = get_random_certifications(skills_for_role)

    total_exp = get_random_exp(grade)
    exp_current_role = random.randint(1, min(total_exp, 10))  # Current role experience <= total experience

    return {
        "EMP_ID": emp_id,
        "FIRST_NAME": fake.first_name(),
        "LAST_NAME": fake.last_name(),
        "GENDER": random.choice(['Male', 'Female']),
        "EMAIL": fake.email(),
        "GRADE": grade,
        "JOB_FAMILY": 'Risk Management',
        "ROLE": role,
        "ROLE_DESCRIPTION": fake.job(),
        "TOTAL_EXP": total_exp,
        "EXP_CURRENT_ROLE": exp_current_role,
        "SKILLS": ", ".join(skills_for_role),
        "DEPARTMENT": department,
        "QUALIFICATION": random.choice(qualifications),
        "CERTIFICATIONS": ", ".join(certifications_for_skills),
        "COMPENSATION": get_random_compensation(grade),
        "COUNTRY": fake.country(),
        "REGION": random.choice(region),
        "EMPLOYMENT_TYPE": random.choice(employment_types)
    }

def generate_employees(num_records):
    employees = [generate_employee(i) for i in range(1, num_records + 1)]
    return employees

# Generate 2000 employee records
employees_data = generate_employees(2000)

# Save to JSON file
with open('synthetic_data_riskMgmt.json', 'w') as f:
    json.dump(employees_data, f, indent=4)

print("Employee data generation complete. Saved to 'synthetic_data_riskMgmt.json'")
