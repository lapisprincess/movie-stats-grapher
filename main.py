import downloader
import gzip

prompt = input("Update file? ")
if 'y' in prompt: downloader.download()
print(gzip.open("data/name.basics.tsv.gz").read())