import zipfile
import requests
board="b"
thread="921442765"
with zipfile.ZipFile('someZipFile.zip', 'w') as z: [z.writestr(i,requests.get(f"https://i.4cdn.org/{board}/{i}").content) for i in [str(i["tim"])+i["ext"] for i in requests.get(f"https://a.4cdn.org/{board}/thread/{thread}.json").json()["posts"] if "tim" in i.keys()]]
