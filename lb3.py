import cv2
import time
import numpy as np

def graham_scan(points):
    points = sorted(points, key=lambda p: (p[0], p[1]))
    stack = []

    def cross(o, a, b):
        return (a[1] - o[1]) * (b[0] - a[0]) - (a[0] - o[0]) * (b[1] - a[1])

    for p in points:
        while len(stack) >= 2 and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    t = len(stack)
    for p in reversed(points):
        while len(stack) > t and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack[:-1]

def apply_graham_scan(frame, points):
    contour_points = graham_scan(points)
    for i in range(len(contour_points)):
        cv2.line(frame, tuple(contour_points[i]), tuple(contour_points[(i + 1) % len(contour_points)]), (0, 0, 255), 2)
    return frame


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Graham Scan Contour', cv2.WINDOW_NORMAL)

    start_time = time.time()
    frame_count = 0

    ret, prev_frame = cap.read()
    if not ret:
        return

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        points = np.argwhere(np.abs(flow) > 2)

        contour_image = apply_graham_scan(frame.copy(), points)

        cv2.imshow('Video', frame)

        cv2.imshow('Graham Scan Contour', contour_image)

        frame_count += 1

        if cv2.waitKey(1) & 0xFF == 27:
            break

        prev_gray = gray.copy()

    end_time = time.time()
    elapsed_time = end_time - start_time

    processing_speed = frame_count / elapsed_time
    print(f"Швидкість обробки кадрів: {processing_speed:.2f} кадрів за секунду")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
