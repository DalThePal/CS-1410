import numpy
import matplotlib.pyplot as plt
import os


VT = 100

def smoothArray(array):
    newArray = []
    for i in range(0, len(array)):
        if 2 < i < len(array) - 4:
            value = ((array[i - 3]) + (2 * array[i]) + (3 * array[i - 1]) + (3 * array[i + 1]) + (2 * array[i + 2]) + (array[i + 3]))
            newArray.append(value // 15)
        else:
            newArray.append(array[i])

    return numpy.asarray(newArray)
   
def plotArrays(array, smoothArray, fileName):
    _,axes = plt.subplots(nrows=2)
    xs = numpy.arange(len(array))
    ys = numpy.array(array)
    axes[0].plot(xs, ys, 'r')
    axes[0].set(title=fileName, ylabel="RAW", xticks=[])

    ys2 = numpy.array(smoothArray)
    axes[1].plot(xs, ys2)
    axes[1].set(ylabel="SMOOTH", xticks=[])
 
    newFile = fileName.replace('.dat', '.pdf')
    plt.savefig(newFile)

def readDatFile(fileName):
    file = open(fileName, 'r')
    content = file.readlines()
    file.close()
    lines = list(map(int, content))
    array = numpy.array(lines)
    newArray = smoothArray(array)
    pulses = locatePulse(array, newArray)
    writeOutFile(fileName, pulses)
    plotArrays(array, newArray, fileName)

def writeOutFile(fileName, pulses):
    newFile = fileName.replace('.dat', '.out')
    file = open(newFile, 'w')
    file.write(newFile + '\n')
    
    for i in range(0, len(pulses)):
        pulse = pulses[i]
        file.write("Pulse " + str(i + 1) + ": " + str(pulse['start'] + 1) + " (" + str(pulse['area']) + ")\n")

    file.close()

def locatePulse(rawArray, smoothArray):
    pulses = []
    search = "start"

    for i in range(0, len(smoothArray)-2):
        if search == "start":

            if ((smoothArray[i + 2]) - (smoothArray[i])) > VT:
                pulseStart = i
                if len(pulses):
                    width = pulseStart - pulses[-1]['start']
                    if width > 50:
                        width = 50
                    pulses[-1]['width'] = width

                    pulseArea = 0
                    for x in range(pulses[-1]['start'], pulses[-1]['start'] + width):
                        pulseArea += rawArray[x]
                    
                    pulses[-1]['area'] = pulseArea


                pulses.append({
                    "start": pulseStart,
                    "width": 0,
                    "area": 0
                })
                search = "decrease"
        if search == "decrease":
            if smoothArray[i + 1] < smoothArray[i]:
                search = "start"

    pulses[-1]['width'] = 50
    pulseArea = 0
    for x in range(pulses[-1]['start'], pulses[-1]['start'] + pulses[-1]['width']):
        pulseArea += rawArray[x]

    pulses[-1]['area'] = pulseArea
    return pulses

def main():

    for fileName in os.listdir('./'):
        if fileName.endswith(".dat"): 
            readDatFile(fileName)
            continue
        else:
            continue
        

main()