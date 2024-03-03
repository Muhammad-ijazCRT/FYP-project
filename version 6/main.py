import cv2
import mediapipe as mp
import time
from directkeys import right_pressed,left_pressed
from directkeys import PressKey, ReleaseKey  
import joblib


break_key_pressed=left_pressed
accelerato_key_pressed=right_pressed

time.sleep(2.0)
current_key_pressed = set()

mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands


tipIds=[4,8,12,16,20]

video=cv2.VideoCapture(0)
global my_break

my_break = 0
with mp_hand.Hands(min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
    while True:
        keyPressed = False
        break_pressed=False
        accelerator_pressed=False
        key_count=0
        key_pressed=0
        ret,image=video.read()
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList=[]
        # lmList2=[]
        
        
        
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers=[]
        
        
        if len(lmList)!=0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # initializing list
            test_list = fingers

            res = [ test_list[1], test_list[4] ]
            sec = [ test_list[0], test_list[2], test_list[3] ]
            
            vec_open = [ test_list[1], test_list[2] ]
            vec_close = [ test_list[0], test_list[3], test_list[4] ]
            

            three_open = [ test_list[1], test_list[2], test_list[3],test_list[4] ]
            three_close = [ test_list[0]]
        
            total=fingers.count(1)
            # print(total)
            if total==0:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                PressKey(break_key_pressed)
                break_pressed=True
                current_key_pressed.add(break_key_pressed)
                key_pressed=break_key_pressed
                keyPressed = True
                key_count=key_count+1
                
            elif total==5:
                
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, " GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)

                PressKey(accelerato_key_pressed)
                key_pressed=accelerato_key_pressed
                accelerator_pressed=True
                keyPressed = True
                current_key_pressed.add(accelerato_key_pressed)
                key_count=key_count+1


        if not keyPressed and len(current_key_pressed) != 0:
            my_break += 1
            print(my_break)
        
            # starttime = 0
            # endtime = 0
            # if vec_open == [1,1] and vec_close == [0,0,0]: #For ENTER
                
            #     starttime = time.time()
            #     print('Started')
            # elif KeyboardInterrupt: 
            #     endtime = time.time()
            #     print('Total Time:', int(endtime - starttime),'secs') 
            #     print('Data Sent...')
            #     # my_break = 0
        
            
            
            if res == [1,1] and sec == [0,0,0]:
                # name = My_car.objects.all()
                # q = My_car(gas = my_break)
                # q.save()
                print('Data Sent...')
                my_break = 0
                # starttime = 0

                
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
        elif key_count==1 and len(current_key_pressed)==2:
            for key in current_key_pressed:
                if key_pressed!=key:
                    # if fingers == [0,0,0,0,0]:
                    #     my_break += 1
                    #     print(my_break)
                    ReleaseKey(key)
                    
                    
            current_key_pressed = set()
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
            # if lmList[8][2] < lmList[6][2]:
            #     print("Open")
            # else:
            #     print("Close")
        
        

        
        cv2.imshow("Frame",image)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
video.release()
cv2.destroyAllWindows()
