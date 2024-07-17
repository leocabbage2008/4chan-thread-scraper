import zipfile
import requests
link="https://boards.4chan.org/b/thread/921442765"
board=link.split("/thread")[0].split("/")[-1]
thread=link.split("/")[-1]
with zipfile.ZipFile('someZipFile.zip', 'w') as z: [z.writestr(i,requests.get(f"https://i.4cdn.org/{board}/{i}").content) for i in [str(i["tim"])+i["ext"] for i in requests.get(f"https://a.4cdn.org/{board}/thread/{thread}.json").json()["posts"] if "tim" in i.keys()]]
