import face_recognition
import picamera
import numpy as np
import time
import os
import gc

DIR_NAME = "/home/pi/.dingdang/contrib/datasets"
ENCODINGS = "/home/pi/.dingdang/contrib/encodings.npy"
REGISTERS = "/home/pi/.dingdang/contrib/registers.npy"
TH = 0.45


def get_fname(file_dir):
    file_list=[]
    for root, dirs, files in os.walk(file_dir):
        file_list.extend(files)
    return file_list


def reset(state=False):

    if not state:
        print("Invaild permisstion\n")
        return -1

    file_list = get_fname(DIR_NAME)
    names = []
    image_list = []
    face_encoding_list = []
    for fname in file_list:
        names.append(fname[0:-9])
        file_dir = DIR_NAME+"/"+str(fname)
        image_tmp = face_recognition.load_image_file(file_dir)
        image_list.append(image_tmp)
        encoding_tmp = face_recognition.face_encodings(image_tmp)[0]
        face_encoding_list.append(encoding_tmp)

    np.save(ENCODINGS,face_encoding_list)
    np.save(REGISTERS,names)

    return 1

def recognition(state=False):
    #K = 5
    recognization_state = False
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)

    # Load a sample picture and learn how to recognize it.
        encodings_0 = list(np.load(ENCODINGS))
        names_0 = list(np.load(REGISTERS))

        output_v = np.empty((320*240*3), dtype=np.uint8)

        face_locations = []
        face_encodings = []

        while (not recognization_state):
            print("Capturing image.")
            camera.capture(output_v, 'rgb')
            output = output_v.reshape((240,320,3))
            name = "Unknown"

        # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(output)
            print("Found {} faces in image.".format(len(face_locations)))
            face_encodings = face_recognition.face_encodings(output, face_locations)

        # Loop over each face found in the frame to see if it's someone we know.
            for face_encoding in face_encodings:

            # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces(encodings_0, face_encoding,tolerance=TH)


                for index,name_n in enumerate(names_0):
                    if match[index]:
                        recognization_state = True
                        name = name_n
                        break

                print("\nI see some one named {}\n".format(name))

            break


    return name, recognization_state



def add_id(state=False):

    if not state:
        print("Invaild permission\n")
        return -1,-1

    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)

    # Load a sample picture and learn how to recognize it.
        encodings_0 = list(np.load(ENCODINGS))
        names_0 = list(np.load(REGISTERS))

        output_v = np.empty((240*320*3), dtype=np.uint8)

        face_locations = []
        face_encodings = []

        while True:
            print("Capturing face.\nPlease face to the camera!\nAnd make sure only one face on the cam!\n\n")
            time.sleep(2)
            camera.capture(output_v, format="rgb")
            output = output_v.reshape((240,320,3))

            face_locations = face_recognition.face_locations(output)
            face_det = len(face_locations)
            if face_det<1:
                print("No face detected!Please face to the camera!\n\n")
                continue
            elif face_det>1:
                print("More than one face detected!\nPlease make sure only one face on the cam while adding identities!\n\n")
                continue

            while True:
               # name = raw_input("Face captured!Please input your name:")
                name = str(time.time())
                if len(name)<1:
                    continue
                break

            break

        encoding_n = face_recognition.face_encodings(output)[0]
        name_n = name

        encodings_0.append(encoding_n)
        names_0.append(name_n)

    np.save(ENCODINGS,encodings_0)
    np.save(REGISTERS,names_0)

    print("ID added successfully!")

    return encodings_0, names_0


def del_id(usrname, state=False):

    if not state:
        print("Invaild permission\n")
        return -1,-1

    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)

    # Load a sample picture and learn how to recognize it.
        encodings_0 = list(np.load(ENCODINGS))
        names_0 = list(np.load(REGISTERS))

        face_locations = []
        face_encodings = []

        name = raw_input("Please input name to delete:")

        if not(name in names_0):
            print("Name input is not found!\n")
            return [], []

        if (name == usrname):
            print("Can not remove the id which is being used!\n")
            return [], []
        elif (name == "LATEST"):
            name = names_0[-1]  

        con = raw_input("Name {} is found in the list, sure to remove it?[y/n]: ".format(name))
        if not(con=='y'):
            return [], []

        while(True):
            index = names_0.index(name)
            del names_0[index]
            del encodings_0[index]

            if not(name in names_0):
                break

    np.save(ENCODINGS,encodings_0)
    np.save(REGISTERS,names_0)
    print("Sucessfully remove {} from the list!\n".format(name))

    return encodings_0, names_0


