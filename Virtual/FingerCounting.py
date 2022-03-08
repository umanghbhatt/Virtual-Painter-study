"""Hand Tracking Module
"""

from .initialize import *

class FingerCounting:
    

    #folderpath = "Fingure_img"
    # myList = os.listdir(folderpath)
    # print(myList)

    # overlayList = []
    # for imPath in myList:
    #     image =cv2.imread(f'{folderpath}/{imPath}')
    #     #print(f'{folderpath}/{imPath}')
    #     overlayList.append(image)

    #print(len(overlayList))

    def countFingers(self):
        wCam , hCam =  648, 480
        cap = cv2.VideoCapture(0)
        cap.set(3,wCam)
        cap.set(4,hCam)
        
        pTime = 0
        #Detector
    

        tipIds = [4, 8, 12, 16, 20]

        detector = handDetector(detectionCon=0.6)
        while True:
            
            success , img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img,draw=False)
            #print(lmlist)

            if len(lmList) != 0:
                fingers = []

                #Thumb
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)


                #4 fingers
                for id in range(1,5):

                    if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

            # print(fingers)
                totalFingers = fingers.count(1)
                print(totalFingers)

                        #print("Index Finger Open")
                # h, w, c = overlayList[0].shape
                # img[0:h, 0:w] = overlayList[totalFingers-1]

                #cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(img,str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0) , 25)
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime

            cv2.putText(img,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,
                        3,(255,0,0,),3)

            ret, buffer = cv2.imencode('.jpg',img)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

        # cv2.imshow("Image",img)
        # cv2.waitKey(1)

        

