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
    ("Những cánh hoa rơi theo dòng nước mắt", 0.7, 0.06, "cyan"),
    ("Ngày đã hoá thành mưa rồi", 0.6, 0.07, "red"),
    ("Tiếng thét vang lên trong từng cơn đau", 0.1, 0.06, "cyan"),
    ("Nào dám nói thành câu nào", 0.3, 0.09, "red"),
    ("Chẳng trách ai cũng phải sợ", 0.4, 0.07, "cyan"),
    ("Đến lúc yêu thương không còn", 1.2, 0.09, "red"),
    ("Người cạnh bên mà chẳng thể hiểu được...", 0.1, 0.06, "cyan"),
    ("Làm cách nào có thể giữ lấy Không bằng chia tay", 0.1, 0.09, "red"),
    ("Chìm xuống dưới vực sâu này", 0.4, 0.08, "cyan"),
    ("Dễ nhớ mau quên những lời mây bay", 0.3, 0.07, "red"),
    ("Chỉ nhận lại những đắng cay", 0.2, 0.08, "cyan"),
]


def main():
    setup()
    print(color_text("       Dia Nguc Tran Gian\n", "yellow"))
    try:

        for line in lyrics:

            display(*line)
        print("\nHoàn thành! ")
    except KeyboardInterrupt:
        print("\n\nDừng phát!")


if __name__ == "__main__":
    main()
