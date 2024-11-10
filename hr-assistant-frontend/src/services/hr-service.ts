import {
  JobDescription,
  ResumeScreening,
  InternalMobility,
  HRDocument,
  APIResponse,
} from "../types/hr-types";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "/api";

async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "API request failed");
  }
  return response.json();
}

export const hrService = {
  async generateInterviewQuestions(
    jobDescription: string
  ): Promise<APIResponse> {
    const response = await fetch(`${API_BASE_URL}/interview-questions`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ job_description: jobDescription }),
    });
    return handleResponse<APIResponse>(response);
  },

  async screenResume(data: ResumeScreening): Promise<APIResponse> {
    const response = await fetch(`${API_BASE_URL}/screen-resume`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    return handleResponse<APIResponse>(response);
  },

  async generateJobDescription(data: JobDescription): Promise<APIResponse> {
    const response = await fetch(`${API_BASE_URL}/job-description`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    return handleResponse<APIResponse>(response);
  },

  async suggestInternalMobility(data: InternalMobility): Promise<APIResponse> {
    const response = await fetch(`${API_BASE_URL}/internal-mobility`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    return handleResponse<APIResponse>(response);
  },

  async generateHRDocument(data: HRDocument): Promise<APIResponse> {
    const response = await fetch(`${API_BASE_URL}/hr-document`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    return handleResponse<APIResponse>(response);
  },
};
