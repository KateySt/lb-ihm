import cv2
import time

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    cv2.namedWindow('Original Video', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Canny Edge Detection', cv2.WINDOW_NORMAL)

    frame_count = 0
    total_processing_speed = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        start_time = time.time()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 50, 150)

        cv2.imshow('Original Video', frame)
        cv2.imshow('Canny Edge Detection', edges)

        end_time = time.time()

        processing_speed = 1 / (end_time - start_time)
        total_processing_speed += processing_speed
        frame_count += 1

        print(f"Швидкість обробки: {processing_speed:.2f} кадрів/с")

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
