export const config = {
  apiBaseUrl: process.env.REACT_APP_API_BASE_URL || "/api",
  maxRequestSize: 1024 * 1024, // 1MB
  timeoutMs: 30000,
};
