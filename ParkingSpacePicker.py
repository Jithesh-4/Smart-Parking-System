import cv2
import pickle

width, height = 103, 43
try:
    with open('polygons', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('polygons', 'wb') as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread('carParkImg.png')
    if img is None:
        print("Error: Could not load the image file 'carParkImg.png'. Ensure it exists.")
        break

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    key = cv2.waitKey(1)
    if key == ord('q'):  # Press 'q' to quit
        break

cv2.destroyAllWindows()
