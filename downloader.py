import requests
import zlib

def download():
    URL = "https://datasets.imdbws.com/"
    URL += "name.basics.tsv.gz"


    print("Downloading file...")
    response = requests.get(URL, stream=True)
    print("Writing file...")
    open("data/name.basics.tsv.gz", 'w').write(response.text)
