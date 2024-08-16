import streamlit as st
import boto3
from txt_speech import convert_text_to_speech
from txt_summarizer import get_response

def translate_text(text, target_language):
  """Translates text to the specified target language using Amazon Translate."""
  translate = boto3.client('translate')
  response = translate.translate_text(
      Text=text,
      SourceLanguageCode='auto',
      TargetLanguageCode=target_language
  )
  return response['TranslatedText']

def main():
  st.title("Text Translator")

  text_input = st.text_area("Enter text to translate")
  sett = get_response(text_input)  # Assuming this doesn't need the translated text
  target_language = st.selectbox("Select target language", ["en","hi","te","fr", "es", "de"])# Add more languages as needed

  if st.button("Translate"):
    translated_text = translate_text(text_input, target_language)
    voice_select = st.selectbox("Select Voice", ["Joanna", "Matthew", "Emma"])
    speech_bytes = convert_text_to_speech(translated_text, voice_select)
    if speech_bytes:
      st.audio(speech_bytes, format="audio/mpeg")
    else:
      st.error("Error converting text to speech")

if __name__ == "__main__":
  main()
