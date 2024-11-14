import random
import json
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define metadata
job_families = ['Technology']
grades = ['L1', 'L2', 'L3', 'AVP', 'VP', 'Director', 'Executive Director', 'Managing Director']
roles = [
    'Software Engineer', 'Junior Developer', 'Application Support Analyst', 'Systems Analyst',
    'Database Administrator', 'Security Analyst', 'IT Support Specialist', 'Infrastructure Engineer',
    'Cloud Architect', 'DevOps Engineer', 'Business Analyst', 'Data Scientist', 'Solutions Architect',
    'Head of IT', 'VP of Technology', 'Director of Technology', 'Chief Technology Officer', 'Technical Program Manager',
    'Risk Technology Analyst', 'Financial Systems Analyst', 'Quantitative Analyst', 'Blockchain Developer', 'Compliance Technology Specialist'
]
departments = [
    'Technology', 'Software Development', 'IT Support', 'Risk Management Technology', 'Compliance Technology', 'Data Analytics', 'Cloud Computing', 
    'Infrastructure', 'Cybersecurity', 'Business Intelligence', 'Digital Transformation', 'Blockchain', 'Quantitative Analysis', 'Financial Systems', 
    'Application Development', 'AI and Machine Learning', 'Project Management', 'Regulatory Technology', 'Treasury Technology'
]
qualifications = [
    'Bachelors in Computer Science', 'Masters in Computer Science', 'MBA in Technology Management', 'Information Technology', 
    'Software Engineering', 'Data Science', 'Cybersecurity', 'Computer Engineering', 'Finance', 'Risk Management', 'Economics', 'Quantitative Finance'
]
skills = [
    'Software Development', 'Java', 'Python', 'C++', 'SQL', 'Data Analysis', 'Machine Learning', 'Cloud Computing',
    'Cybersecurity', 'DevOps', 'Agile', 'Blockchain', 'Network Security', 'Database Management', 'AI', 'Automation',
    'Big Data', 'Project Management', 'Cloud Infrastructure', 'System Integration', 'Risk Technology', 'Financial Modelling', 'Quantitative Analysis', 
    'Regulatory Technology', 'Treasury Management Systems', 'Financial Services Applications'
]
certifications = [
    "Certified Information Systems Security Professional (CISSP)", "Certified Cloud Security Professional (CCSP)", "AWS Certified Solutions Architect", 
    "Microsoft Certified: Azure Solutions Architect Expert", "Certified ScrumMaster (CSM)", "Certified Kubernetes Administrator (CKA)",
    "Oracle Certified Professional (OCP)", "Certified Data Scientist (CDS)", "Certified Ethical Hacker (CEH)", "CompTIA Security+",
    "Google Professional Data Engineer", "Project Management Professional (PMP)", "Certified Blockchain Professional (CBP)", 
    "Cisco Certified Network Associate (CCNA)", "Certified Information Security Manager (CISM)", "Certified DevOps Engineer (CDE)", 
    "Chartered Financial Analyst (CFA)", "Financial Risk Manager (FRM)", "Certified Quantitative Analyst (CQF)", "Certified Treasury Professional (CTP)",
    "Certified Anti-Money Laundering Specialist (CAMS)", "Certified Financial Services Auditor (CFSA)", "Certified Risk Management Professional (CRMP)",
    "Certified Regulatory Compliance Manager (CRCM)", "Certified Bank Auditor (CBA)"
]
region = ['APAC', 'EMEA', 'AMER', 'GLOBAL']

# Role to Grade Mapping
role_grade_mapping = {
    'L1': ['Software Engineer', 'Junior Developer', 'Application Support Analyst'],
    'L2': ['Systems Analyst', 'Database Administrator', 'Security Analyst'],
    'L3': ['IT Support Specialist', 'Infrastructure Engineer', 'Cloud Architect'],
    'AVP': ['DevOps Engineer', 'Business Analyst', 'Risk Technology Analyst'],
    'VP': ['Solutions Architect', 'Head of IT', 'Financial Systems Analyst'],
    'Director': ['VP of Technology', 'Director of Technology', 'Compliance Technology Specialist'],
    'Executive Director': ['Chief Technology Officer'],
    'Managing Director': ['Chief Technology Officer']
}

