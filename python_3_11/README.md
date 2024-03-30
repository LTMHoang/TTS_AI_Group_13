Demo TTS bằng elevenlabs và gtts

Yêu cầu: Đã cài đặt phiên bản Python 3.11 hoặc cao hơn và tạo môi trường venv

1. Thực hiện install các thư viện
    - Các thư viện cần thiết cho bản Demo này là: elevenlabs, gtts, playsound
    - Câu lệnh install: pip install elevenlabs
                        pip install gtts
                        pip install playsound

    Lưu ý: Nếu như muốn cài nhanh các thư viện có thể install như sau: pip install -r requirements.txt

2. Chạy Demo
    2.1 Demo elevenlabs
        B1: Truy cập vào trang web https://elevenlabs.io/app/speech-synthesis, đăng nhập để lấy api_key ở phần
            Profile + API key và bỏ vào biến your_api_key trong demo_elevenlabs.py
        B2: Thêm đoạn văn bản bạn muốn chuyển từ văn bản sang giọng nói ở biến text_to_speech
        B3: Bạn có thể điều chỉnh giọng người đọc dựa vào file VOICE_ID.txt và một số thông số khác ở phần settings
        B4: Cuối cùng chỉ việc run Demo và nghe đoạn văn bản được chuyển thành giọng nói

    2.2 Demo gtts
        Với Demo này bạn chỉ cần thêm đoạn văn bản bạn muốn chuyển từ văn bản sang giọng nói ở biến text trong demo_gtts,
        sau đó run Demo và nghe đoạn văn bản được chuyển thành giọng nói.