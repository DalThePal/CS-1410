import requests
from time import perf_counter
import concurrent.futures


BASE_URL = "https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/"
FILE_EXT = "-lgflag.gif"
downloaded = 0
countries = None


def readFile():
    global countries
    file = open('./flags.txt', 'r')
    countries = file.read().splitlines()
    file.close()



def loadUrl(country):
    global downloaded

    flagUrl = BASE_URL + country + FILE_EXT
    flag = requests.get(flagUrl)

    flagSize = int(flag.headers["Content-Length"])
    downloaded += flagSize

    flagFile = open(country + FILE_EXT, 'wb')
    flagFile.write(flag.content)
    flagFile.close()


def main():
    start = perf_counter()
    readFile()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
      futureData = {executor.submit(loadUrl, country, 60): country for country in countries}
      for flag in concurrent.futures.as_completed(futureData):
        request = futureData[flag]
        print(request)
        try:
            data = flag.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))


    end = perf_counter()
    time = end - start

    print('elapsed time: ' + str(time))
    print(str(downloaded) + ' bytes downloaded')

main()