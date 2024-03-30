Demo TTS bằng zalotts

Yêu cầu: Đã cài đặt phiên bản Python 3.8 và tạo môi trường venv

1. Thực hiện install các thư viện
    - Các thư viện cần thiết cho bản Demo này là: pyaudio, python-dotenv
    - Câu lệnh install: pip install pyaudio
                        pip install python-dotenv

    Lưu ý: Nếu như muốn cài nhanh các thư viện có thể install như sau: pip install -r requirements.txt

2. Chạy Demo
    B1: Truy cập vào trang web https://zalo.ai/products/text-to-audio-converter và đăng nhập, sau đó thực hiện lấy api key
        tại Account -> Manage Keys và bỏ vào biến your_api_key trong demo_zalotts.py
    B2: Thêm đoạn văn bản bạn muốn chuyển từ văn bản sang giọng nói ở biến text
    B3: Tại phần speaker bạn có thể thay đổi người đọc theo bảng sau:
        ID	Name	        Constant
        1	South women	    ZaloTTS.SOUTH_WOMEN
        2	Northern women	ZaloTTS.NORTHERN_WOMEN
        3	South men	    ZaloTTS.SOUTH_MEN
        4	Northern men	ZaloTTS.NORTHERN_MEN
    B4: Cuối cùng chỉ việc run Demo và nghe đoạn văn bản được chuyển thành giọng nói