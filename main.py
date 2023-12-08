import downloader
import gzip

def main():
    print("Welcome, fellow film buff!")

    datafiles = {}
    for line in open("datafiles.csv", 'r').readlines():
        info = []
        for word in line.split(', '): info.append(word)
        datafiles.update({info[1]: (info[2], info[1])})









main()
