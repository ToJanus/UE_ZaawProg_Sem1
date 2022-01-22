import os
from pathlib import Path

import json
from time import perf_counter

import cv2


def run(obraz=None):
    if obraz is None:
        base_str = Path('images')
        obr_list = os.listdir(base_str)
        for img in obr_list:
            p = base_str / Path(img)
            detect(p)
    else:
        detect(obraz)


def detect(obraz_path):
    img = cv2.imread(str(obraz_path))
    cvNet = cv2.dnn.readNetFromTensorflow('models_tensorflow/frozen_inference_graph.pb',
                                          'models_tensorflow/frozen_inference_graph.pbtxt')

    rows = img.shape[0]
    cols = img.shape[1]
    cvNet.setInput(cv2.dnn.blobFromImage(img, size=(600, 600), swapRB=True, crop=False))
    start_time = perf_counter()
    cv_out = cvNet.forward()
    end_time = perf_counter() - start_time
    print(f"Czas detekcji dla pliku {obraz_path}: {end_time} s")
    with open("models_tensorflow/classes.json") as file:
        classes = json.load(file)
    licz_osob = 0
    for i in range(cv_out.shape[2]):
        wynik = float(cv_out[0, 0, i, 2])
        if wynik > 0.5:
            klasa = classes[str(int(cv_out[0, 0, i, 1]))]
            if klasa == "person":
                licz_osob += 1
                cv_obj = cv_out[0, 0, i]
                left = cv_obj[3] * cols
                top = cv_obj[4] * rows
                right = cv_obj[5] * cols
                bottom = cv_obj[6] * rows
                cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 23, 210), thickness=2)
                cv2.putText(img, f"Osoba {licz_osob}", (int(left), int(bottom) + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                            (23, 23, 210), 2)

    cv2.putText(img, f"Wykryto {licz_osob} osob", (10, rows - 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (23, 23, 210), 3)
    cv2.putText(img, f"Czas detekcji: {round(end_time, 3)} s", (10, rows - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 230), 2)
    cv2.imshow("Obraz", img)
    cv2.waitKey()
