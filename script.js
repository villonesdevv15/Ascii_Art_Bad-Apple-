// Configuration
const ASCII_CHARS = ' $8obdpq0L@n1+"`';
const VIDEO_PATH = 'assets/Bad_apple!!.mp4';
const AUDIO_PATH = 'assets/Bad_apple!!.mp3';
const OUTPUT_WIDTH = 150; // Reduced for better performance
const FPS = 30;

// DOM elements
const asciiArt = document.getElementById('ascii-art');

// Create hidden video element
const video = document.createElement('video');
video.src = VIDEO_PATH;
video.crossOrigin = 'anonymous';
video.preload = 'auto';
video.playsInline = true;

// Create audio element
const audio = new Audio(AUDIO_PATH);
audio.preload = 'auto';
audio.volume = 1.0;

// Create canvas for processing
const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');

// Animation control
let animationId = null;
let lastFrameTime = 0;
const frameDelay = 1000 / FPS;

function frameToAscii(frame) {
    const aspectRatio = frame.videoWidth / frame.videoHeight;
    const newHeight = Math.floor(OUTPUT_WIDTH / aspectRatio * 0.5);
    
    canvas.width = OUTPUT_WIDTH;
    canvas.height = newHeight;
    ctx.drawImage(frame, 0, 0, OUTPUT_WIDTH, newHeight);
    
    const imageData = ctx.getImageData(0, 0, OUTPUT_WIDTH, newHeight);
    const pixels = imageData.data;
    let asciiFrame = '';
    
    for (let y = 0; y < newHeight; y++) {
        for (let x = 0; x < OUTPUT_WIDTH; x++) {
            const idx = (y * OUTPUT_WIDTH + x) * 4;
            const gray = 0.299 * pixels[idx] + 0.587 * pixels[idx+1] + 0.114 * pixels[idx+2];
            const charIndex = Math.min(Math.floor(gray / 25), ASCII_CHARS.length - 1);
            asciiFrame += ASCII_CHARS[charIndex];
        }
        asciiFrame += '\n';
    }
    
    return asciiFrame;
}

function animate(timestamp) {
    if (!lastFrameTime) lastFrameTime = timestamp;
    const elapsed = timestamp - lastFrameTime;
    
    if (elapsed > frameDelay) {
        if (video.paused || video.ended) return;
        
        asciiArt.textContent = frameToAscii(video);
        lastFrameTime = timestamp - (elapsed % frameDelay);
    }
    
    animationId = requestAnimationFrame(animate);
}

async function startPlayback() {
    try {
        // Start video and audio together
        await Promise.all([video.play(), audio.play()]);
        animationId = requestAnimationFrame(animate);
        asciiArt.textContent = "Bad Apple!! set to 150% width. Click to play";
    } catch (err) {
        asciiArt.textContent = "Bad Apple!! failed to load. Click to retry.";
        document.addEventListener('click', startPlayback, { once: true });
    }
}

// Initialize when ready
video.addEventListener('canplaythrough', () => {
    asciiArt.textContent = "Loading Bad Apple!!... Click to play";
    document.addEventListener('click', startPlayback, { once: true });
});

// Error handling
video.addEventListener('error', () => {
    asciiArt.textContent = `Video error: ${video.error.message}`;
});

audio.addEventListener('error', () => {
    asciiArt.textContent = `Audio error: ${audio.error.message}`;
});