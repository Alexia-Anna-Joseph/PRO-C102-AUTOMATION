import cv2
import random
import time
import dropbox

start_time = time.time()

def take_snapshot():
    num = random.randint(1,100)
    #video capture object from cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
        return img_name
    print("Snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

    take_snapshot()

def upload_file(img_name):
    access_token = "sl.A_fG-lBqB1vLIhWjOYAw6-YMjyP2qI0qKfgNrMDxYlHKOuDdUoayclmticQ_Ozw4QkQZ1p1714O_14SeKxvzrIwPsjICYuOfQcVRZBo9bMtFBIz2tcF4j5YFC26dJKhp8a1ppOA"
    file_from = img_name
    file_to = "/pro 102 Automation/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 3):
            name = take_snapshot()
            upload_file(name)

main()