# Salary based on Grade
salary_range = {
    'L1': (30000, 80000),
    'L2': (50000, 100000),
    'L3': (80000, 150000),
    'AVP': (120000, 250000),
    'VP': (200000, 500000),
    'Director': (400000, 800000),
    'Executive Director': (600000, 1000000),
    'Managing Director': (800000, 1500000)
}

# Skill to Certifications Mapping
skill_certifications_mapping = {
    'Software Development': ["Oracle Certified Professional (OCP)", "Certified ScrumMaster (CSM)", "Certified DevOps Engineer (CDE)"],
    'Java': ["Oracle Certified Professional (OCP)", "AWS Certified Solutions Architect"],
    'Python': ["Certified Data Scientist (CDS)", "Certified Ethical Hacker (CEH)"],
    'C++': ["Oracle Certified Professional (OCP)", "Certified ScrumMaster (CSM)"],
    'SQL': ["Microsoft Certified: Azure Solutions Architect Expert", "AWS Certified Solutions Architect"],
    'Data Analysis': ["Certified Data Scientist (CDS)", "Google Professional Data Engineer"],
    'Machine Learning': ["Certified Data Scientist (CDS)", "AWS Certified Machine Learning - Specialty"],
    'Cloud Computing': ["AWS Certified Solutions Architect", "Microsoft Certified: Azure Solutions Architect Expert"],
    'Cybersecurity': ["Certified Information Systems Security Professional (CISSP)", "Certified Ethical Hacker (CEH)", "CompTIA Security+"],
    'DevOps': ["Certified Kubernetes Administrator (CKA)", "Certified DevOps Engineer (CDE)"],
    'Agile': ["Certified ScrumMaster (CSM)", "Project Management Professional (PMP)"],
    'Blockchain': ["Certified Blockchain Professional (CBP)", "Certified Ethical Hacker (CEH)"],
    'Network Security': ["Certified Information Systems Security Professional (CISSP)", "CompTIA Security+"],
    'Database Management': ["Oracle Certified Professional (OCP)", "Microsoft Certified: Azure Solutions Architect Expert"],
    'AI': ["Certified Data Scientist (CDS)", "AWS Certified Machine Learning - Specialty"],
    'Automation': ["Certified Kubernetes Administrator (CKA)", "Certified DevOps Engineer (CDE)"],
    'Big Data': ["Google Professional Data Engineer", "AWS Certified Big Data - Specialty"],
    'Project Management': ["Project Management Professional (PMP)", "Certified ScrumMaster (CSM)"],
    'Cloud Infrastructure': ["AWS Certified Solutions Architect", "Microsoft Certified: Azure Solutions Architect Expert"],
    'System Integration': ["Certified Kubernetes Administrator (CKA)", "Certified DevOps Engineer (CDE)"],
    'Risk Technology': ["Certified Risk Management Professional (CRMP)", "Financial Risk Manager (FRM)", "Certified Treasury Professional (CTP)"],
    'Financial Modelling': ["Chartered Financial Analyst (CFA)", "Certified Financial Services Auditor (CFSA)"],
    'Quantitative Analysis': ["Certified Quantitative Analyst (CQF)", "Financial Risk Manager (FRM)"],
    'Regulatory Technology': ["Certified Regulatory Compliance Manager (CRCM)", "Certified Anti-Money Laundering Specialist (CAMS)"],
    'Treasury Management Systems': ["Certified Treasury Professional (CTP)", "Certified Financial Services Auditor (CFSA)"],
    'Financial Services Applications': ["Certified Bank Auditor (CBA)", "Certified Financial Services Auditor (CFSA)"]
}

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
    compensation_range = salary_range.get(grade)
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
        "JOB_FAMILY": 'Technology',
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
employees = [generate_employee(2001 + i) for i in range(2000)]

# Write to JSON file
with open('synthetic_data_technology.json', 'w') as f:
    json.dump(employees, f, indent=4)

print("Employee data generated successfully!")
