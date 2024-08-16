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

from dd import translate_text
from txt_image import generate_image
from txt_speech import convert_text_to_speech
from txt_summarizer import get_response


def main():
    # Title and header
    st.set_page_config(page_title="VISOR", layout="wide")
    st.header(" VISOR: Make the Task Easier with AI")

    # Text summarization section (expandable)
    text_area = st.text_area("Enter your text to summarize:")
    summary = get_response(text_area)
    with st.expander("Summarize Your Text ", expanded=True):

        if st.button("Summarize"):
            if summary:
                st.write("Please Copy the Summary so u can hear in your Comfortable Language")
                st.success("Here's your summary")
                st.write(summary)
            else:
                st.error("Error summarizing text. Please try again.")

    # Text-to-speech section (expandable)
    with st.expander("Generate Artwork", expanded=False):
        prompt_text = text_area
        art_style = st.selectbox("Choose an Image Style", [
            "Abstract", "Cute", "Fantasy", "Futuristic", "Realistic",
            "Science Fiction", "Surreal", "Techno"
        ])
        st.subheader("Your artwork will take a moment. Please be patient.")
        if st.button("Generate Artwork"):
            artwork_image = generate_image(prompt_text, art_style)
            if artwork_image:
                st.image(artwork_image, width=400)
            else:
                st.error("Error generating image. Please try again.")



    s_text = summary  # Placeholder for summarized text
    text_list = list(s_text)  # Convert the generator to a list
    s_text = " ".join(text_list)
    
    with st.expander("Listen to Your Summarized Text", expanded=False):
        summarized_text = s_text
        voice_select = st.selectbox("Select Voice", ["Joanna", "Matthew", "Emma"], key="voice_for_summary")  # Add unique key
        speech_bytes = convert_text_to_speech(summarized_text, voice_select)
        if speech_bytes:
            st.audio(speech_bytes, format="audio/mpeg")
        else:
            st.error("Error converting text to speech")

    with st.expander("Listen in your own language", expanded=False):
        text_to_l=st.text_area("Please  paste the Summary here that you got Above form summarize box  to listen in our preffered language")
        target_language = st.selectbox("Select target language", ["en", "hi", "te", "fr", "es", "de"], key="target_language_select")  # Add unique key
       
        if st.button("Translate"):
            translated_text = translate_text(text_to_l, target_language)
            select_voice = st.selectbox("Select Voice", ["Joanna", "Matthew", "Emma"], key="voice_for_translation")  # Add unique key
            speech_bytes = convert_text_to_speech(translated_text, select_voice)
            if speech_bytes:
                st.audio(speech_bytes, format="audio/mpeg")
            else:
                st.error("Error converting text to speech")


if __name__ == "__main__":
    main()
