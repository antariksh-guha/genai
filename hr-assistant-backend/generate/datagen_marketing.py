import random
import json
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define metadata
job_family = ['Marketing']
grades = ['L1', 'L2', 'L3', 'AVP', 'VP', 'Director', 'Executive Director', 'Managing Director']
roles = [
    'Marketing Assistant', 'Marketing Coordinator', 'Junior Digital Marketing Specialist', 'Marketing Analyst',
    'Digital Marketing Manager', 'Brand Manager', 'Customer Engagement Specialist', 'Campaign Manager',
    'Product Marketing Manager', 'Content Marketing Manager', 'Social Media Manager', 'SEO Specialist', 
    'Market Research Manager', 'CRM Manager', 'Head of Marketing', 'VP of Marketing', 'Chief Marketing Officer (CMO)',
    'Director of Digital Marketing', 'Director of Brand Marketing'
]
role_grade_mapping = {
    'L1': ['Marketing Assistant', 'Marketing Coordinator'],
    'L2': ['Junior Digital Marketing Specialist', 'Marketing Analyst'],
    'L3': ['Digital Marketing Manager', 'Brand Manager', 'Campaign Manager'],
    'AVP': ['Product Marketing Manager', 'Customer Engagement Specialist'],
    'VP': ['Head of Marketing', 'VP of Marketing'],
    'Director': ['Director of Digital Marketing', 'Director of Brand Marketing'],
    'Executive Director': ['Chief Marketing Officer (CMO)'],
    'Managing Director': ['Chief Marketing Officer (CMO)']
}
departments = [
    'Marketing', 'Digital Marketing', 'Brand Management', 'Customer Engagement', 'Product Marketing', 
    'Market Research', 'Campaign Management', 'Content Marketing', 'Social Media Marketing', 'SEO & SEM',
    'CRM', 'Public Relations', 'Event Management', 'Advertising', 'Corporate Communications'
]
qualifications = ['Bachelors in Marketing', 'Masters in Marketing', 'MBA in Marketing', 'Communications', 
                  'Business Administration', 'Economics']
employment_types = ['Full-time', 'Part-time', 'Contract']
skills_list = [
    'Digital Marketing', 'Brand Strategy', 'Content Marketing', 'SEO (Search Engine Optimization)', 'Social Media Marketing',
    'Customer Relationship Management (CRM)', 'Market Research', 'Campaign Management', 'Email Marketing', 'PPC (Pay-per-click)',
    'Lead Generation', 'Public Relations', 'Copywriting', 'Advertising', 'Analytics', 'Data-Driven Marketing', 'Customer Insights'
]
certifications = [
    "Google Ads Certification", "Google Analytics Certification", "HubSpot Inbound Marketing Certification", 
    "Facebook Blueprint Certification", "Certified Digital Marketing Professional (CDMP)", "Hootsuite Social Media Marketing Certification", 
    "Content Marketing Certification", "SEO Certification (Moz, SEMrush)", "Marketing Analytics Certification", 
    "Customer Relationship Management (CRM) Certification", "PMP (Project Management Professional) Certification",
    "Certified Marketing Management Professional (CMMP)", "Financial Services Marketing Specialist (FSMS)"
]
skill_certifications_mapping = {
    'Digital Marketing': ["Google Ads Certification", "Google Analytics Certification", "Certified Digital Marketing Professional (CDMP)"],
    'Brand Strategy': ["Certified Marketing Management Professional (CMMP)"],
    'Content Marketing': ["Content Marketing Certification", "HubSpot Inbound Marketing Certification"],
    'SEO (Search Engine Optimization)': ["SEO Certification (Moz, SEMrush)"],
    'Social Media Marketing': ["Hootsuite Social Media Marketing Certification", "Facebook Blueprint Certification"],
    'Customer Relationship Management (CRM)': ["Customer Relationship Management (CRM) Certification"],
    'Market Research': ["Marketing Analytics Certification", "Certified Marketing Management Professional (CMMP)"],
    'Campaign Management': ["PMP (Project Management Professional) Certification"],
    'Email Marketing': ["HubSpot Email Marketing Certification"],
    'PPC (Pay-per-click)': ["Google Ads Certification", "Facebook Blueprint Certification"],
    'Lead Generation': ["Certified Digital Marketing Professional (CDMP)", "HubSpot Inbound Marketing Certification"],
    'Public Relations': ["Certified Marketing Management Professional (CMMP)"],
    'Copywriting': ["Content Marketing Certification", "Certified Marketing Management Professional (CMMP)"],
    'Advertising': ["PMP (Project Management Professional) Certification"],
    'Analytics': ["Google Analytics Certification", "Marketing Analytics Certification"],
    'Data-Driven Marketing': ["Certified Marketing Management Professional (CMMP)", "Marketing Analytics Certification"],
    'Customer Insights': ["Certified Digital Marketing Professional (CDMP)", "Marketing Analytics Certification"]
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
        "JOB_FAMILY": 'Marketing',
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
employees = [generate_employee(6001 + i) for i in range(2000)]

# Write to JSON file
with open('synthetic_data_marketing.json', 'w') as f:
    json.dump(employees, f, indent=4)

print("Employee data generated successfully!")
