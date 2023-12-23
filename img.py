import cv2
from pyautogui import screenshot,size
import time
def capture_image():
    # Open a connection to the camera (0 represents the default camera, change it if necessary)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    if ret:
        return frame
    else:
        print("Error: Could not capture an image.")
        return None

def cameraCapture():
    # Capture an image
    captured_image = capture_image()
    filename="captured_image.jpg"
    # Check if the image was successfully captured
    if captured_image is not None:
        # Save the image
        # save_image(captured_image)
        cv2.imwrite(filename, captured_image)
    return filename
    
def take_screenshot(output_filename="screenshot.png"):
    screen_width, screen_height = size()
    ss = screenshot()

    # Save the screenshot using PIL
    ss.save(output_filename)
    return str(output_filename)

async def record(duration):
    start_time = time.time()
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        # cv2.imshow('Frame', frame)
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= duration:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return "output.avi"

