import cv2
import mediapipe as mp
import pyautogui
import random
import time
import util

from pynput.mouse import Button, Controller

mouse = Controller()

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# MediaPipe Hands setup
mpHands = mp.solutions.hands

hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

draw = mp.solutions.drawing_utils

# Prevent gestures such as clicks from firing continuously
last_action_time = 0
ACTION_COOLDOWN = 0.6

# Drag state
dragging = False

# Previous position used for scrolling
previous_scroll_y = None


def find_finger_tip(processed):
    """
    Find the index finger tip from MediaPipe hand landmarks.
    """
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]
        index_finger_tip = hand_landmarks.landmark[
            mpHands.HandLandmark.INDEX_FINGER_TIP
        ]
        return index_finger_tip

    return None


def move_mouse(index_finger_tip):
    """
    Move the system cursor according to the index finger position.
    """
    if index_finger_tip is not None:
        x = int(index_finger_tip.x * screen_width)

        # Limit vertical movement to make cursor control easier
        y = int(index_finger_tip.y / 2 * screen_height)

        pyautogui.moveTo(x, y)


def is_left_click(landmark_list, thumb_index_dist):
    """
    Detect left-click gesture.
    """
    return (
        util.get_angle(
            landmark_list[5],
            landmark_list[6],
            landmark_list[8]
        ) < 50
        and
        util.get_angle(
            landmark_list[9],
            landmark_list[10],
            landmark_list[12]
        ) > 90
        and
        thumb_index_dist > 50
    )


def is_right_click(landmark_list, thumb_index_dist):
    """
    Detect right-click gesture.
    """
    return (
        util.get_angle(
            landmark_list[9],
            landmark_list[10],
            landmark_list[12]
        ) < 50
        and
        util.get_angle(
            landmark_list[5],
            landmark_list[6],
            landmark_list[8]
        ) > 90
        and
        thumb_index_dist > 50
    )


def is_double_click(landmark_list, thumb_index_dist):
    """
    Detect double-click gesture.
    """
    return (
        util.get_angle(
            landmark_list[5],
            landmark_list[6],
            landmark_list[8]
        ) < 50
        and
        util.get_angle(
            landmark_list[9],
            landmark_list[10],
            landmark_list[12]
        ) < 50
        and
        thumb_index_dist > 50
    )


def is_screenshot(landmark_list, thumb_index_dist):
    """
    Detect screenshot gesture.
    """
    return (
        util.get_angle(
            landmark_list[5],
            landmark_list[6],
            landmark_list[8]
        ) < 50
        and
        util.get_angle(
            landmark_list[9],
            landmark_list[10],
            landmark_list[12]
        ) < 50
        and
        thumb_index_dist < 50
    )


def is_scroll(landmark_list, thumb_index_dist):
    """
    Detect scrolling gesture.

    Both index and middle fingers are extended
    while the thumb is separated from the index finger.
    """
    index_angle = util.get_angle(
        landmark_list[5],
        landmark_list[6],
        landmark_list[8]
    )

    middle_angle = util.get_angle(
        landmark_list[9],
        landmark_list[10],
        landmark_list[12]
    )

    return (
        index_angle > 90
        and
        middle_angle > 90
        and
        thumb_index_dist > 50
    )


def is_drag(landmark_list, thumb_index_dist):
    """
    Detect dragging gesture.

    Index finger is extended while the middle finger
    is bent and the thumb is close to the index finger.
    """
    index_angle = util.get_angle(
        landmark_list[5],
        landmark_list[6],
        landmark_list[8]
    )

    middle_angle = util.get_angle(
        landmark_list[9],
        landmark_list[10],
        landmark_list[12]
    )

    return (
        index_angle > 90
        and
        middle_angle < 50
        and
        thumb_index_dist < 50
    )


def perform_scroll(index_finger_tip):
    """
    Scroll according to vertical index finger movement.
    """
    global previous_scroll_y

    if index_finger_tip is None:
        return

    current_y = index_finger_tip.y

    if previous_scroll_y is not None:
        movement = previous_scroll_y - current_y

        # Ignore very small movements
        if abs(movement) > 0.01:
            scroll_amount = int(movement * 30)

            if scroll_amount != 0:
                pyautogui.scroll(scroll_amount)

    previous_scroll_y = current_y


def reset_scroll():
    """
    Reset the previous scroll position.
    """
    global previous_scroll_y
    previous_scroll_y = None


