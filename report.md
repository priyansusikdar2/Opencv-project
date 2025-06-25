Approach and Methodology

Used YOLOv8n for fast object detection, limited to detecting class person.

Integrated Deep SORT for multi-object tracking that handles re-identification when players leave and re-enter the frame.

Filtered out false positives using confidence and bounding box constraints.

Techniques Tried

YOLOv8 + Deep SORT (final): Stable tracking, quick to integrate, works for 15s clips.

Improved tracking by filtering detections by size and applying a unique label-per-ID policy.

Challenges Encountered

Deep SORT had some ID switches in highly occluded areas.

Ghost detections and overlapping player IDs occurred at times.

Incomplete Areas / Next Steps

Still minor flickering of IDs when players overlap.

Improve tracking with ByteTrack or add jersey color-based team identification.

Consider optimizing runtime with ONNX or TensorRT deployment.

