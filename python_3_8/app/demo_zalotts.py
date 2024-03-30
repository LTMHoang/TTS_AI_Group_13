from zalo_tts import ZaloTTS
import re

your_api_key = ""

text=("Xin chào, tôi là clone Text-to-Speech được thực hiện bởi nhóm 13")

letters_only = re.sub("[^a-zA-Z]",  # Search for all non-letters
                          " ",          # Replace all non-letters with spaces
                          str(text))


def demo(text):
    tts = ZaloTTS(speaker=ZaloTTS.NORTHERN_WOMEN, api_key=your_api_key)
    tts.text_to_audio(text, "sounds/audio_zalotts.mp3")
    tts.text_to_speech(text)


if __name__ == "__main__":
    demo(text)