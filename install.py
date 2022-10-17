import urllib.request
import platform
import shutil
import os

version = platform.python_version()

def Download(url, path):
    urllib.request.urlretrieve(url,path)

def Unzip(filename, extract_dir):
    shutil.unpack_archive(filename, extract_dir)

def Install__3_9__1_7():
    ItemsToDownload = [
        ["https://22d78da4-551e-4018-a788-e9419ccd237e.usrfiles.com/archives/22d78d_4551993481b847f9a454a382c3c74832.zip", "main.zip", "main/"],
        ["https://22d78da4-551e-4018-a788-e9419ccd237e.usrfiles.com/archives/22d78d_ef5aa4fbbc2c4d288a5997aacfb98a15.zip", "pygame.zip", "main/"],
        ["https://22d78da4-551e-4018-a788-e9419ccd237e.usrfiles.com/archives/22d78d_f0766125bcb4484f9d2355cbf749cc20.zip", "requests.zip", "main/"],
        ["https://22d78da4-551e-4018-a788-e9419ccd237e.usrfiles.com/archives/22d78d_aa3ba115d1a2405abff1a6d1726774fe.zip", "paperclip.zip", "main/"]
        ]

    for item in ItemsToDownload:
        Download(item[0], item[1])
        Unzip(item[1], item[2])
        print("Downloaded & Extracted", item[1])

    for item in ItemsToDownload:
        if os.path.exists(item[1]):
            os.remove(item[1])
            print("Cleaned Up", item[1])


def Install__3_10__1_7():
    ItemsToDownload = [
        ["https://22d78da4-551e-4018-a788-e9419ccd237e.usrfiles.com/archives/22d78d_3a582cdbede545fa801433c54f3d43c2.zip", "main.zip", "main/"],
        ["https://22d78da4-551e-4018-a788-e9419ccd237e.usrfiles.com/archives/22d78d_48ab86b9559842fcbe8f74c4fc0e9cee.zip", "pygame.zip", "main/"],
        ["https://22d78da4-551e-4018-a788-e9419ccd237e.usrfiles.com/archives/22d78d_72801785955a4238924085bc55c6e798.zip", "requests.zip", "main/"]
        ]

    for item in ItemsToDownload:
        Download(item[0], item[1])
        Unzip(item[1], item[2])
        print("Downloaded & Extracted", item[1])

    for item in ItemsToDownload:
        if os.path.exists(item[1]):
            os.remove(item[1])
            print("Cleaned Up", item[1])



print("Detected Python Version", platform.python_version())
if version.startswith("3.9"): # If Version Is 3.9
    IN = input("Please Select A Version (1.7,):").lower()
    if IN == "1.7":
        Install__3_9__1_7()

elif version.startswith("3.10"):
    IN = input("Please Select A Version (1.7,):").lower()
    if IN == "1.7":
        Install__3_10__1_7()

else:
    print("Your Version Is Not Currently Supported.")
    print("Supported Versions: 3.9, ")


