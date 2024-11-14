import React, { useState } from "react";
import {
  Box,
  Paper,
  Typography,
  Tabs,
  Tab,
  TextField,
  Button,
  Select,
  MenuItem,
  CircularProgress,
  Alert,
  Stack,
} from "@mui/material";
import { hrService } from "../services/hr-service";
import { formatEmployeeData, formatInternalPosition, formatJobDescription, getEmployeeDataFormat, validateJson } from "../utils/jsonHelpers";
import { CareerProgressionRequest } from "../types/hr-types";

const LoadingSpinner = () => <CircularProgress size={20} color="inherit" />;

export const HRAssistant: React.FC = () => {
  const [activeTab, setActiveTab] = useState("interview");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<string>("");

  const [jobDesc, setJobDesc] = useState("");
  const [number, setNumber] = useState("");
  // const [resume, setResume] = useState("");
  const [employeeData, setEmployeeData] = useState("");
  const [documentType, setDocumentType] = useState("offer_letter");
  const [internalPositions, setInternalPositions] = useState<string>("");
  const [targetRole, setTargetRole] = useState("");
  const [targetGrade, setTargetGrade] = useState("");
  const [targetDepartment, setTargetDepartment] = useState("");
  const [targetJobFamily, setTargetJobFamily] = useState("");

  const clearInputs = () => {
    setJobDesc("");
    // setResume("");
    setNumber("");
    setEmployeeData("");
    setInternalPositions("");
    setResult("");
    setTargetRole("");
    setTargetGrade("");
    setTargetDepartment("");
    setTargetJobFamily("");
  };

  const handleTabChange = (tab: string) => {
    setActiveTab(tab);
    clearInputs();
    if (tab === "career") {
      setEmployeeData(getEmployeeDataFormat());
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      if (activeTab === "jobdesc") {
        if (!validateJson(jobDesc)) {
          throw new Error(
            `Invalid JSON format. Expected format:\n${formatJobDescription()}`
          );
        }
      }
     
      if (activeTab === "mobility") {
        if (!validateJson(employeeData)) {
          throw new Error(
            `Invalid JSON format. Expected format:\n${formatEmployeeData()}`
          );
        }
        if (!validateJson(internalPositions)) {
          throw new Error(
            `Invalid JSON format. Expected format:\n${formatInternalPosition()}`
          );
        }
      }

      if (activeTab === "document") {
        if (!validateJson(employeeData)) {
          throw new Error(
            `Invalid JSON format. Expected format:\n${formatEmployeeData()}`
          );
        }
      }

      if (activeTab === "career") {
        if (!validateJson(employeeData)) {
          throw new Error(
            `Invalid JSON format. Expected format:\n${formatEmployeeData()}`
          );
        }
      }

      let response;
      switch (activeTab) {
        case "career":
          let curObj: CareerProgressionRequest = {
            employee_data: JSON.parse(employeeData), 
            target_role: targetRole,
            target_grade: targetGrade,
            target_department: targetDepartment,
            target_job_family: targetJobFamily
          };
          response = await hrService.suggestCareerProgression(curObj);
          setResult(response.suggestions || "");
          break;
        case "interview":
          response = await hrService.generateInterviewQuestions(jobDesc);
          setResult(response.questions || "");
          break;
        case "resume":
          response = await hrService.screenResume(number, jobDesc);
          setResult(JSON.stringify(response.analysis) || "");
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
    <>
      {/* Add margin-top to account for fixed AppBar */}
      <Box>
        <Paper 
          elevation={2} 
          sx={{ 
            maxWidth: 800, 
            mx: 'auto', 
            p: 3,
            bgcolor: 'background.paper' 
          }}
        >
          <Typography variant="h4" gutterBottom align="center">
            Talent Rise
          </Typography>

            <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 3 }}>
              
            <Tabs 
              value={activeTab}
              onChange={(_, tab) => handleTabChange(tab)}
              variant="scrollable"
              scrollButtons="auto"
            >
              <Tab label="Path Finder" value="career" sx={{ ml: 2 }} />
              <Tab label="Talent Hound" value="resume" sx={{ ml: 2 }} />
              <Tab label="HireWise" value="interview" />
              <Tab label="Job Match" value="mobility" />
              <Tab label="Docufy" value="document" />
            </Tabs>
            </Box>

          <Box component="form" onSubmit={handleSubmit}>
            {activeTab === "career" && (
              <Stack spacing={3}>
                <Box>
                    <Typography variant="h6" gutterBottom>
                    Current Profile
                    </Typography>
                    {employeeData && (
                    <Box sx={{ mb: 2 }}>
                      {Object.entries(JSON.parse(employeeData)).map(([key, value]) => (
                        <Typography key={key} sx={{ mb: 1 }}>
                          <strong>{key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}:</strong>{' '}
                          {typeof value === 'object' ? JSON.stringify(value) : String(value)}
                        </Typography>
                      ))}
                    </Box>
                    )}
                
                  {/* <Button
                    variant="outlined"
                    onClick={() => setEmployeeData(getEmployeeDataFormat())}
                    color="secondary"
                    sx={{ mt: 1 }}
                  >
                    Generate Employee Data Format
                  </Button> */}
                </Box>

                
                <Box>
                  <Typography variant="h6" gutterBottom>
                    Target Role (Optional)
                  </Typography>
                  <TextField
                    value={targetRole}
                    onChange={(e) => setTargetRole(e.target.value)}
                    placeholder="Enter target role"
                    rows={1}
                  />
                </Box>

                <Box>
                  <Typography variant="h6" gutterBottom>
                  Target Grade (Optional)  
                  </Typography>
                  <TextField
                    type="text"
                    value={targetGrade}
                    onChange={(e) => setTargetGrade(e.target.value)}
                    placeholder="Enter target grade"
                    rows={1}
                  />
                </Box>

                <Box>
                  <Typography variant="h6" gutterBottom>
                    Target Department (Optional)  
                  </Typography>
                  <TextField
                    value={targetDepartment}
                    onChange={(e) => setTargetDepartment(e.target.value)}
                    placeholder="Enter target department"
                    rows={1}
                  />
                </Box>

                <Box>
                  <Typography variant="h6" gutterBottom>
                  Target Job Family (Optional)  
                  </Typography>
                  <TextField
                  value={targetJobFamily}
                  onChange={(e) => setTargetJobFamily(e.target.value)}
                  placeholder="Enter target job family"
                  rows={1}
                  />
                </Box>
              </Stack>
            )}

            {activeTab === "interview" && (
              <TextField
                value={jobDesc}
                onChange={(e) => setJobDesc(e.target.value)}
                placeholder="Enter job description"
                required
              />
            )}

            {activeTab === "resume" && (
              <Stack spacing={2}>
                <TextField
                  value={jobDesc}
                  onChange={(e) => setJobDesc(e.target.value)}
                  placeholder="Enter job description"
                  required
                />
                <TextField
                  value={number}
                  onChange={(e) => setNumber(e.target.value)}
                  placeholder="Enter number of resumes to fetch (1-10) to screen against job description"
                  required
                />
              </Stack>
            )}

            {activeTab === "jobdesc" && (
              <Stack spacing={2}>
                <TextField
                  value={jobDesc}
                  onChange={(e) => setJobDesc(e.target.value)}
                  placeholder="Enter job parameters (JSON)"
                  required
                />
                <Button
                  variant="outlined"
                  onClick={() => setJobDesc(formatJobDescription())}
                  color="secondary"
                >
                  Generate Job Desc Format
                </Button>
              </Stack>
            )}

            {activeTab === "mobility" && (
              <Stack spacing={3}>
                <Box>
                  <Typography variant="h6" gutterBottom>
                    Employee Data
                  </Typography>
                  <TextField
                    value={employeeData}
                    onChange={(e) => setEmployeeData(e.target.value)}
                    placeholder="Enter employee data (JSON)"
                    required
                  />
                  <Button
                    variant="outlined"
                    onClick={() => setEmployeeData(formatEmployeeData())}
                    color="secondary"
                    sx={{ mt: 1 }}
                  >
                    Generate Employee Data Format
                  </Button>
                </Box>

                <Box>
                  <Typography variant="h6" gutterBottom>
                    Available Positions
                  </Typography>
                  <TextField
                    value={internalPositions}
                    onChange={(e) => setInternalPositions(e.target.value)}
                    placeholder="Enter available positions (JSON array)"
                  />
                  <Button
                    variant="outlined"
                    onClick={() => setInternalPositions(formatInternalPosition())}
                    color="secondary"
                    sx={{ mt: 1 }}
                  >
                    Generate Positions Format
                  </Button>
                </Box>
              </Stack>
            )}

            {activeTab === "document" && (
              <Stack spacing={2}>
                <Select
                  value={documentType}
                  onChange={(e) => setDocumentType(e.target.value)}
                >
                  <MenuItem value="offer_letter">Offer Letter</MenuItem>
                  <MenuItem value="promotion_letter">Promotion Letter</MenuItem>
                  <MenuItem value="termination_letter">Termination Letter</MenuItem>
                </Select>
                <TextField
                  value={employeeData}
                  onChange={(e) => setEmployeeData(e.target.value)}
                  placeholder="Enter employee data (JSON)"
                  required
                />
                <Button
                    variant="outlined"
                    onClick={() => setEmployeeData(formatEmployeeData())}
                    color="secondary"
                    sx={{ mt: 1 }}
                >
                    Generate Employee Data Format
                </Button>
              </Stack>
            )}

            <Button
              type="submit"
              variant="contained"
              disabled={loading}
              sx={{ mt: 3 }}
              startIcon={loading && <LoadingSpinner />}
            >
              {loading ? "Processing..." : "Submit"}
            </Button>
          </Box>

          {result && (
            <Box sx={{ mt: 3 }}>
              {result.startsWith("Error:") ? (
                <Alert severity="error" variant="outlined">
                  <Typography component="pre" sx={{ m: 0, whiteSpace: 'pre-wrap' }}>
                    {result}
                  </Typography>
                </Alert>
              ) : (
                <Paper variant="outlined" sx={{ p: 2 }}>
                  <Typography variant="h6" gutterBottom>
                    Result:
                  </Typography>
                  <Typography component="pre" sx={{ m: 0, whiteSpace: 'pre-wrap' }}>
                    {result}
                  </Typography>
                </Paper>
              )}
            </Box>
          )}
        </Paper>
      </Box>
    </>
  );
};
