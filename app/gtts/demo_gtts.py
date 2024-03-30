from gtts import gTTS
from playsound import playsound

# Chuỗi văn bản bạn muốn chuyển đổi thành giọng nói
text = "Xin chào, tôi là một phiên bản clone Text-to-Speech được thực hiện bởi nhóm 13"


def tts_gtts_test(text):
    # Tạo đối tượng gTTS và chuyển đổi văn bản thành giọng nói (sử dụng ngôn ngữ Vietnamese)
    tts = gTTS(text=text, lang='vi')

    # Lưu giọng nói vào file âm thanh
    tts.save("sounds/audio_gtts.mp3")

    # Chạy file âm thanh vừa lưu
    playsound("sounds/audio_gtts.mp3", True)


if __name__ == "__main__":
    tts_gtts_test(text)