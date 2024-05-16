import streamlit as st
from googletrans import Translator
import base64
from gtts import gTTS
import os
from pathlib import Path
from datetime import datetime, timedelta

# Function to convert image to base64
def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convert your local image to base64
#img = get_img_as_base64("/home/devansh/Documents/text-to-speech/Images/lufyy.png")
#
#page_bg_img = f'''
#<style>
#[data-testid="stAppViewContainer"] > .main {{
#background-image: url("https://ideogram.ai/api/images/direct/ByKFpaNIQCOLNV1lvpa1rg.png");
#background-size: cover;
#background-position: top left;
#background-repeat: no-repeat;
#background-attachment: local;
#}}
#
#[data-testid="stSidebar"] > div:first-child {{
#background-image: url("data:image/png;base64,{img}");
#background-size: fit;
#background-position: center; 
#background-repeat: no-repeat;
#background-attachment: fixed;
#}}
#
#[data-testid="stHeader"] {{
#background: rgba(0,0,0,0);
#}}
#
#[data-testid="stToolbar"] {{
#right: 2rem;
#}}
#
#/* Custom CSS for input_area */
#div[data-testid="stText"] > div > div > div:nth-child(1) > div > div > textarea {{
#    background-color: transparent !important;
#    color: black !important;
#    font-weight: bold !important;
#}}
#</style>
#'''
#
#st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='color: white; font-weight:bold'>Text to Speech</h1>", unsafe_allow_html=True)

translator = Translator()

# File Upload/Download Options
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
if uploaded_file is not None:
    file_contents = uploaded_file.read().decode("utf-8")
    st.session_state["input_text"] = file_contents

if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""

input_area = st.text_area("Enter Your text:", value=st.session_state["input_text"], height=100, key='input_text')

# Character count
char_count = len(st.session_state["input_text"])
st.write(f'<span style="color:green; font-weight:bold;font-size:20px;">Character Count: {char_count}</span>', unsafe_allow_html=True)

# Language selection with default values
in_lang = st.selectbox("Select the input language",
    ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese",
     "Spanish", "French", "German", "Italian", "Portuguese", "Russian",
     "Arabic", "Turkish", "Dutch", "Greek", "Swedish", "Norwegian",
     "Danish", "Finnish", "Polish", "Czech", "Hungarian", "Romanian",
     "Thai", "Vietnamese", "Indonesian"),
    index=0)  # Default is "English"

in_lang_code = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Swedish": "sv",
    "Norwegian": "no",
    "Danish": "da",
    "Finnish": "fi",
    "Polish": "pl",
    "Czech": "cs",
    "Hungarian": "hu",
    "Romanian": "ro",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id"
}[in_lang]

out_lang = st.selectbox("Select the output language",
    ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese",
     "Spanish", "French", "German", "Italian", "Portuguese", "Russian",
     "Arabic", "Turkish", "Dutch", "Greek", "Swedish", "Norwegian",
     "Danish", "Finnish", "Polish", "Czech", "Hungarian", "Romanian",
     "Thai", "Vietnamese", "Indonesian"),
    index=0)  # Default is "English"

out_lang_code = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Swedish": "sv",
    "Norwegian": "no",
    "Danish": "da",
    "Finnish": "fi",
    "Polish": "pl",
    "Czech": "cs",
    "Hungarian": "hu",
    "Romanian": "ro",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id"
}[out_lang]

english_accent = st.selectbox(
    "Select your English accent",
    (
        "Default",
        "India",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "Ireland",
        "South Africa",
    ),
    index=0  # Default is "Default"
)

tld = {
    "Default": "com",
    "India": "co.in",
    "United Kingdom": "co.uk",
    "United States": "com",
    "Canada": "ca",
    "Australia": "com.au",
    "Ireland": "ie",
    "South Africa": "co.za"
}[english_accent]

def text2speech(in_lang, out_lang, text, tld):
    translation = translator.translate(text, src=in_lang, dest=out_lang)
    translated_text = translation.text

    # using GOOGLE TEXT TO SPEECH for language code
    lang_code = out_lang if out_lang != "Chinese" else "zh"

    # Generate Text to speech
    tts = gTTS(translated_text, lang=lang_code, tld=tld, slow=False, lang_check=False)

    try:
        my_file = text[0:300]  # first 300 characters
    except:
        my_file = 'audio'

    audio_file_path = f'/home/devansh/Documents/text-to-speech/Example/{my_file}.mp3'
    tts.save(audio_file_path)
    
    return audio_file_path, translated_text

st.markdown("<h2 style='color: green; font-weight:bold'>Load Saved Audio</h2>", unsafe_allow_html=True)

saved_audio_dir = '/home/devansh/Documents/text-to-speech/Example'
audio_files = [f for f in os.listdir(saved_audio_dir) if f.endswith('.mp3')]

selected_audio_file = st.selectbox("Select an audio file to play", audio_files)
if selected_audio_file:
    audio_file_path = os.path.join(saved_audio_dir, selected_audio_file)
    audio_file = open(audio_file_path, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

three_days_ago = datetime.now() - timedelta(days=3)
for file in audio_files:
    file_path = os.path.join(saved_audio_dir, file)
    if os.path.isfile(file_path):
        creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
        if creation_time < three_days_ago:
            os.remove(file_path)
            st.write(f"Deleted {file} because it was older than 3 days.")

col1, col2 = st.columns([2, 1])
with col1:
    if st.button("Convert"):
        if st.session_state["input_text"]:
            # Generate audio
            audio_file_path, out_text = text2speech(in_lang_code, out_lang_code, st.session_state["input_text"], tld)
            audio_file = open(audio_file_path, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.text_area("Converted Language:", value=out_text, height=100, key='output_text')

with col2:
    if st.button("Clear"):
        st.session_state['output_text'] = ''
        st.experimental_rerun()

