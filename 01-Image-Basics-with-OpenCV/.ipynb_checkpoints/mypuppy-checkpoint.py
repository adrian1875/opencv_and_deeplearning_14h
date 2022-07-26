import cv2

img  = cv2.imread('../DATA/00-puppy.jpg')

while True:

    cv2.imshow('Puppy', img)

    # if cv2.waitKey():  # 기본적으로 특정 밀리초 만큼 기다린다
    if cv2.waitKey(1) & 0xff == 27:  # 1ms만큼 기다림 AND esc를 누름 
        break
    
cv2.destroyAllWindows()