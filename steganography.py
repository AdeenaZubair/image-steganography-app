import cv2
import numpy as np

cover = cv2.imread("cover.jpg")
secret = cv2.imread("secret.jpg")

secret = cv2.resize(secret, (cover.shape[1], cover.shape[0]))

stego = (cover & 254) | (secret >> 7)

cv2.imwrite("stego.png", stego)

print("Done")
