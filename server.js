const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = 3000;

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url);
  const pathname = parsedUrl.pathname;

  // Handle video download
  if (pathname === '/download') {
    const videoPath = path.join(__dirname, 'sangeet-invitation.mp4');

    if (!fs.existsSync(videoPath)) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('Video not found');
      return;
    }

    const stat = fs.statSync(videoPath);
    const fileSize = stat.size;

    res.writeHead(200, {
      'Content-Type': 'video/mp4',
      'Content-Length': fileSize,
      'Content-Disposition': 'attachment; filename="sangeet-invitation.mp4"'
    });

    fs.createReadStream(videoPath).pipe(res);
  }
  // Serve the HTML preview
  else if (pathname === '/' || pathname === '/preview') {
    const videoPath = path.join(__dirname, 'sangeet-invitation.mp4');
    const exists = fs.existsSync(videoPath);
    const fileSize = exists ? (fs.statSync(videoPath).size / 1024 / 1024).toFixed(2) : 0;

    const html = `
<!DOCTYPE html>
<html>
<head>
  <title>Sangeet Invitation Video</title>
  <style>
    body {
      font-family: 'Cormorant Garamond', serif;
      background: linear-gradient(135deg, #1b2a5b, #0b1230);
      color: #f3ead3;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
      padding: 20px;
    }
    .container {
      max-width: 800px;
      text-align: center;
    }
    h1 {
      font-size: 48px;
      margin-bottom: 10px;
      text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    .status {
      margin: 20px 0;
      padding: 20px;
      background: rgba(255,255,255,0.1);
      border-radius: 8px;
      backdrop-filter: blur(10px);
    }
    .video-container {
      margin: 30px 0;
      background: #000;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }
    video {
      width: 100%;
      max-width: 600px;
      display: block;
      margin: 0 auto;
    }
    .download-link {
      display: inline-block;
      padding: 14px 28px;
      margin: 10px;
      background: linear-gradient(135deg, #c99a4b, #e7c27a);
      color: #1b2a5b;
      text-decoration: none;
      border-radius: 999px;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      font-size: 14px;
      cursor: pointer;
      border: none;
      transition: all 0.3s ease;
      box-shadow: 0 8px 20px rgba(201, 154, 75, 0.3);
    }
    .download-link:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 30px rgba(201, 154, 75, 0.5);
    }
    .file-info {
      font-size: 14px;
      color: #d9d894;
      margin-top: 15px;
    }
    .loading {
      color: #d9d894;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🎉 Sangeet Invitation</h1>
    <div class="status">
      ${exists ? `
        <p style="color: #d9d894; font-size: 18px; margin: 0;">✓ Video Ready!</p>
        <div class="video-container">
          <video controls>
            <source src="/download" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </div>
        <div class="file-info">
          File Size: <strong>${fileSize} MB</strong>
        </div>
        <div style="margin-top: 20px;">
          <a href="/download" class="download-link">Download Video</a>
        </div>
      ` : `
        <p class="loading">⏳ Generating video...</p>
        <p>This may take a few minutes. Refresh to check status.</p>
      `}
    </div>
  </div>
</body>
</html>
    `;

    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(html);
  }
  else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

server.listen(PORT, () => {
  console.log(`\n🎬 Sangeet Invitation Video Server`);
  console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
  console.log(`Server running at: http://localhost:${PORT}`);
  console.log(`Preview: http://localhost:${PORT}/preview`);
  console.log(`Download: http://localhost:${PORT}/download`);
  console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);
});

process.on('SIGINT', () => {
  console.log('\nServer stopped.');
  process.exit(0);
});
