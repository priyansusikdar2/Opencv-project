import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load model and initialize tracker
model = YOLO("yolov8n.pt")
tracker = DeepSort(
    max_age=15,
    n_init=2,
    max_iou_distance=0.7,
    embedder="mobilenet",
    half=True
)

# Open video
cap = cv2.VideoCapture("15sec_input_720p.mp4")
fps = int(cap.get(cv2.CAP_PROP_FPS))
w, h = int(cap.get(3)), int(cap.get(4))
out = cv2.VideoWriter("output_tracked_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

print("[INFO] Running optimized tracking. Press ESC to quit early.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Step 1: Detect with YOLO
    results = model(frame, classes=[0], conf=0.6, verbose=False)[0]

    detections = []
    for box in results.boxes:
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        width, height = x2 - x1, y2 - y1

        # Filter out tiny ghost boxes
        if width < 20 or height < 40:
            continue

        detections.append(([x1, y1, width, height], conf, "person"))

    # Step 2: Track
    tracks = tracker.update_tracks(detections, frame=frame)

    # Step 3: Draw unique player labels
    seen = set()
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        if track_id in seen:
            continue
        seen.add(track_id)
        l, t, r, b = map(int, track.to_ltrb())
        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
        cv2.putText(frame, f"Player {track_id}", (l, t - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow("Fixed Player Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        print("[INFO] Exit requested.")
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("[INFO] Final output saved to 'output_tracked_video.mp4'")
