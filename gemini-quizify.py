import vertexai;
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Content, ChatSession,Tool

project = "gemini-quizify-416617"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.4
)

#load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)
chat = model.start_chat()