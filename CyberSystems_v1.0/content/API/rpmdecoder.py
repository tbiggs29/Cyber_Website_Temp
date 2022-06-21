import json
import re
def decoder(file):
    with open(file, "r") as file:
        data = file.read()
    organizedData = re.split("\n |\n", data)
    organizedData = organizedData[1:len(organizedData)-1]
    returnData = {"Time": [],
                   "rpm": []}
    time = []
    dataID = []
    byteData = []
    for i in range(0, len(organizedData)):
        split = re.split("   |  ", organizedData[i])
        time.append(split[0][1:len(split[0])-1])
        dataID.append(split[2])
        byteData.append(split[4])
    for i in range(0, len(dataID)):
        pgn = dataID[i][2:6]
        if(int(pgn[0:2],16) < int("F0",16)):
            pgn = pgn[0:2] + "00"
        pgn = str(int(pgn, 16))
        if(pgn == "61444"):
            bytes = byteData[i].split(" ")
            rpmSpeed = str(int(bytes[4] + bytes[3], 16)*0.125)
            returnData["Time"].append(time[i])
            returnData["rpm"].append(rpmSpeed)
    return json.dumps(returnData, indent=3)