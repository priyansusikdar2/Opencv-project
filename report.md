# 📝 Player Tracking Assignment Report

## 📌 Objective

To implement a system that can identify and consistently re-identify players in a 15-second video clip. The system must:

* Assign unique IDs to players.
* Maintain those IDs when players reappear after leaving the frame.
* Simulate real-time processing.

---

## 🧠 Approach & Methodology

### 🎯 Detection

* Used **YOLOv8n** from Ultralytics for efficient person detection.
* Filtered detections using confidence threshold (`0.6`) and bounding box size to remove false positives.

### 🚀 Tracking

* Integrated **Deep SORT** with MobileNet embedding.
* Ensured unique IDs using `track_id` per detection.
* Prevented ghost tracking using filters on width and height.

### 🎬 Video Processing

* Captured frames via OpenCV.
* Saved output video with bounding boxes and labels.
* Allowed early termination with `ESC` key.

---

## 🧪 Techniques Tried

| Technique                         | Outcome                                                                    |
| --------------------------------- | -------------------------------------------------------------------------- |
| YOLOv8 + Deep SORT                | Stable tracking for short clips. ID switching reduced with size filtering. |
| YOLOv8 + ByteTrack (experimental) | More stable in occlusion, but more complex integration.                    |

---

## ⚠️ Challenges Encountered

* **Ghost boxes** from overlapping players.
* **ID flickering** during occlusions.
* Some players still receive **multiple IDs** in rare cases.

---

## ✅ Improvements Made

* Filtered out tiny bounding boxes under 20x40 pixels.
* Ensured only `is_confirmed()` tracks were shown.
* De-duplicated ID display using a `seen` set per frame.

---

## 🔧 Incomplete/Next Steps

* Add **team-color classification** (red vs blue) for semantic grouping.
* Add a **ReID embedding network** trained on sports datasets.
* Consider **ByteTrack** or **StrongSORT** for better long-term tracking.
* Deploy with ONNX or TensorRT for improved runtime on edge devices.

---

## 📁 Files Included

* `src/main_yolo_deepsort.py` — Main tracking script
* `requirements.txt` — Python dependencies
* `README.md` — Setup instructions
* `15sec_input_720p.mp4` — Input video
* `output_tracked_video.mp4` — Output (after running)

---

> ✨ Built using Python, OpenCV, Ultralytics YOLOv8, and Deep SORT.
> Final output is a video with green boxes and player IDs rendered live.
