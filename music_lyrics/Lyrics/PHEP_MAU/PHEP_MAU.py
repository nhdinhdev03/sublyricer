import sys
import time

COLORS = {
    "cyan": "\033[96m",
    "red": "\033[1;91m",
    "reset": "\033[0m"
}

def setup():
    pass

def color_text(text, color="cyan"):

    return COLORS.get(color, COLORS["cyan"]) + text + COLORS["reset"]

def display(text, delay_before=0, delay_after=0, char_speed=0.05, color="cyan"):
    time.sleep(delay_before)
    for char in text:
        sys.stdout.write(color_text(char, color))
        sys.stdout.flush()
        time.sleep(char_speed)
    print()
    time.sleep(delay_after)

lyrics = [
    ("Thiếu em tôi sợ bơ vơ", 0.2, 1.48, 0.08, "red"),
    ("Vắng em như tàn cơn mơ", 0.1, 1.42, 0.07, "cyan"),
    ("Chẳng phải phép màu", 0.1, 0.68, 0.08, "cyan"),
    ("Vậy sao chúng ta gặp nhau", 0.2, 2.3, 0.07, "red"),
    ("Một người khẽ cười", 0.1, 0.84, 0.08, "cyan"),
    ("Người kia cũng dịu nỗi đau", 0.1, 2.3, 0.07, "cyan"),
    ("Gọi tôi thức giấc cơn ngủ mê", 0.1, 1.46, 0.08, "cyan"),
    ("Dìu tôi đi lúc quên lối về", 0.1, 1.05, 0.08, "cyan"),
    ("Quãng đời mai sau", 0.1, 2.4, 0.07, "cyan"),
    ("LUÔN CẠNH NHAU", 0.1, 1.8, 0.07, "red"),
]

def main():
    setup()

    try:
        # Hiển thị tiêu đề
        display("🎵 PHÉP MÀU 🎵")
        print()
    
        for line in lyrics:
            display(*line)
        print("\n🎵 Hoàn thành! 🎵")
    except KeyboardInterrupt:
        print("\n\nDừng phát!")

if __name__ == "__main__":
    main()
