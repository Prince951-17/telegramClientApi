from datetime import datetime

import cv2
import numpy as np

array = []


def getStringFromArray(index):
    return array[index]


def countdown(now):
    date_time_str = '2021-01-01 00:00:00'
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    return date_time_obj - now


def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}:{dt.second:02}"


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)


def get_black_background():
    return np.zeros((500, 500, 4))


def generate_time_image_bytes(dt):
    text = convert_time_to_string(dt)
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(image, text, (int(image.shape[0] * 0.24), int(image.shape[0] * 0.55)), font, 3.0, (0, 0, 255), 10,
                cv2.LINE_AA)
    _, bts = cv2.imencode('.jpg', image)
    return bts.tobytes()
