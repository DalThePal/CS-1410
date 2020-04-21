import requests
import json
from time import perf_counter

BASE_URL = "https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/"
FILE_EXT = "-lgflag.gif"
downloaded = 0


def downloadFlags():
    global downloaded
    file = open('./flags.txt', 'r')
    countries = file.read().splitlines()
    file.close()
    
    for country in countries:
        flagUrl = BASE_URL + country + FILE_EXT
        flag = requests.get(flagUrl)

        flagSize = int(flag.headers["Content-Length"])
        downloaded += flagSize

        flagFile = open(country + FILE_EXT, 'wb')
        flagFile.write(flag.content)
        flagFile.close()



def main():
    start = perf_counter()
    downloadFlags()
    end = perf_counter()
    time = end - start

    print('elapsed time: ' + str(time))
    print(str(downloaded) + ' bytes downloaded')

main()