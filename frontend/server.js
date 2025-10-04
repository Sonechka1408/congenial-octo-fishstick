import express from 'express';
import { fileURLToPath } from 'url';
import { dirname, join, extname } from 'path';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files
app.use(express.static(join(__dirname)));

// Handle HTML routes for all pages
app.get('/', (req, res) => {
  res.sendFile(join(__dirname, 'index.html'));
});

app.get('/cases.html', (req, res) => {
  res.sendFile(join(__dirname, 'cases.html'));
});

app.get('/about-us.html', (req, res) => {
  res.sendFile(join(__dirname, 'about-us.html'));
});

app.get('/marketing.html', (req, res) => {
  res.sendFile(join(__dirname, 'marketing.html'));
});

app.get('/personal-design.html', (req, res) => {
  res.sendFile(join(__dirname, 'personal-design.html'));
});

app.get('/strategy.html', (req, res) => {
  res.sendFile(join(__dirname, 'strategy.html'));
});

app.get('/contact.html', (req, res) => {
  res.sendFile(join(__dirname, 'contact.html'));
});

// Handle routes without .html extension
app.get('/cases', (req, res) => {
  res.sendFile(join(__dirname, 'cases.html'));
});

app.get('/about-us', (req, res) => {
  res.sendFile(join(__dirname, 'about-us.html'));
});

app.get('/marketing', (req, res) => {
  res.sendFile(join(__dirname, 'marketing.html'));
});

app.get('/personal-design', (req, res) => {
  res.sendFile(join(__dirname, 'personal-design.html'));
});

app.get('/strategy', (req, res) => {
  res.sendFile(join(__dirname, 'strategy.html'));
});

app.get('/contact', (req, res) => {
  res.sendFile(join(__dirname, 'contact.html'));
});

// Fallback for SPA - serve index.html for any other route
app.get('*', (req, res) => {
  // Check if the request is for a file that exists
  const requestedPath = join(__dirname, req.path);
  
  try {
    if (fs.existsSync(requestedPath) && extname(requestedPath) !== '') {
      // If it's a file (has extension), serve it
      res.sendFile(requestedPath);
    } else {
      // Otherwise serve index.html for SPA routing
      res.sendFile(join(__dirname, 'index.html'));
    }
  } catch (error) {
    // If any error, serve index.html
    res.sendFile(join(__dirname, 'index.html'));
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server is running on port ${PORT}`);
  console.log(`Visit: http://localhost:${PORT}`);
});