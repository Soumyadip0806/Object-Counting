# -*- coding: utf-8 -*-

!nvidia-smi

from google.colab import drive
drive.mount('/content/drive')

!pip install ultralytics -q

from ultralytics import YOLO

model=YOLO("yolov8m.pt")

!touch data.yaml

model.train(data ="/content/data.yaml",epochs=100)

!scp -r /content/runs/detect/train5 '/content/gdrive/My Drive/mgroad/mgroad'

infer = YOLO("/content/drive/MyDrive/best (1)_FROM OUR DATA SET.pt")

infer.predict("//content/drive/MyDrive/VIDEO/7139152e-bd3d-44b0-8b45-ede178f52930.mp4", save = True , save_txt = True)

import json
from ultralytics import YOLO
results = infer.predict("/content/drive/MyDrive/mgroad/FINAL/test/images/TALAS09_100.jpg")

for result in results:
    boxes = result.boxes
    print(boxes)

infer.predict(source="/content/drive/MyDrive/VIDEO/7139152e-bd3d-44b0-8b45-ede178f52930.mp4", save = True,imagesize="67")

"""FOR COUNTING

"""

pip install supervision

from ultralytics import YOLO
from ultralytics.solutions import object_counter
import cv2

model = YOLO("/content/drive/MyDrive/best (1)_FROM OUR DATA SET.pt")
cap = cv2.VideoCapture("/content/drive/MyDrive/VIDEO/WhatsApp Video 2024-03-31 at 13.02.03_4660e101.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define line points
line_points = [(466, 196), (1118, 180)]
classes_to_count = [10]  # person and car classes for count
track_thickness=[4]

# Video writer
video_writer = cv2.VideoWriter("object_counting_output_opt5.avi",
                       cv2.VideoWriter_fourcc(*'mp4v'),
                       fps,
                       (w, h))

# Init Object Counter
counter = object_counter.ObjectCounter()
counter.set_args(view_img=True,
                 reg_pts=line_points,
                 classes_names=model.names,
                 draw_tracks=True)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    tracks = model.track(im0, persist=True, show=True)

    im0 = counter.start_counting(im0, tracks)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()

"""JUST FOR CHECKING MILESTON FILE

"""

infer = YOLO("/content/drive/MyDrive/best.pt")

infer.predict("/content/drive/MyDrive/VIDEO/Client Files", save = True , save_txt = True)