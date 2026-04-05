# Jarvis AI Assistant

## Description
A voice-controlled AI assistant that listens and talks back using speech recognition and OpenAI's GPT models.

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/kenjidotvom/jarvis-ai.git
cd jarvis-ai
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Set Up Your OpenAI API Key
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and replace `your_key_here` with your actual OpenAI API key
3. Get your API key from: https://platform.openai.com/api-keys

### 5. Run Jarvis
```bash
python jarvis.py
```

## Required Packages
- **openai** - OpenAI API client
- **speechrecognition** - Speech recognition library
- **pyaudio** - Audio input/output
- **python-dotenv** - Environment variable management
- **playsound** - Audio playback
- **requests** - HTTP library

## Features
- 🎤 Voice recognition using Google Speech API
- 🤖 AI-powered responses with OpenAI GPT
- 🔊 Text-to-speech audio output
- ⏰ Time announcements
- 💬 Natural conversation capabilities

## Future Plans
- 🎙️ **Voice Upgrade** - Enhanced voice quality and accent options
- 🥧 **Raspberry Pi Support** - Run Jarvis on embedded systems
- 🎧 **Earbuds Integration** - Wireless audio device support

## Troubleshooting
- Make sure your microphone is connected and working
- Verify your OpenAI API key is valid
- Check internet connection for Google Speech API
- Install PyAudio dependencies if issues occur

## License
MIT License
