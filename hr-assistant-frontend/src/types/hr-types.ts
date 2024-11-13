export interface JobDescription {
  parameters: {
    title: string;
    level: string;
    department: string;
    requirements: string[];
  };
}

export interface ResumeScreening {
  number: string;
  job_description: string;
}

export interface InternalPosition {
  id: string;
  title: string;
  department: string;
  level: string;
  requirements: string[];
}

export interface InternalMobility {
  employee_data: {
    current_role: string;
    skills: string[];
    experience: string[];
    interests: string[];
    preferred_departments?: string[];
  };
  available_positions?: InternalPosition[];
}

export interface HRDocument {
  template_type: string;
  employee_data: {
    name: string;
    position: string;
    department: string;
    [key: string]: any;
  };
}

export interface APIResponse {
  questions?: string;
  analysis?: string;
  job_description?: string;
  suggestions?: string;
  document?: string;
  
}

export interface ResumeScreenRequest {
  job_description: string;
  resume_text: string; // Added missing field
}

export interface ResumeScreenResponse {
  analysis: {
    id: string;
    name: string;
    similarity_score: number;
    match_details: string;
  }[];
}

export interface CareerProgressionRequest {
  employee_data: {
    current_role: string;
    grade: string;
    department: string;
    job_family: string;
    skills: string[];
    total_exp: number;
    qualifications: string[];
    certifications: string[];
  };
  target_role?: string;
  target_grade?: string;
  target_department?: string;
  target_job_family?: string;
}

export const employeeDataSchema = {
  type: "object",
  required: [
    "GRADE",
    "JOB_FAMILY", 
    "ROLE",
    "TOTAL_EXP",
    "SKILLS",
    "DEPARTMENT",
    "QUALIFICATION",
    "CERTIFICATIONS"
  ],
  properties: {
    GRADE: { type: "string" },
    JOB_FAMILY: { type: "string" },
    ROLE: { type: "string" },
    TOTAL_EXP: { type: "number", minimum: 0 },
    SKILLS: { type: "string" },
    DEPARTMENT: { type: "string" },
    QUALIFICATION: { type: "string" },
    CERTIFICATIONS: { type: "string" }
  }
};
