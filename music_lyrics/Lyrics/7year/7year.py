import sys, time, os, atexit
from typing import Optional

# Xóa màn hình (đa nền tảng)
os.system("cls" if os.name == "nt" else "clear")

# Ẩn con trỏ
sys.stdout.write("\x1b[?25l")
sys.stdout.flush()

# Luôn hiện lại con trỏ khi thoát
atexit.register(lambda: (sys.stdout.write("\x1b[?25h"), sys.stdout.flush()))

# Ghi ra ngay lập tức (nếu môi trường hỗ trợ)
try:
    sys.stdout.reconfigure(line_buffering=False, write_through=False)
except Exception:
    pass

# Màu (nếu có)
try:
    from termcolor import colored
    from colorama import init as colorama_init

    colorama_init()

    def paint(t: str) -> str:
        return colored(t, "cyan")

except Exception:

    def paint(t: str) -> str:
        return t


# Thông số mặc định
CHAR_DELAY = 0
LEAD_IN = 0


def type_out(text: str, char_delay: float = CHAR_DELAY) -> None:

    for ch in text:
        sys.stdout.write(paint(ch))
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def sing(
    line: str,
    before: float = 0.0,
    after: float = 0.0,
    target_duration: Optional[float] = None,
    char_delay: Optional[float] = None,
) -> None:

    time.sleep(before + LEAD_IN)

    if char_delay is None:
        if target_duration is not None and len(line) > 0:
            char_delay = target_duration / len(line)
        else:
            char_delay = CHAR_DELAY

    type_out(line, char_delay=char_delay)
    time.sleep(after)


lines = [
    ("Once I was seven years old, my mama told me", 0.5, 0.5, 3.6),
    ('"Go make yourself some friends, or you\'ll be lonely"', 0.10, 0.10, 3.1),
    ("Once I was seven years old", 0.10, 5.60, 2.8),
    ("It was a big, big world, but we thought we were bigger", 0.10, 0.10, 4.1),
    ("Pushin' each other to the limits, we were learnin' quicker", 0.10, 0.10, 3.7),
    ("By 11, smokin' herb and drinkin' burnin' liquor", 0.10, 0.10, 3.8),
    ("Never rich, so we were out to make that steady figure", 0.10, 0.10, 3.7),
    ("Once I was 11 years old, my daddy told me", 0.10, 0.10, 3.5),
    ('"Go get yourself a wife, or you\'ll be lonely"', 0.10, 0.10, 3.3),
    ("Once I was 11 years old", 0.3, 3.7, 3.0),
]

try:
    for item in lines:
        if len(item) == 3:
            text, before, after = item
            sing(text, before, after)
        elif len(item) == 4:
            text, before, after, target_duration = item
            sing(text, before, after, target_duration=target_duration)
        else:
            continue
finally:
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()
