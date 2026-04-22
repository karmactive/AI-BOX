# Sangeet Wedding Invitation Video

This project converts the animated Sangeet wedding invitation design into an MP4 video file.

## Project Overview

The original design is an HTML/CSS/JavaScript animated invitation featuring:
- **Duration**: 10 seconds
- **Resolution**: 708 × 1000 px
- **Framerate**: 30 fps
- **Format**: MP4 (H.264/AVC video codec, AAC audio)

## Animation Sequence

The invitation animation includes:
1. **0-3s**: Vine borders draw in from the sides with leaf/bud/lotus elements blooming
2. **1.1-1.3s**: Scalloped arch card fades in with a subtle scale effect
3. **1.9s**: Lotus crest appears and gently bobs
4. **2.3-4.4s**: Text reveals in sequence:
   - "We are thrilled..." (small intro text)
   - "Sangeet" (large script with shimmer effect)
   - "To celebrate the wedding of"
   - "Vishad" (large script)
5. **5.3-5.7s**: Date and time details appear
6. **6.1-7.0s**: Gold divider with center dots draws in
7. **6.8-7.4s**: Venue information and "Dinner to Follow" appear
8. **Throughout**: Floating rose petals drift downward; sparkles twinkle on the indigo borders

## Color Palette

- **Indigo**: #1b2a5b (main background)
- **Cream**: #f3ead3 (card background)
- **Gold**: #c99a4b (accent/borders)
- **Olive**: #5a6b2f (text)
- **Rose**: #d89aa6 (petals)
- **Leaf**: #7fae5a (vine foliage)

## Files

- `sangeet-invite.html` - Original animated invitation design
- `generate_video.js` - Script to render HTML animation and encode to MP4
- `sangeet-invitation.mp4` - Final video output
- `server.js` - Simple HTTP server for video preview and download
- `frames/` - Temporary directory containing captured frame PNGs (300 frames @ 30fps)

## Generation Process

The video generation uses:

1. **Puppeteer** - Headless browser automation to render HTML
2. **FFmpeg** - Video encoding from PNG frames to MP4

### Steps:
1. HTML is rendered frame-by-frame in a headless browser
2. Each frame is captured as PNG (708×1000, 30fps for 10 seconds = 300 frames)
3. Frames are encoded to H.264 MP4 using FFmpeg with:
   - Bitrate optimization
   - YUV420p color space (web-compatible)
   - Medium encoding preset

## Download

Once generated, the MP4 file can be:
- Downloaded directly
- Previewed in a browser
- Shared via email, messaging apps, or social media
- Embedded in web pages or presentations

## Technical Details

**Video Specifications:**
- Container: MP4 (MPEG-4 Part 14)
- Video Codec: H.264 (AVC)
- Resolution: 708 × 1000 pixels
- Framerate: 30 fps
- Duration: ~10 seconds
- Typical file size: 2-5 MB

**Browser Compatibility:**
- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support
- Mobile browsers: Full support

## Running the Server

To preview and download the video:

```bash
node server.js
```

Then visit: `http://localhost:3000/preview`

## Re-generating the Video

To regenerate the video (e.g., if HTML is modified):

```bash
node generate_video.js
```

This will:
1. Clear any existing frames
2. Capture new frames from the current HTML
3. Encode a new MP4 file, overwriting the previous one

The entire process typically takes 5-10 minutes depending on system performance.
