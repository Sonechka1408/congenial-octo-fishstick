const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from current directory
app.use(express.static(__dirname));

// Handle all routes
app.get('*', (req, res) => {
  const requestedPath = req.path;
  
  // If root, serve index.html
  if (requestedPath === '/') {
    return res.sendFile(path.join(__dirname, 'index.html'));
  }
  
  // If path ends with .html, serve the HTML file
  if (requestedPath.endsWith('.html')) {
    const filePath = path.join(__dirname, requestedPath);
    if (fs.existsSync(filePath)) {
      return res.sendFile(filePath);
    }
  }
  
  // If path doesn't have extension, try to serve .html file
  const htmlPath = path.join(__dirname, requestedPath + '.html');
  if (fs.existsSync(htmlPath)) {
    return res.sendFile(htmlPath);
  }
  
  // For any other case, serve index.html (SPA fallback)
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Make sure all HTML files are in the root directory!');
});