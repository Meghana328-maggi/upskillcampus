from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Video path
video_path = "videos/traffic3.mp4"

# Open video
cap = cv2.VideoCapture(video_path)

# Check video
if not cap.isOpened():
    print("Cannot open video")
    exit()

# Vehicle classes
vehicle_classes = ["car", "motorcycle", "bus", "truck"]

while cap.isOpened():

    ret, frame = cap.read()

    # Restart video automatically
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Resize frame
    frame = cv2.resize(frame, (1000, 600))

    # YOLO detection
    results = model(frame)

    vehicle_count = 0

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])
            class_name = model.names[cls]

            if class_name in vehicle_classes:

                vehicle_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw rectangle
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                # Vehicle label
                cv2.putText(
                    frame,
                    class_name,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

    # Traffic density logic
    if vehicle_count < 10:
        density = "LOW"
        signal_time = 20

    elif vehicle_count < 25:
        density = "MEDIUM"
        signal_time = 40

    else:
        density = "HIGH"
        signal_time = 60

    # Vehicle count text
    cv2.putText(
        frame,
        f"Vehicle Count: {vehicle_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

    # Density text
    cv2.putText(
        frame,
        f"Traffic Density: {density}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        3
    )

    # Signal timing text
    cv2.putText(
        frame,
        f"Signal Time: {signal_time} sec",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        3
    )

    # Display output
    cv2.imshow("Smart Traffic Management", frame)

    # Exit key
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()