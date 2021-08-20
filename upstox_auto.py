import cv2
import numpy as np
import pyautogui

buyPixel = [245, 185, 97]
sellPixel = [96, 64, 176]

buy_flag = 1
sell_flag = 0

while True:
    # take a screenshot
    img = pyautogui.screenshot(region=(2200, 410, 200, 450))
    # img = pyautogui.screenshot(region=(2200, 675, 20, 20))

    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)

    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    for pixelValues in frame:
        for pixelValue in pixelValues:
            pixelValueList = pixelValue.tolist()
            
            if pixelValueList[0] == buyPixel[2] and pixelValueList[1] == buyPixel[1] and pixelValueList[2] == buyPixel[0] and buy_flag:
                print("\n\nBuy!!!!\n\n")
                buy_flag = 0
                sell_flag = 1
            elif pixelValueList[0] == sellPixel[2] and pixelValueList[1] == sellPixel[1] and pixelValueList[2] == sellPixel[0] and sell_flag:
                print("\n\n---------------- Sell ----------------\n\n")
                buy_flag = 1
                sell_flag = 0

    cv2.imshow("Screen", frame)

    # if the user clicks q, it exits
    if cv2.waitKey(5) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()