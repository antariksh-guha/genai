import random
import json
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define metadata
job_families = ['Trading']

grades = ['L1', 'L2', 'L3', 'AVP', 'VP', 'Director', 'Executive Director', 'Managing Director']

roles = [
    'Trading Assistant', 'Junior Trader', 'Trade Support Analyst', 'Trading Analyst', 
    'Senior Trader', 'Risk Trader', 'Quantitative Analyst', 'Trade Operations Manager', 
    'Head of Trading', 'VP of Trading', 'Director of Trading', 'Chief Trading Officer', 
    'Head of Proprietary Trading', 'Head of Algorithmic Trading', 'Director of Trade Execution'
]

role_grade_mapping = {
    'L1': ['Trading Assistant', 'Junior Trader', 'Trade Support Analyst'],
    'L2': ['Trading Analyst', 'Risk Trader', 'Quantitative Analyst'],
    'L3': ['Senior Trader', 'Trade Operations Manager', 'Trading Specialist'],
    'AVP': ['Head of Trading', 'VP of Trading'],
    'VP': ['Director of Trading', 'Head of Proprietary Trading'],
    'Director': ['Director of Trading', 'Head of Algorithmic Trading'],
    'Executive Director': ['Chief Trading Officer'],
    'Managing Director': ['Chief Trading Officer']
}

departments = [
    'Trading', 'Proprietary Trading', 'Algorithmic Trading', 'Equity Trading', 'Fixed Income Trading', 
    'Commodities Trading', 'FX Trading', 'Derivatives Trading', 'Trade Operations', 'Market Risk', 'Quantitative Research'
]

qualifications = ['Bachelors in Finance', 'Masters in Finance', 'MBA in Finance', 'Economics', 'Mathematics', 'Engineering']

employment_types = ['Full-time', 'Part-time', 'Contract']

skills = [
    'Equity Trading', 'Derivatives Trading', 'Fixed Income Trading', 'Foreign Exchange (FX) Trading', 'Commodities Trading',
    'Algorithmic Trading', 'Quantitative Analysis', 'Risk Management', 'Trading Strategies', 'Market Microstructure', 
    'Portfolio Management', 'High-Frequency Trading', 'Financial Modelling', 'Execution Algorithms', 'Market Risk Analysis', 
    'Trade Execution', 'Trading Platforms', 'Regulatory Compliance'
]

certifications = [
    "Chartered Financial Analyst (CFA)", "Financial Risk Manager (FRM)", "Certified Quantitative Analyst (CQF)", 
    "Certified Treasury Professional (CTP)", "Certified Financial Services Auditor (CFSA)", "Project Management Professional (PMP)",
    "Certified Algorithmic Trading Professional (CATP)", "Certified Trading Professional (CTP)", "Market Risk Certification (PRMIA)", 
    "Certified Market Technician (CMT)", "Certified Risk Management Professional (CRMP)", "Financial Modeling and Valuation Analyst (FMVA)"
]

skill_certifications_mapping = {
    'Equity Trading': ["Chartered Financial Analyst (CFA)", "Certified Trading Professional (CTP)"],
    'Derivatives Trading': ["Chartered Financial Analyst (CFA)", "Certified Quantitative Analyst (CQF)"],
    'Fixed Income Trading': ["Certified Trading Professional (CTP)", "Financial Risk Manager (FRM)"],
    'Foreign Exchange (FX) Trading': ["Chartered Financial Analyst (CFA)", "Certified Risk Management Professional (CRMP)"],
    'Commodities Trading': ["Certified Financial Services Auditor (CFSA)", "Certified Trading Professional (CTP)"],
    'Algorithmic Trading': ["Certified Algorithmic Trading Professional (CATP)", "Certified Quantitative Analyst (CQF)"],
    'Quantitative Analysis': ["Certified Quantitative Analyst (CQF)", "Financial Risk Manager (FRM)"],
    'Risk Management': ["Certified Risk Management Professional (CRMP)", "Financial Risk Manager (FRM)"],
    'Trading Strategies': ["Chartered Financial Analyst (CFA)", "Certified Market Technician (CMT)"],
    'Market Microstructure': ["Certified Trading Professional (CTP)", "Certified Market Technician (CMT)"],
    'Portfolio Management': ["Chartered Financial Analyst (CFA)", "Financial Risk Manager (FRM)"],
    'High-Frequency Trading': ["Certified Algorithmic Trading Professional (CATP)", "Certified Quantitative Analyst (CQF)"],
    'Financial Modelling': ["Certified Financial Modeling & Valuation Analyst (FMVA)", "Chartered Financial Analyst (CFA)"],
    'Execution Algorithms': ["Certified Algorithmic Trading Professional (CATP)", "Certified Quantitative Analyst (CQF)"],
    'Market Risk Analysis': ["Financial Risk Manager (FRM)", "Certified Risk Management Professional (CRMP)"],
    'Trade Execution': ["Certified Trading Professional (CTP)", "Project Management Professional (PMP)"],
    'Trading Platforms': ["Certified Trading Professional (CTP)", "Financial Modeling and Valuation Analyst (FMVA)"],
    'Regulatory Compliance': ["Certified Compliance and Ethics Professional (CCEP)", "Certified Bank Auditor (CBA)"]
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
    skill = random.choice(skills)
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
        "JOB_FAMILY": 'Trading',
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
employees = [generate_employee(8001 + i) for i in range(2000)]

# Write to JSON file
with open('synthetic_data_trading.json', 'w') as f:
    json.dump(employees, f, indent=4)

print("Employee data generated successfully!")
