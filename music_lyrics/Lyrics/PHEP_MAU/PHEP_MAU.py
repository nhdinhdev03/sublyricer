import sys
import time
import os
import atexit

def setup():
    """Quick setup - clear screen and hide cursor"""
    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.write("\x1b[?25l")
    atexit.register(lambda: sys.stdout.write("\x1b[?25h"))

def color_text(text):
    """Add color if available, fallback to plain text"""
    try:
        from termcolor import colored
        return colored(text, "cyan")
    except ImportError:
        return text


def display(text, delay_before=0, delay_after=0, char_speed=0.05):
    time.sleep(delay_before)

    for char in text:
        sys.stdout.write(color_text(char))
        sys.stdout.flush()
        time.sleep(char_speed)

    print()
    time.sleep(delay_after)


lyrics = [
    ("Thiếu em tôi sợ bơ vơ", 0.2, 1.48, 0.08),
    ("vắng em như tàn cơn mơ", 0.1, 1.42, 0.07),
    ("Chẳng phải phép màu", 0.1, 0.68, 0.08),
    ("vậy sao chúng ta gặp nhau", 0.2, 2.3, 0.07),
    ("Một người khẽ cười", 0.1, 0.84, 0.08),
    ("người kia cũng dịu nỗi đau", 0.1, 2.3, 0.07),
    ("Gọi tôi thức giấc cơn ngủ mê", 0.1, 1.46, 0.08),
    ("Dìu tôi đi lúc quên lối về", 0.1, 1.05, 0.08),
    ("Quãng đời mai sau", 0.1, 2.4, 0.07),
    ("LUÔN CẠNH NHAU", 0.1, 1.08, 0.07),
]


def main():
    setup()

    try:
        for line in lyrics:
            display(*line)
        print("\n🎵 Hoàn thành! 🎵")
    except KeyboardInterrupt:
        print("\n\nDừng phát!")


if __name__ == "__main__":
    main()
