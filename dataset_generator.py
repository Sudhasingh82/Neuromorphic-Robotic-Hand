import pandas as pd
import numpy as np

gestures = ["open_hand", "close_fist", "thumbs_up", "peace", "point"]

data = []
np.random.seed(42)

for gesture in gestures:
    for _ in range(200):
        thumb = np.random.uniform(0, 90)
        index = np.random.uniform(0, 90)
        middle = np.random.uniform(0, 90)
        ring = np.random.uniform(0, 90)
        little = np.random.uniform(0, 90)

        data.append([gesture, thumb, index, middle, ring, little])

df = pd.DataFrame(
    data,
    columns=["gesture", "thumb", "index", "middle", "ring", "little"]
)

df.to_csv("dataset/gesture_dataset.csv", index=False)

print("Dataset generated successfully")