from rembg import remove
import cv2

def bg_remover(input):
    output = remove(input)
    return output