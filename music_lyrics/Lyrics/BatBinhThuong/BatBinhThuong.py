import sys
import time

COLORS = {
    "cyan": "\033[96m",
    "red": "\033[1;91m",
    "yellow": "\033[1;93m",
    "reset": "\033[0m",
}
def setup():
    pass


def color_text(text, color="cyan"):

    return COLORS.get(color, COLORS["cyan"]) + text + COLORS["reset"]
def display(text, delay_after=0, char_speed=0.05, color="cyan"):
    for char in text:
        sys.stdout.write(color_text(char, color))
        sys.stdout.flush()
        time.sleep(char_speed)
    print()
    time.sleep(delay_after)


lyrics = [
    ("Và trong mơ anh hái bông hoa", 0.34, 0.07, "cyan"),
    ("Anh cài lên tóc em", 0.0, 0.09, "cyan"),
    ("Rồi nắm đôi tay của em", 0.9, 0.10, "cyan"),
    ("Nhạc vang lên theo trái tim anh từng nhịp", 0.10, 0.07, "cyan"),
    ("Bước đến bên em", 3, 0.10, "cyan"),
    ("Chợt anh như kẻ ngốc sau sưa nụ cười", 1.0, 0.07, "cyan"),
    ("Trên mắt em người nói những câu dịu êm", 0.8, 0.08, "cyan"),
    ("Chẳng một ai đánh thuế giấc mơ nên sợ", 0.1, 0.08, "cyan"),
    ("Chi cứ mơ mộng...", 3, 0.15, "red"),
]


def main():
    setup()
    print(color_text("     "))
    try:

        for line in lyrics:

            display(*line)
        print("\nHoàn thành! ")
    except KeyboardInterrupt:
        print("\n\nDừng phát!")


if __name__ == "__main__":
    main()
