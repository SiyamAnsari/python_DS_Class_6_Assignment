import streamlit as st
import speech_recognition as sr
from googletrans import Translator

# Create a Streamlit web app
st.title("NED-PGD Project Audio-to-Audio and Text-to-Text Translation Web App")

# Option to select translation direction
translation_option = st.radio("Translation Direction:", ("Audio to Text", "Text to Text"))

if translation_option == "Audio to Text":
    # Upload an audio file
    audio_file = st.file_uploader("Upload an audio file (MP3 or WAV)", type=["mp3", "wav"])

    if audio_file:
        recognizer = sr.Recognizer()

        # Recognize the audio
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        # Recognize speech using Google Web Speech API
        try:
            st.write("Transcribed Text:")
            transcribed_text = recognizer.recognize_google(audio_data)
            st.write(transcribed_text)
        except sr.UnknownValueError:
            st.write("Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            st.write(f"Could not request results from Google Speech Recognition service; {e}")

else:
    # Text input for translation
    text_input = st.text_area("Enter text for translation:")

    if text_input:
        target_language = st.selectbox("Select the target language:", ["en", "es", "fr", "de", "zh", "ur"])

        # Translate the input text
        translator = Translator()
        translation = translator.translate(text_input, dest=target_language)

        st.write(f"Original Text ({translation.src}):")
        st.write(text_input)
        st.write(f"Translation ({translation.dest}):")
        st.write(translation.text)

# Display a message about limitations
st.info("Note that this is a simplified example. For more accurate results, consider using commercial APIs like Google Cloud or others.")
