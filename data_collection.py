import cv2
import os

directory_path = "data/color/"
game_name = input('What is the game you are capturing: ')
i = int(input('What is the starting picture number: '))

cam = cv2.VideoCapture(0)
cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)

while cam.isOpened():
    ret, frame = cam.read()

    cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):  # Save image when 's' is pressed
        image_path = directory_path+game_name+str(i)+'.png'
        cv2.imwrite(image_path, frame)
        i += 1
        print("Image saved!")
    elif key == ord('q'):  # Quit when 'q' is pressed
        print("Quitting...")
        break

cam.release()

cv2.destroyAllWindows()
