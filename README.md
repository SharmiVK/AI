# Voice Assistant with Google Gemini & gTTS

This project is a simple **AI-powered voice assistant** built using:
- [Google Generative AI (Gemini)](https://ai.google.dev)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [playsound](https://pypi.org/project/playsound/)

It takes **user input from the terminal**, sends it to Gemini for a response, then converts the reply into **speech output**.

---

## 🚀 Features
- Converses with Google Gemini (`gemini-1.0-pro-latest`).
- Converts AI responses into **speech** using gTTS.
- Plays the generated audio instantly.
- Designed for **short, factual, assistant-style replies**.

---

## 📦 Requirements
Install dependencies with:

```bash
pip install google-generativeai gTTS playsound
