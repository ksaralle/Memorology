import os

path = "./audio"
want = []
def deleteFile(filename):
    list_dir = os.listdir("./audio")
    for i in list_dir:
        if filename == i:
            f = "./audio/%s" % i
            os.remove(f)
            break

def containsRecording(id):
    #filename = "%s.wav" % id
    list_dir = os.listdir("./audio")
    for i in list_dir:
        if id in i:
            return True
    return False


def generateNewFilename(id):
    id_audio = []
    list_dir = os.listdir("./audio")
    for i in list_dir:
        if id in i:
            print(i)
            id_audio += [i]
    # print(list_dir)
    # print(len(list_dir))
    # print(id_audio)
    newID = str(id) + str(len(id_audio))
    # print(newID)
    newFilename = "%s.wav" % newID
    return newFilename

print(os.listdir("./audio"))
id = "2\n.wav"
deleteFile(id)
print("---")
print(os.listdir("./audio"))

# print(generateNewFilename(id))
# iid = "hehe"
# print(containsRecording(iid))


# print(dir)
# dir_list = os.listdir(path)
# if (dir in dir_list) :
#     # print("yoooo")

# for i in dir_list:
#     if (i == "sensor.py"):
#         want += [i]


# print(path)
# print(dir_list)
# print(want)
