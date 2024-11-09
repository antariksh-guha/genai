export interface JobDescription {
  parameters: {
    title: string;
    level: string;
    department: string;
    requirements: string[];
  };
}

export interface ResumeScreening {
  resume: string;
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
