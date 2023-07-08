import time

# # Progress Bar ////////////////////////////////////////////////
length = 50
delay = 0.1
for i in range(1, length + 1):
    time.sleep(delay)
    progress_bar = "#" * i
    print(f"[{progress_bar.ljust(length, ' ')}] {i*2:02d}%\r", end="")
print()


# # Spinning Stick ////////////////////////////////////////////////
delay = 0.1
frames = ["\\", "|", "/", "-", 0]
while True:
    time.sleep(delay)
    animation_element = frames[frames[4]] * 5
    print(animation_element + " Hello " + animation_element + "\r", end="")
    frames[4] = (frames[4] + 1) % 4


# # Bouncing Line ////////////////////////////////////////////////
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


# # Running Line ////////////////////////////////////////////////
length = 30
running_line = "88888"
left_marging = 0
right_marging = length - len(running_line)
frame = 0
while True:
    time.sleep(0.15)
    print(
        "|"
        + running_line.rjust(left_marging + frame + len(running_line), " ")
        + (right_marging - frame) * " "
        + "|"
        + "\r",
        end="",
    )
    direction = 1
    frame = (frame + direction) % (length - len(running_line))
