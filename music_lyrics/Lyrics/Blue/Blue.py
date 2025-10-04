import sys
import time

COLORS = {
    "cyan": "\033[96m",
    "red": "\033[1;91m",
    "blue": "\033[94m",
    "reset": "\033[0m",
}


def setup():
    pass


def color_text(text, color="blue"):
    return COLORS.get(color, COLORS["blue"]) + text + COLORS["reset"]


def display(text, delay_after=0, char_speed=0.05, color="blue"):
    for char in text:
        sys.stdout.write(color_text(char, color))
        sys.stdout.flush()
        time.sleep(char_speed)
    print()
    time.sleep(delay_after)


lyrics = [
    ("Your morning eyes", 0.9, 0.05, "blue"),
    ("I could stare like watching stars", 2.0, 0.10, "cyan"),
    ("I could walk you by", 0.6, 0.05, "blue"),
    ("and I'll tell without a thought", 0.7, 0.06, "cyan"),
    ("You'd be mine", 0.5, 0.04, "blue"),
    ("Would you mind ", 0.5, 0.04, "cyan"),
    ("If I took your hand tonight?", 0.8, 0.07, "blue"),
    ("Know you're all ", 0.9, 0.08, "cyan"),
    ("That I want this life", 0.7, 0.06, "blue"),
    ("I'll imagine we fell in love", 0.6, 0.05, "red"),
    ("I'll nap under moonlight skies with you", 0.8, 0.06, "red"),
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
