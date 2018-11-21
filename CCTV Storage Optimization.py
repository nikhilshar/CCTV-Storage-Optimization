
# import the necessary packages
from skimage.measure import compare_ssim
import imutils
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Compressed.avi',fourcc, 20.0, (640,480))
ret,imageA=cap.read()
score1=1.0
while(cap.isOpened()):
    # load the two input images
    
    ret,imageB =cap.read()
    
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    
    
    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    #diff = (diff * 255).astype("uint8")
    
    print(score)
    
    if  (score1 - score) >-0.004 and (score1 -score)< 0.004  :
        continue
    else:
        score1=score
        out.write(imageB)
        imageA=imageB
       
    cv2.imshow("Out", imageB)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

 