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
    ("Nơi đâu cho em thật sự yên lành", 0, 0, 0.1, "red"),
    ("Và ai đó mang em đi xa dần lắng nghe tim anh đôi lần", 0.0, 0, 0.1, "cyan"),
    ("Xót xa khi em không cần mình gần bên nhau", 0, 1.4, 0.07, "red"),
    ("Vì thời gian sẽ không trôi êm đềm giống như khi đôi môi mềm", 0.1, 0.8, 0.14, "cyan"),
    ("Còn ấm đam mê như ban đầu để miền yêu thương khép lại", 0, 0.7, 0.08, "red"),
    ("Uhhh anh đã cố nói em khi bên anh chỉ là mộng ước", 0, 0.8, 0.06, "cyan"),
    ("Nguội lạnh theo hơi ấm nhạt màu", 0, 0.5, 0.08, "red"),
    ("(Lạnh theo hơi ấm nhạt màu)", 0, 0.3, 0.08, "cyan"),
    ("Nguội lạnh theo hơi ấm nhạt màu", 0, 0.5, 0.08, "red"),
    ("(eh y-yeh y-yeh huh)", 0, 1.0, 0.1, "cyan"),
]


def main():
    setup()

    try:
        # Hiển thị tiêu đề
        display("  ")
        print()

        for line in lyrics:
            display(*line)
        print("\n🎵 Hoàn thành! ")
    except KeyboardInterrupt:
        print("\n\nDừng phát!")


if __name__ == "__main__":
    main()
