import sys
import time

COLORS = {"cyan": "\033[96m", "red": "\033[1;91m", "reset": "\033[0m"}


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
    ("Em là ai từ đâu bước đến", 3.5, 0, 0.1, "red"),
    ("Nơi đây dịu dàng chân phương", 0.0, 0, 0.1, "cyan"),
    ("Em là ai tựa như ánh nắng", 0.8, 0.4, 0.08, "red"),
    ("Ban mai ngọt ngào trong sương", 0.2, 1.4, 0.07, "cyan"),
    ("Ngắm em thật lâu", 0.1, 0.8, 0.14, "red"),
    ("Con tim anh yếu mềm", 0.2, 1.3, 0.08, "cyan"),
    ("Đắm say từ phút đó", 0.1, 0.7, 0.08, "red"),
    ("Từng giây trôi yêu thêm...", 0.1, 1.1, 0.08, "cyan"),
]


def main():
    setup()

    try:
        # Hiển thị tiêu đề
        display("  ")
        print()

        for line in lyrics:
            display(*line)
        print("\n🎵 Hoàn thành! 🎵")
    except KeyboardInterrupt:
        print("\n\nDừng phát!")


if __name__ == "__main__":
    main()