def can_perform_action():
    """
    Check whether enough time has passed since the last action.
    """
    global last_action_time

    current_time = time.time()

    if current_time - last_action_time >= ACTION_COOLDOWN:
        last_action_time = current_time
        return True

    return False


def take_screenshot():
    """
    Capture and save a screenshot with a random filename.
    """
    image = pyautogui.screenshot()

    label = random.randint(1, 100000)

    filename = f"my_screenshot_{label}.png"

    image.save(filename)

    return filename


def detect_gesture(frame, landmark_list, processed):
    """
    Detect the current hand gesture and perform the
    corresponding mouse action.
    """
    global dragging

    if len(landmark_list) < 21:
        reset_scroll()

        if dragging:
            mouse.release(Button.left)
            dragging = False

        return

    index_finger_tip = find_finger_tip(processed)

    thumb_index_dist = util.get_distance(
        [landmark_list[4], landmark_list[5]]
    )

    # -------------------------------------------------
    # DRAG
    # -------------------------------------------------
    if is_drag(landmark_list, thumb_index_dist):

        reset_scroll()

        if not dragging:
            mouse.press(Button.left)
            dragging = True

        move_mouse(index_finger_tip)

        cv2.putText(
            frame,
            "Dragging",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2
        )

        return

    # If dragging gesture has ended, release mouse
    if dragging:
        mouse.release(Button.left)
        dragging = False

    # -------------------------------------------------
    # SCROLL
    # -------------------------------------------------
    if is_scroll(landmark_list, thumb_index_dist):

        perform_scroll(index_finger_tip)

        cv2.putText(
            frame,
            "Scrolling",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2
        )

        return

    reset_scroll()

    # -------------------------------------------------
    # CURSOR MOVEMENT
    # -------------------------------------------------
    index_angle = util.get_angle(
        landmark_list[5],
        landmark_list[6],
        landmark_list[8]
    )

    if thumb_index_dist < 50 and index_angle > 90:

        move_mouse(index_finger_tip)

        cv2.putText(
            frame,
            "Moving Cursor",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    # -------------------------------------------------
    # LEFT CLICK
    # -------------------------------------------------
    elif is_left_click(landmark_list, thumb_index_dist):

        if can_perform_action():

            mouse.press(Button.left)
            mouse.release(Button.left)

        cv2.putText(
            frame,
            "Left Click",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    # -------------------------------------------------
    # RIGHT CLICK
    # -------------------------------------------------
    elif is_right_click(landmark_list, thumb_index_dist):

        if can_perform_action():

            mouse.press(Button.right)
            mouse.release(Button.right)

        cv2.putText(
            frame,
            "Right Click",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # -------------------------------------------------
    # DOUBLE CLICK
    # -------------------------------------------------
    elif is_double_click(landmark_list, thumb_index_dist):

        if can_perform_action():

            pyautogui.doubleClick()

        cv2.putText(
            frame,
            "Double Click",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2
        )

    # -------------------------------------------------
    # SCREENSHOT
    # -------------------------------------------------
    elif is_screenshot(landmark_list, thumb_index_dist):

        if can_perform_action():

            filename = take_screenshot()

            cv2.putText(
                frame,
                "Screenshot Taken",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 0),
                2
            )

    else:
        cv2.putText(
            frame,
            "Gesture not recognized",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 165, 255),
            2
        )


def main():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Virtual Mouse started.")
    print("Press 'q' to quit.")

    try:

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read webcam frame.")
                break

            # Mirror the webcam
            frame = cv2.flip(frame, 1)

            # Convert BGR to RGB for MediaPipe
            frameRGB = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            # Process hand
            processed = hands.process(frameRGB)

            landmark_list = []

            # Draw hand landmarks
            if processed.multi_hand_landmarks:

                hand_landmarks = processed.multi_hand_landmarks[0]

                draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mpHands.HAND_CONNECTIONS
                )

                for lm in hand_landmarks.landmark:

                    landmark_list.append(
                        (lm.x, lm.y)
                    )

            # Detect gesture
            detect_gesture(
                frame,
                landmark_list,
                processed
            )

            # Display webcam
            cv2.imshow(
                "Gesture Controlled Virtual Mouse",
                frame
            )

            # Press Q to exit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:

        if dragging:
            mouse.release(Button.left)

        cap.release()

        cv2.destroyAllWindows()

        print("Virtual Mouse stopped.")


if __name__ == "__main__":
    main()
