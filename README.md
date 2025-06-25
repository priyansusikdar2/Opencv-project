# 📘 Real-Time Player Re-Identification and Tracking

A computer vision project using **YOLOv8** and **Deep SORT** to track and re-identify players in a short video clip.

---

## 🚀 Features

* Real-time person detection with YOLOv8
* Consistent ID tracking using Deep SORT
* False detection filtering
* ESC key to terminate early
* Saves result to `output_tracked_video.mp4`

---

## 🛠️ Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

### requirements.txt

```
ultralytics
deep-sort-realtime
opencv-python
```

---

## 🎥 Running the Project

Make sure the input video `15sec_input_720p.mp4` is in the same directory.

Run the script:

```bash
python src/main_yolo_deepsort.py
```

You will see a window with live tracking. Press `ESC` to exit early.
The output video will be saved as `output_tracked_video.mp4`.

---

## 🧪 Output Example

* Each player is marked with a green box.
* A label like `Player 4` is shown for consistent re-identification.
* Players are assigned the same ID even after temporary disappearance.

---

## 🔄 Customization Tips

| Feature           | How to Customize                       |
| ----------------- | -------------------------------------- |
| Detection model   | Change `yolov8n.pt` to `yolov8s.pt`    |
| Confidence filter | Adjust `conf=0.6` in script            |
| Tracker embedding | Switch `embedder` to `osnet` or others |

---

## 📂 Folder Structure

```
project_folder/
├── src/
│   └── main_yolo_deepsort.py
├── 15sec_input_720p.mp4
├── output_tracked_video.mp4
├── README.md
├── report.md
└── requirements.txt
```

---

## 👨‍💻 Credits

Built using:

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* [deep-sort-realtime](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch)
* [OpenCV](https://opencv.org/)

---

> ⚡ For best performance, run on a CUDA-enabled GPU.
> 📫 For questions or improvements, feel free to reach out!
