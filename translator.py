import streamlit as st
import boto3

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
  target_language = st.selectbox("Select target language", ["en","hi","te","fr","es","de"])  # Add more languages as needed

  if st.button("Translate"):
    translated_text = translate_text(text_input, target_language)
    st.success(f"Translated text: {translated_text}")

if __name__ == "__main__":
  main()
