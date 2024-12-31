import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1, detectionCon=0.8)

timer = 0
stateResult = False
startGame = False
scores = [0, 0]

winImage = cv2.imread("Resources/you_won.png", cv2.IMREAD_UNCHANGED)
winImage = cv2.resize(winImage, (400, 400))  

loseImage = cv2.imread("Resources/you_lose.png", cv2.IMREAD_UNCHANGED)
loseImage = cv2.resize(loseImage, (400, 400)) 

while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    hands, img = detector.findHands(imgScaled)

    if startGame:
        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0


                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1  # Rock
                    elif fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2  # Paper
                    elif fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3  # Scissors

                    randomNumber = random.randint(1, 3)
                    imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    if (playerMove == 1 and randomNumber == 3) or \
                        (playerMove == 2 and randomNumber == 1) or \
                        (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1

                    if (playerMove == 3 and randomNumber == 1) or \
                        (playerMove == 1 and randomNumber == 2) or \
                        (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1


    imgBG[234:654, 795:1195] = imgScaled

    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    
    if scores[0] == 2:
        imgBG = cvzone.overlayPNG(imgBG, loseImage, (450, 200))
        cv2.putText(imgBG, "You Lost!", (450, 700), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 3)
    elif scores[1] == 2:
        imgBG = cvzone.overlayPNG(imgBG, winImage, (450, 200))
        cv2.putText(imgBG, "You Won!", (450, 700), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 3)

    cv2.imshow("BG", imgBG)

    key = cv2.waitKey(3)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
        if scores[0] == 2 or scores[1] == 2:
            break
    elif key == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
