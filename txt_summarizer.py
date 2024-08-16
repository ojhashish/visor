
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

api_endpoint = "https://ui6wghph64yqexouqa3ofr42mm0lnrwt.lambda-url.us-east-1.on.aws/"

def get_response(text):
    payload = {

        "prompt": f"{text}"
    }

    response = requests.post(api_endpoint, json = payload)
    print(f"response status:: {response.status_code}")
    response_text = response.text
  
    # For streaming like behavior
    for word in response_text.split():
        yield word + " "
        time.sleep(0.1)
    