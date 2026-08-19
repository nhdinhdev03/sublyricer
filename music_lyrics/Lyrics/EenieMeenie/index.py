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


# Thông số mặc định
CHAR_DELAY = 0
LEAD_IN = 0


def type_out(text: str, char_delay: float = CHAR_DELAY) -> None:

    for ch in text:
        sys.stdout.write(ch)
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
    ("I like you, but...", 0.1, 0.3, 1.8),
    ("You seem like the type to love 'em and leave 'em", 2.0, 0.6, 5.3),
    ("And disappear right after the song", 0.2, 0.1, 2.9),
    ("So give me the night", 0.8, 1.0, 2.0),
    ("To show you, and hold you", 0.2, 0.5, 2.0),
    ("Don't leave me out here dancin' alone", 0.2, 0.3, 3.5),
    ("Can't make up your mind, mind, mind, mind, mind", 0.2, 1.0, 3.2),
    ("Please don't waste my time, time, time, time, time", 0.2, 0.5, 3.8),
    ("Not tryin' to rewind, wind, wind, wind, wind, wind", 0.9, 0.5, 4.0),
    ("I wish our hearts could come together as one", 0.2, 0.7, 3.7),
    ("Shawty yeah is an eenie meenie miney mo lover", 0.2, 0.5, 3.8),
    ("Shawty is an eenie meenie miney mo lover ", 0.9, 0.1, 4.0),
    ("Shawty is an eenie meenie miney mo lover", 0.9, 0.2, 4.2),
    ("Shawty is an eenie meenie miney mo lover", 0.12, 0.1, 4.5),
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
