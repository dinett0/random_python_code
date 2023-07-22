import time


def progress_bar():
    length = 50
    delay = 0.1
    for i in range(1, length + 1):
        time.sleep(delay)
        progress_bar = "#" * i
        print(f"[{progress_bar.ljust(length, ' ')}] {i*2:02d}%\r", end="")
    print()


def spinning_stick():
    delay = 0.1
    frames = ["\\", "|", "/", "-", 0]
    while True:
        time.sleep(delay)
        animation_element = frames[frames[4]] * 5
        print(animation_element + " Hello " + animation_element + "\r", end="")
        frames[4] = (frames[4] + 1) % 4


def bouncing_line():
    length = 30
    running_line = "88888"
    left_marging = 0
    right_marging = length - len(running_line)
    frame = 0
    while True:
        time.sleep(0.05)
        print(
            running_line.rjust(left_marging + frame + len(running_line), " ")
            + (right_marging - frame) * " "
            + "\r",
            end="",
        )
        if frame == length - len(running_line):
            direction = -1
        elif frame == 0:
            direction = 1
        frame = (frame + direction) % length


def running_line():
    length = 30
    running_line = "88888"
    left_marging = 0
    right_marging = length - len(running_line)

    while True:
        time.sleep(0.05)
        print(
            "|"
            + left_marging * " "
            + running_line
            + (right_marging - left_marging) * " "
            + "|"
            + "\r",
            end="",
        )
        direction = 1
        left_marging = (left_marging + direction) % (length - len(running_line) + 1)


def running_line_dumb():
    delay = 0.1
    while True:
        print("***   \r", end="")
        time.sleep(delay)
        print(" ***  \r", end="")
        time.sleep(delay)
        print("  *** \r", end="")
        time.sleep(delay)
        print("   ***\r", end="")
        time.sleep(delay)
        print("*   **\r", end="")
        time.sleep(delay)
        print("**   *\r", end="")
        time.sleep(delay)


# progress_bar()
spinning_stick()
# bouncing_line()
# running_line()
#running_line_dumb()
