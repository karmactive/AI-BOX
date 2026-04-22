const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const ffmpeg = require('fluent-ffmpeg');
const ffmpegStatic = require('ffmpeg-static');

ffmpeg.setFfmpegPath(ffmpegStatic);

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  page.setViewport({ width: 708, height: 1000 });

  // Read the HTML file
  const htmlPath = path.join(__dirname, 'sangeet-invite.html');
  const htmlContent = fs.readFileSync(htmlPath, 'utf-8');

  // Load HTML
  await page.setContent(htmlContent, { waitUntil: 'networkidle2' });

  // Create frames directory
  const framesDir = path.join(__dirname, 'frames');
  if (!fs.existsSync(framesDir)) {
    fs.mkdirSync(framesDir, { recursive: true });
  }

  // Clean up any existing frames
  fs.readdirSync(framesDir).forEach(file => {
    fs.unlinkSync(path.join(framesDir, file));
  });

  // Capture frames for 10 seconds at 30 fps
  const fps = 30;
  const duration = 10; // seconds
  const totalFrames = fps * duration;
  const frameInterval = 1000 / fps; // milliseconds

  console.log(`Capturing ${totalFrames} frames at ${fps} fps...`);

  for (let i = 0; i < totalFrames; i++) {
    await new Promise(resolve => setTimeout(resolve, frameInterval));

    const frameNumber = String(i).padStart(6, '0');
    const framePath = path.join(framesDir, `frame_${frameNumber}.png`);

    await page.screenshot({ path: framePath });

    if ((i + 1) % 30 === 0) {
      console.log(`Captured frame ${i + 1}/${totalFrames}`);
    }
  }

  await browser.close();

  console.log('Frames captured successfully!');
  console.log('Creating MP4 video...');

  const outputPath = path.join(__dirname, 'sangeet-invitation.mp4');
  const framesPattern = path.join(framesDir, 'frame_%06d.png');

  return new Promise((resolve, reject) => {
    ffmpeg()
      .input(framesPattern)
      .inputFPS(fps)
      .outputOptions([
        '-c:v libx264',
        '-pix_fmt yuv420p',
        '-preset medium'
      ])
      .output(outputPath)
      .on('progress', (progress) => {
        process.stdout.write(`\rEncoding: ${Math.round(progress.percent || 0)}%`);
      })
      .on('end', () => {
        console.log('\n✓ Video created successfully!');
        const fileSize = fs.statSync(outputPath).size;
        console.log(`File: ${outputPath}`);
        console.log(`Size: ${(fileSize / 1024 / 1024).toFixed(2)} MB`);
        resolve();
      })
      .on('error', (error) => {
        console.error('\n✗ Encoding error:', error.message);
        reject(error);
      })
      .run();
  });
})().catch(error => {
  console.error('Fatal error:', error.message);
  process.exit(1);
});
