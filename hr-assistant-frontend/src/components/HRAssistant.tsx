import React, { useState } from "react";
import { hrService } from "../services/hr-service";
import "./HRAssistant.css";
import { validateJson } from "../utils/jsonHelpers";

const LoadingSpinner = () => <div className="loading-spinner"></div>;

export const HRAssistant: React.FC = () => {
  const [activeTab, setActiveTab] = useState("interview");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<string>("");

  const [jobDesc, setJobDesc] = useState("");
  const [resume, setResume] = useState("");
  const [employeeData, setEmployeeData] = useState("");
  const [documentType, setDocumentType] = useState("offer_letter");
  const [internalPositions, setInternalPositions] = useState<string>("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      if (activeTab === "jobdesc") {
        if (!validateJson(jobDesc)) {
          throw new Error(
            `Invalid JSON format. Expected format:\n${formatJobDescription("")}`
          );
        }
      }
      // JSON parse validation needed before API calls
      if (activeTab === "jobdesc" || activeTab === "mobility") {
        try {
          JSON.parse(jobDesc); // Validate JSON
        } catch (e) {
          throw new Error("Invalid JSON format");
        }
      }

      let response;
      switch (activeTab) {
        case "interview":
          response = await hrService.generateInterviewQuestions(jobDesc);
          setResult(response.questions || "");
          break;
        case "resume":
          response = await hrService.screenResume({
            resume,
            job_description: jobDesc,
          });
          setResult(response.analysis || "");
          break;
        case "jobdesc":
          response = await hrService.generateJobDescription({
            parameters: JSON.parse(jobDesc),
          });
          setResult(response.job_description || "");
          break;
        case "mobility":
          response = await hrService.suggestInternalMobility({
            employee_data: JSON.parse(employeeData),
          });
          setResult(response.suggestions || "");
          break;
        case "document":
          response = await hrService.generateHRDocument({
            template_type: documentType,
            employee_data: JSON.parse(employeeData),
          });
          setResult(response.document || "");
          break;
      }
    } catch (error) {
      setResult(
        "Error: " +
          ((error as Error).message ||
            "An unexpected error occurred. Please try again.")
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="hr-assistant">
      <h1>HR Assistant</h1>

      <div className="tabs">
        <button onClick={() => setActiveTab("interview")}>
          Interview Questions
        </button>
        <button onClick={() => setActiveTab("resume")}>Resume Screening</button>
        <button onClick={() => setActiveTab("jobdesc")}>Job Description</button>
        <button onClick={() => setActiveTab("mobility")}>
          Internal Mobility
        </button>
        <button onClick={() => setActiveTab("document")}>HR Documents</button>
      </div>

      <form onSubmit={handleSubmit}>
        {activeTab === "interview" && (
          <textarea
            value={jobDesc}
            onChange={(e) => setJobDesc(e.target.value)}
            placeholder="Enter job description"
            required
          />
        )}

        {activeTab === "resume" && (
          <>
            <textarea
              value={jobDesc}
              onChange={(e) => setJobDesc(e.target.value)}
              placeholder="Enter job description"
              required
            />
            <textarea
              value={resume}
              onChange={(e) => setResume(e.target.value)}
              placeholder="Enter resume text"
              required
            />
          </>
        )}

        {activeTab === "jobdesc" && (
          <div>
            <textarea
              value={jobDesc}
              onChange={(e) => setJobDesc(e.target.value)}
              placeholder="Enter job parameters (JSON)"
              required
            />
            <button
              type="button"
              onClick={() => setJobDesc(formatJobDescription(""))}
            >
              Format JSON
            </button>
          </div>
        )}

        {activeTab === "mobility" && (
          <div className="mobility-section">
            <div className="input-group">
              <h3>Employee Data</h3>
              <textarea
                value={employeeData}
                onChange={(e) => setEmployeeData(e.target.value)}
                placeholder="Enter employee data (JSON)"
                required
              />
              <button
                type="button"
                onClick={() => setEmployeeData(formatEmployeeData())}
                className="format-button"
              >
                Format Employee Data
              </button>
            </div>

            <div className="input-group">
              <h3>Available Positions</h3>
              <textarea
                value={internalPositions}
                onChange={(e) => setInternalPositions(e.target.value)}
                placeholder="Enter available positions (JSON array)"
              />
              <button
                type="button"
                onClick={() => setInternalPositions(formatInternalPosition())}
                className="format-button"
              >
                Format Positions
              </button>
            </div>
          </div>
        )}

        {activeTab === "document" && (
          <>
            <select
              value={documentType}
              onChange={(e) => setDocumentType(e.target.value)}
            >
              <option value="offer_letter">Offer Letter</option>
              <option value="promotion_letter">Promotion Letter</option>
              <option value="termination_letter">Termination Letter</option>
            </select>
            <textarea
              value={employeeData}
              onChange={(e) => setEmployeeData(e.target.value)}
              placeholder="Enter employee data (JSON)"
              required
            />
          </>
        )}

        <button type="submit" disabled={loading}>
          {loading ? "Processing..." : "Submit"}
        </button>
      </form>

      {result && result.startsWith("Error:") ? (
        <div className="error-message">
          <pre>{result}</pre>
        </div>
      ) : (
        result && (
          <div className="result">
            <h3>Result:</h3>
            <pre>{result}</pre>
          </div>
        )
      )}
    </div>
  );
};
function formatJobDescription(jobDesc: string) {
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

function formatInternalPosition() {
  return JSON.stringify(
    [
      {
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

function formatEmployeeData() {
  return JSON.stringify(
    {
      name: "",
      position: "",
      department: "",
      experience: "",
      skills: [],
      performance: "",
    },
    null,
    2
  );
}
