import sys
import time

COLORS = {"cyan": "\033[96m", "red": "\033[1;91m", "reset": "\033[0m"}


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
    ("Nơi đâu cho em thật sự yên lành", 0.7, 0.05, "cyan"),
    ("Và ai đó mang em đi xa dần ", 0.6, 0.07, "red"),
    ("Lắng nghe tim anh đôi lần", 0.1, 0.06, "cyan"),
    ("Xót xa khi em không cần mình gần bên nhau", 0.3, 0.07, "red"),
    ("Vì thời gian sẽ không trôi êm đềm ", 0.1, 0.07, "cyan"),
    ("Giống như khi đôi môi mềm", 0.2, 0.06, "red"),
    ("Còn ấm đam mê như ban đầu", 0.1, 0.06, "cyan"),
    ("Để miền yêu thương khép lại", 0.1, 0.06, "red"),
    ("Uhhh anh đã cố nói em khi", 0.4, 0.09, "cyan"),
    ("Bên anh chỉ là mộng ước", 0.4, 0.08, "red"),
    ("Nguội lạnh theo hơi ấm nhạt màu", 0.3, 0.07, "cyan"),
    ("(Lạnh theo hơi ấm nhạt màu)", 0.2, 0.04, "red"),
    ("Nguội lạnh theo hơi ấm nhạt màu", 0.3, 0.05, "cyan"),
    ("(eh y-yeh y-yeh huh)", 0.3, 0.06, "red"),
]

                                                                                       
def main():
    setup()

    try:

        for line in lyrics:
            display(*line)
        print("\nHoàn thành! ")
    except KeyboardInterrupt:
        print("\n\nDừng phát!")


if __name__ == "__main__":
    main()
