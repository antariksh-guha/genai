import { ThemeProvider } from '@mui/material';
import { theme } from './theme';
import { HRAssistant } from "./components/HRAssistant";
import { Box } from '@mui/material';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Box sx={{ 
        minHeight: '100vh',
        bgcolor: 'background.default',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        py: 3
      }}>
        <HRAssistant />
      </Box>
    </ThemeProvider>
  );
}

export default App;
