// src/utils/jsonHelpers.ts
export const validateJson = (text: string): boolean => {
  try {
    JSON.parse(text);
    return true;
  } catch {
    return false;
  }
};

export const validateEmployeeData = (data: any): boolean => {
  try {
    // Parse JSON if string
    const employeeData = typeof data === 'string' ? JSON.parse(data) : data;

    // Check required fields
    const requiredFields = ["GRADE", "JOB_FAMILY", "ROLE", "TOTAL_EXP", 
                          "SKILLS", "DEPARTMENT", "QUALIFICATION", "CERTIFICATIONS"];
    
    const missingFields = requiredFields.filter(field => !employeeData[field]);
    if (missingFields.length) {
      throw new Error(`Missing required fields: ${missingFields.join(', ')}`);
    }

    // Validate types
    if (typeof employeeData.TOTAL_EXP !== 'number' || employeeData.TOTAL_EXP < 0) {
      throw new Error('TOTAL_EXP must be a positive number');
    }

    const stringFields = ["GRADE", "JOB_FAMILY", "ROLE", "SKILLS", 
                         "DEPARTMENT", "QUALIFICATION", "CERTIFICATIONS"];
    
    stringFields.forEach(field => {
      if (typeof employeeData[field] !== 'string') {
        throw new Error(`${field} must be a string`);
      }
    });

    return true;
  } catch (error) {
    console.error('Employee data validation error:', error);
    throw error;
  }
};

// Add sample data format function
export const getEmployeeDataFormat = (): string => {
  return JSON.stringify({
    "GRADE": "L3",
    "JOB_FAMILY": "Trading",
    "ROLE": "Senior Trader",
    "TOTAL_EXP": 5,
    "SKILLS": "Fixed Income Trading",
    "DEPARTMENT": "FX Trading",
    "QUALIFICATION": "Bachelors",
    "CERTIFICATIONS": "Chartered Financial Analyst (CFA)"
  }, null, 2);
};

export const formatJobDescription = (): string => {
  return JSON.stringify(
    {
      title: "",
      department: "",
      level: "",
      responsibilities: [],
      requirements: [],
      location: "",
      salary_range: "",
    },
    null,
    2
  );
}

export const formatInternalPosition = (): string =>{
  return JSON.stringify(
    [
      {
        id: "",
        title: "",
        department: "",
        level: "",
        requirements: [],
      },
    ],
    null,
    2
  );
}

export const formatEmployeeData = (): string => {
  return JSON.stringify(
    {
      name: "",
      position: "",
      department: "",
      start_date: "",
      salary: "",
      email: "",
      // Additional fields needed for HR documents
      manager: "",
      employee_id: "",
      effective_date: ""
    },
    null,
    2
  );
}
