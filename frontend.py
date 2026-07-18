import gradio as gr
import requests
API_URL = "https://multimodel-backend-1.onrender.com"

def analyze_meeting(image):

    if image is None:
        return "Please upload a meeting image.", "", ""

    with open(image, "rb") as f:
        files = {
            "file": f
        }

        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result = response.json()

        return (
            result["meeting_analysis"],
            
            result["sentiment"]
        )

    return "Error occurred!", "", ""


demo = gr.Interface(
    fn=analyze_meeting,
    inputs=gr.Image(type="filepath", label="Upload Meeting Image"),
    outputs=[
        gr.Textbox(label="Meeting Analysis", lines=12),
        
        gr.Textbox(label="Sentiment")
    ],
    title="🤖 AI Meeting Analyzer",
    description="Upload a meeting image to analyze participants, meeting summary, and sentiment."
)

import os

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
