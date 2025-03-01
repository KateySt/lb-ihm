import cv2
import time
import numpy as np

def graham_scan(points):
    points = sorted(points, key=lambda p: (p[0], p[1]))
    stack = []

    def cross(o, a, b):
        return (a[1] - o[1]) * (b[0] - o[0]) - (a[0] - o[0]) * (b[1] - o[1])

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

def filter_points_by_motion(flow, threshold=2):
    points = np.argwhere(np.abs(flow) > threshold)
    return points

def apply_contour_detection(frame, points):
    mask = np.zeros_like(frame, dtype=np.uint8)
    for point in points:
        cv2.circle(mask, (point[1], point[0]), 3, 255, -1)

    gray_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    contours, _ = cv2.findContours(gray_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)

    for contour in contours:
        cv2.fillPoly(frame, [contour], (0, 0, 255))

    return frame

def test_lighting_conditions():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Contour Detection', cv2.WINDOW_NORMAL)

    start_time = time.time()
    frame_count = 0
    contour_processing_time = 0

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

        points = filter_points_by_motion(flow, threshold=2)

        contour_start_time = time.time()
        contour_image = apply_contour_detection(frame.copy(), points)
        contour_end_time = time.time()
        contour_processing_time += contour_end_time - contour_start_time

        cv2.imshow('Video', frame)
        cv2.imshow('Contour Detection', contour_image)

        frame_count += 1

        if cv2.waitKey(1) & 0xFF == 27:
            break

        prev_gray = gray.copy()

    end_time = time.time()
    elapsed_time = end_time - start_time

    processing_speed = frame_count / elapsed_time
    contour_speed = frame_count / contour_processing_time

    print(f"Швидкість обробки кадрів: {processing_speed:.2f} кадрів за секунду")
    print(f"Швидкість побудови контуру: {contour_speed:.2f} кадрів за секунду")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_lighting_conditions()
