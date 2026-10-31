/**
 * MediCare Plus - Hospital Appointment & Status Tracking Web Server
 * Pure Node.js HTTP Server - Zero external dependencies required.
 * Runs instantly on VS Code via:
 *   node server.js
 *   or
 *   npm start
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = process.env.PORT || 3000;
const PUBLIC_DIR = __dirname;

const MIME_TYPES = {
  '.html': 'text/html; charset=UTF-8',
  '.css': 'text/css; charset=UTF-8',
  '.js': 'application/javascript; charset=UTF-8',
  '.json': 'application/json; charset=UTF-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf'
};

const server = http.createServer((req, res) => {
  // Normalize URL to prevent directory traversal
  const parsedUrl = url.parse(req.url);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  if (pathname === '/' || pathname === '') {
    pathname = '/index.html';
  }

  const filePath = path.join(PUBLIC_DIR, path.normalize(pathname).replace(/^(\.\.[\/\\])+/, ''));

  // Security check: ensure path is within PUBLIC_DIR
  if (!filePath.startsWith(PUBLIC_DIR)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      // 404 Not Found
      res.writeHead(404, { 'Content-Type': 'text/html; charset=UTF-8' });
      res.end(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>404 Not Found - MediCare Plus</title>
          <style>
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f0f7ff; color: #0a2540; text-align: center; padding: 50px 20px; }
            .box { max-width: 500px; margin: 0 auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(10,37,64,0.08); border-top: 6px solid #0284c7; }
            h1 { color: #0284c7; font-size: 28px; margin-bottom: 12px; }
            p { color: #475569; font-size: 16px; margin-bottom: 24px; }
            a { display: inline-block; background: #0284c7; color: white; text-decoration: none; padding: 12px 24px; border-radius: 6px; font-weight: 600; }
            a:hover { background: #0369a1; }
          </style>
        </head>
        <body>
          <div class="box">
            <h1>Page Not Found</h1>
            <p>The requested file <code>${pathname}</code> was not found on the server.</p>
            <a href="/">Return to MediCare Plus Home</a>
          </div>
        </body>
        </html>
      `);
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    // Add caching headers for static assets
    const headers = {
      'Content-Type': contentType,
      'Access-Control-Allow-Origin': '*'
    };

    if (ext === '.html') {
      headers['Cache-Control'] = 'no-cache';
    } else {
      headers['Cache-Control'] = 'public, max-age=3600';
    }

    res.writeHead(200, headers);
    const readStream = fs.createReadStream(filePath);
    readStream.pipe(res);
  });
});

server.listen(PORT, () => {
  console.log('====================================================');
  console.log('  MediCare Plus Hospital Portal is Running!');
  console.log(`  Local Server URL : http://localhost:${PORT}`);
  console.log(`  Theme            : Blue & White Modern Healthcare`);
  console.log('  Press Ctrl + C to stop the server.');
  console.log('====================================================');
});
