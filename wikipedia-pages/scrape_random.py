file_max = 3000
counter = 0
import requests
import time

random_url = "http://en.wikipedia.org/wiki/Special:Random"

while counter < file_max:
    if counter % 1000 == 0:
        print("On {}".format(counter))
    try:
        data = requests.get(random_url)
        content = data.content.decode("utf-8")
        if len(content) > 0:
            end = data.url.split("/")[-1]
            with open("wiki/{}.html".format(end), "w+") as f:
                f.write(content)
                counter += 1
    except Exception as e:
        print(e)
    time.sleep(1.5)