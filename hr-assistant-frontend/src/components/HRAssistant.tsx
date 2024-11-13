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
  AppBar,
  Toolbar,
  IconButton,
  Avatar,
  Menu,
} from "@mui/material";
import { hrService } from "../services/hr-service";
import { validateJson } from "../utils/jsonHelpers";

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

  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const open = Boolean(anchorEl);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    setAnchorEl(null);
  };

  const handleMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const clearInputs = () => {
    setJobDesc("");
    // setResume("");
    setNumber("");
    setEmployeeData("");
    setInternalPositions("");
    setResult("");
  };

  const handleTabChange = (tab: string) => {
    setActiveTab(tab);
    clearInputs();
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

      let response;
      switch (activeTab) {
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
      <AppBar position="fixed" color="default" elevation={1}>
        <Toolbar sx={{ justifyContent: "flex-end" }}>
          {isLoggedIn ? (
            <div>
              <IconButton onClick={handleMenu}>
                <Avatar sx={{ bgcolor: "primary.main" }}>
                  {/* User initial or icon */}
                  U
                </Avatar>
              </IconButton>
              <Menu
                anchorEl={anchorEl}
                open={open}
                onClose={handleClose}
              >
                <MenuItem onClick={handleLogout}>Logout</MenuItem>
              </Menu>
            </div>
          ) : (
            <Button
              variant="contained"
              onClick={handleLogin}
              sx={{ textTransform: 'none' }}
            >
              Login
            </Button>
          )}
        </Toolbar>
      </AppBar>

      {/* Add margin-top to account for fixed AppBar */}
      <Box sx={{ mt: 8 }}>
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
            HR Assistant
          </Typography>

          <Tabs 
            value={activeTab}
            onChange={(_, tab) => handleTabChange(tab)}
            variant="scrollable"
            scrollButtons="auto"
            sx={{ mb: 3 }}
          >
            <Tab label="Interview Questions" value="interview" />
            <Tab label="Resume Screening" value="resume" />
            <Tab label="Job Description" value="jobdesc" />
            <Tab label="Internal Mobility" value="mobility" />
            <Tab label="HR Documents" value="document" />
          </Tabs>

          <Box component="form" onSubmit={handleSubmit}>
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

function formatJobDescription() {
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

function formatEmployeeData() {
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
