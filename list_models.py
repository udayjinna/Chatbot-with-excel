import google.generativeai as genai

genai.configure(GEMINI_API_KEY = "AIzaSyBm7Bpq3iVK3G4BEmrWiMBlkr-JvLebX0A")  # Replace with your actual API key

for m in genai.list_models():
    print(m.name, "→", m.supported_generation_methods)
