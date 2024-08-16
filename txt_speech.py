





import io
import streamlit as st
import time
import requests
from PIL import Image
from io import BytesIO
import boto3
import json
import base64
import io
from gtts import gTTS
import autoplay

from keys import ACCESS_KEY, REGION_NAME, SECRET_KEY




def text_to_speech(text_prompt):
  """Converts text to speech using gTTS and returns the audio data."""
  tts = gTTS(text=text_prompt, lang='en')  # Change 'en' for your desired language
  audio_data = io.BytesIO()
  tts.write_to_fp(audio_data)
  audio_data.seek(0)
  return audio_data.read()












# Initialize Polly client
polly = boto3.client(
    "polly",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION_NAME,
)


def convert_text_to_speech(text, voice_id):
    """Converts text to speech using Amazon Polly"""

    try:
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId=voice_id,
        )
        
        if "AudioStream" in response:
            # Access the audio stream
            with (response["AudioStream"]) as stream:
                audio_bytes = stream.read()

            return audio_bytes
        else:
            return None

    except Exception as e:
        print(f"Error converting text to speech: {e}")
        return None
