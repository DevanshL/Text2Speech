# Text2Speech Application

This is a Streamlit application that converts text input into audio using Google Text-to-Speech (gTTS) library. It supports multiple languages for input and output, and allows users to choose different English accents. Users can also upload a text file to be converted into audio.

## Features

- Convert text input into audio
- Support for multiple input and output languages
- Option to select different English accents
- File upload functionality to convert text files into audio
- Character count display
- Clear output fields

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- Streamlit
- googletrans
- gTTS

You can install the required dependencies using pip:
```pip install streamlit googletrans gTTS```

## Usage

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the Streamlit application using the following command:
   ```streamlit run app.py```
4. The application will open in your default web browser.
5. Enter the text you want to convert in the input area, or upload a text file.
6. Select the input and output languages from the dropdown menus.
7. If the output language is English, you can choose the desired accent.
8. Click the "Convert" button to generate the audio.
9. The audio will play automatically, and the converted text will be displayed in the output area.
10. Use the "Clear" button to reset the ioutput field.

## Configuration

You can customize the application by modifying the following variables in the `app.py` file:

- `img`: Path to the local image used for the sidebar background.
- `page_bg_img`: URL or path to the background image for the main content area.
- `audio_file_path`: Directory path for saving the generated audio files.

## Future Enhancements

- Option to select gender (male or female) for the audio output.
- Ability to download the generated audio files.
- Support for additional audio formats (e.g., WAV, OGG).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Streamlit](https://streamlit.io/) - The Python library used for building the application.
- [googletrans](https://py-googletrans.readthedocs.io/en/latest/) - The Python library used for text translation.
- [gTTS](https://github.com/pndurette/gTTS) - The Python library used for text-to-speech conversion.
