from zalo_tts import ZaloTTS
import re

your_api_key = ""

text="Xin chào, tôi là clone Text-to-Speech được thực hiện bởi nhóm 13"

letters_only = re.sub("[^a-zA-Z]",  # Search for all non-letters
                          " ",          # Replace all non-letters with spaces
                          str(text))


def demo(text):
    tts = ZaloTTS(speaker=ZaloTTS.SOUTH_MEN, api_key=your_api_key)
    tts.text_to_speech(text)


if __name__ == "__main__":
    demo(text)