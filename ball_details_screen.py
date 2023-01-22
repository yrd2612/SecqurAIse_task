import numpy as np
import cv2
import time
time_y = []
time_o = []
time_g = []
time_w = []
quad_y = []
quad_o = []
quad_g = []
quad_w = []
text_y = []

q = 0
start =time.time()
stage_y = 0
yellow = False
f = open("myfile.txt", "w")
color = ["yellow","orange","green","white"]
cap = cv2.VideoCapture("D:/internship assignments/ball colour/video.mp4")
# def quadrant(b,a,quad):
#     if b>1252 and b<1735 and a>543 and a<1011:
#         quad = 1
#     if b>786 and b<1217 and a>543 and a<1010:
#         quad = 2
#     if b>786 and b<1217 and a>24 and a <507:
#         quad = 3
#     if b>1252 and b<1735 and a>24 and a<507:
#         quad = 4
#     return(quad)
while(cap.isOpened()):
    success,img = cap.read()
    if success == True:
        cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Resized_Window", 1920, 1080)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(17,17),0)
        circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1.4,90,param1=45,
        param2=35,minRadius=40,maxRadius=100)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for pt in circles [ 0, :]:
                    a,b,r = pt[0],pt[1],pt[2]            
                    cv2.circle(img,(a,b),r,(0,255,0),4)
                    b,g,r = img[b, a]
                    rgb = r,g,b
                    # quadrant(b,a,quad)
                    
                    # cv2.putText(img,str(rgb),(a,b),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),thickness=2)
                    # yellow colour
                    if r<160 and r>110 and g>104 and g<128 and b>39 and b<45:
                        if pt[0]>1252 and pt[0]<1735 and pt[1]>543 and pt[1]<1011:
                            q = 1
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>543 and pt[1]<1010:
                            q = 2
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>24 and pt[1] <507:
                            q = 3
                        elif pt[0]>1252 and pt[0]<1735 and pt[1]>24 and pt[1]<507:
                            q = 4
                        quad_y.append(q)
                        end_y = time.time()
                        time_y_i = end_y-start
                        time_y.append(int(time_y_i))
                        y_1 = ['\n',color[0]," appeares at ",str(time_y[0]), " at quadrant ",str(quad_y[-1]),'\n']
                        y_2 = ['\n',color[0]," dissapears at ",str(time_y[-1]),'\n']
                        # text_y.append(int(time_y_i),color[0])
                        # text_y.append(color[0])
                        cv2.putText(img,color[0],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        cv2.putText(img,str(int(time_y_i)),(pt[0],pt[1]+50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        
                        try:
                            if time_y[-1] - time_y[-2]>3:
                                f.writelines(y_1)
                                f.writelines(y_2)
                                time_y.clear()
                        except:
                            pass
                        # Orange colour
                    if r<230 and r>210 and g>105 and g<130 and b>80 and b<105:
                        if pt[0]>1252 and pt[0]<1735 and pt[1]>543 and pt[1]<1011:
                            q = 1
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>543 and pt[1]<1010:
                            q = 2
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>24 and pt[1] <507:
                            q = 3
                        elif pt[0]>1252 and pt[0]<1735 and pt[1]>24 and pt[1]<507:
                            q = 4
                        quad_o.append(q)
                        end_o = time.time()
                        time_o_i = end_o-start
                        time_o.append(int(time_o_i))
                        cv2.putText(img,color[1],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        cv2.putText(img,str(int(time_o_i)),(pt[0],pt[1]+50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        try:
                            o_1 = ['\n',color[1]," appeares at ",str(time_o[0])," at quadrant ",quad_o[-1],'\n']
                            o_2 = ['\n',color[1]," dissapears at ",str(time_o[-1])," at quadrant ",quad_o[-1],'\n']

                            if time_o[-1] - time_o[-2]>2:
                                f.writelines(o_1)
                                f.writelines(o_2)
                                time_o.clear()
                        except:
                            pass 
                        #green color
                    if r<55 and r>30 and g>65 and g<90 and b>66 and b<99:
                        if pt[0]>1252 and pt[0]<1735 and pt[1]>543 and pt[1]<1011:
                            q = 1
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>543 and pt[1]<1010:
                            q = 2
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>24 and pt[1] <507:
                            q = 3
                        elif pt[0]>1252 and pt[0]<1735 and pt[1]>24 and pt[1]<507:
                            q = 4
                        quad_g.append(q)
                        end_g = time.time()
                        time_g_i = end_g - start 
                        time_g.append(int(time_g_i))
                        cv2.putText(img,color[2],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        cv2.putText(img,str(int(time_g_i)),(pt[0],pt[1]+50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        try:
                            g_1 = ['\n',color[2]," appeares at ",str(time_g[0]),"at quadrant",quad_g[-1],'\n']
                            g_2 = ['\n',color[2]," dissapears at ",str(time_g[-1]),"at quadrant",quad_g[-1],'\n']
                            if time_g[-1] - time_g[-2]>2:
                                f.writelines(g_1)
                                f.writelines(g_2)
                                time_g.clear()
                        except:
                            pass 
                        # white color
                        if r<190 and r>160 and g>180 and g<190 and b>140 and b<170:
                            if pt[0]>1252 and pt[0]<1735 and pt[1]>543 and pt[1]<1011:
                                q = 1
                            elif pt[0]>786 and pt[0]<1217 and pt[1]>543 and pt[1]<1010:
                                q = 2
                            elif pt[0]>786 and pt[0]<1217 and pt[1]>24 and pt[1] <507:
                                q = 3
                            elif pt[0]>1252 and pt[0]<1735 and pt[1]>24 and pt[1]<507:
                                q = 4
                            quad_w.append(q)
                            end_w = time.time()
                            time_w_i = end_w - start 
                            time_g.append(int(time_g_i))
                            w_1 = ['\n',color[3]," appeares at ",time_w[0]," at quadrant ",quad_w[-1]]
                            w_2 = ['\n',color[3]," dissapears at ",time_w[-1]," at quadrant ",quad_w[-1]]
                            cv2.putText(img,color[3],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                            cv2.putText(img,str(int(time_w_i)),(pt[0],pt[1]+50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                            try:
                                if time_g[-1] - time_g[-2]>2:
                                    f.writelines(w_1)
                                    f.writelines(w_2)
                                    time_w.clear()
                            except:
                                pass                    
                                      


        cv2.imshow('Resized_Window',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()