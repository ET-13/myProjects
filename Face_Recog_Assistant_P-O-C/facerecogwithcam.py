import cv2
import face_recognition
from PIL import Image, ImageDraw
import os
import playsound
from gtts import gTTS


cv2.namedWindow("Face_Scan")
vc = cv2.VideoCapture(0)
img_counter = 0
identity = 0


if vc.isOpened(): 
    rval, frame = vc.read()

else:
    rval = False

while rval:
    cv2.imshow("Face_Scan", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)

    if key == 27: # exit on ESC
        break

    elif key%256 == 32:
        img_name = "opencv_frame.png"
        cv2.imwrite(img_name, frame)
        print("image frame written".format(img_name))
        img_counter += 1




    #test screenshot against database below


if img_counter > 0:

    image_of_vinz = face_recognition.load_image_file('./Database/vinzcasseldatabase.jpg')
    vinz_face_encoding = face_recognition.face_encodings(image_of_vinz)[0]

    image_of_hubert = face_recognition.load_image_file('./Database/hubertdatabase.jpg')
    hubert_face_encoding = face_recognition.face_encodings(image_of_hubert)[0]

    image_of_remi = face_recognition.load_image_file('./Database/remidatabase.jpg')
    remi_face_encoding = face_recognition.face_encodings(image_of_remi)[0]

    known_face_encoings = [vinz_face_encoding, hubert_face_encoding, remi_face_encoding]
    known_face_names = ["Vinz Cassel", "Hubert", "Remi"]

    test_image = face_recognition.load_image_file("opencv_frame.png")

    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    pil_image = Image.fromarray(test_image)

    draw = ImageDraw.Draw(pil_image)
    #loop through faces in test image
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encoings, face_encoding)

        name = "Unknown Person" + " "  + "|" + " " + "Access_DENIED"
       
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            identity = 1
            
        
        #draws a box
        draw.rectangle(((left,top),(right,bottom)), outline =(0,0,0))

        #draw label
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0),
        outline=(0,0,0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))


    del draw
    ##alternatively can catalog the image taken instead of delete

    #display
    pil_image.show()
    


 


##deletes screenshot afterward for cleanup
deletescreenshot = "rm" + " " + "opencv_frame.png"
os.system(deletescreenshot)


cv2.destroyWindow("Face_Scan")

#identity counter
if identity == 1:
  
    os.system("pwd")
    runassistantscript = "python3" + " " + "speechassistantfacerecog.py"
    os.system(runassistantscript)
    









    





##if face matches database run assistant script



