from elevenlabs.client import ElevenLabs
import elevenlabs
from playsound import playsound


# Khởi tạo client với API key của bạn, các file âm thanh được tạo sẽ được upload lên web
# https://elevenlabs.io/app/speech-synthesis
client = ElevenLabs(api_key="8562511af55f1ba2000e03ed2289cb78")


# Văn bản muốn chuyển sang giọng nói
text_to_speech = ("Hello, I am a Text-to-Speech clone made by team 13")


# Chỉnh sửa giọng nói
voice_tts = elevenlabs.Voice(
    voice_id="SOYHLrjzK2X1ezoPC6cr", # voice_id người đọc
    settings=elevenlabs.VoiceSettings(
        # stability=0, #sự ổn định
        # similarity_boost=0.5 #trầm - cao
    )
)


def tts_elevenlabs_test(text):
    # Tạo giọng nói từ văn bản
    audio = client.generate(text=text, voice=voice_tts)

    # Lưu âm thanh vào tệp MP3
    elevenlabs.save(audio, "sounds/audio_elevenlabs.mp3")

    # Chạy file âm thanh vừa được tạo
    playsound("sounds/audio_elevenlabs.mp3", True)


if __name__ == "__main__":
    tts_elevenlabs_test(text_to_speech)