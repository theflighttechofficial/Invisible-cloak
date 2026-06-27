import cv2
import numpy as np
import time

selected_color_bgr = None
clicked = False

# Mouse callback to pick color
def pick_color(event, x, y, flags, param):
    global selected_color_bgr, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_color_bgr = palette[y, x]
        clicked = True

# Create a simple color palette (no gradients)
def create_palette():
    colors = [
        (0, 0, 255),      # Red
        (0, 255, 0),      # Green
        (255, 0, 0),      # Blue
        (0, 255, 255),    # Yellow
        (0, 165, 255),    # Orange
        (128, 0, 128),    # Purple
        (203, 192, 255),  # Pink
        (19, 69, 139),    # Brown
        (128, 128, 128),  # Gray
        (255, 255, 0),    # Light Blue (Cyan-like but usable)
        (0, 100, 0)       # Dark Green
    ]

    palette = np.zeros((200, 550, 3), dtype=np.uint8)

    w = 50
    for i, color in enumerate(colors):
        palette[:, i*w:(i+1)*w] = color

    return palette


# Create palette
palette = create_palette()

cv2.namedWindow("Select Color")
cv2.setMouseCallback("Select Color", pick_color)

# Show palette until user selects color
while True:
    cv2.imshow("Select Color", palette)
    if clicked:
        break
    if cv2.waitKey(1) == 27:  # ESC to exit
        cv2.destroyAllWindows()
        exit()

cv2.destroyWindow("Select Color")

# Convert selected BGR to HSV
selected_color = np.uint8([[selected_color_bgr]])
hsv_selected = cv2.cvtColor(selected_color, cv2.COLOR_BGR2HSV)[0][0]

# Define range around selected color
lower = np.array([hsv_selected[0] - 10, 80, 70])
upper = np.array([hsv_selected[0] + 10, 255, 255])

print("Selected HSV:", hsv_selected)

# Start camera
cap = cv2.VideoCapture(0)

print("Capturing background... stay still!")
time.sleep(3)

# Capture background
for i in range(60):
    ret, background = cap.read()
    if not ret:
        continue
    background = np.flip(background, axis=1)

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                            np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

    mask_inv = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisibility Cloak", final_output)

    # Press 'q' or ESC to exit
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()