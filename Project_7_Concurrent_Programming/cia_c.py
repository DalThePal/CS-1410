import requests
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor


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
    print('downloading ' + str(country))
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

    with ThreadPoolExecutor(max_workers=5) as executor:

      for country in countries:

        executor.submit(loadUrl, country)
      

    end = perf_counter()
    time = end - start

    print('elapsed time: ' + str(time))
    print(str(downloaded) + ' bytes downloaded')

if __name__ == '__main__':
  main()