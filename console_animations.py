import time

# Progress Bar ////////////////////////////////////////////////
# length = 30
# delay = 0.3
# for i in range(1, length):
#     time.sleep(delay)
#     progress_bar = "#" * i
#     print(f"[{progress_bar.ljust(length, ' ')}]\r", end="")


# Spinning Stick ////////////////////////////////////////////////
# delay = 0.1
# frames = ["\\", "|", "/", "-", 0]
# while True:
#     time.sleep(delay)
#     print(frames[frames[4]] * 100 + "\r", end="")
#     frames[4] = (frames[4] + 1) % 4


# Running Line ////////////////////////////////////////////////
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

    if frame == length - 5:
        direction = -1
    elif frame == 0:
        direction = 1
    frame = (frame + direction) % length
