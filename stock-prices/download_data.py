from yahoo_finance import Share
import csv
import time

with open("nasdaqlisted.txt", 'r') as f:
    data = f.read()

for line in data.split("\n")[1:]:
    symbol = line.split("|")[0]
    print("Downloading {}".format(symbol))
    try:
        stock = Share(symbol)
        data = stock.get_historical('2007-01-01', '2017-04-17')
        write = []
        write = [[d["Date"], d["Close"], d["Open"], d["High"], d["Low"], d["Volume"]] for d in data]

        write = sorted(write, key=lambda x:x[0])
        write.insert(0,["date", "close", "open", "high", "low", "volume"])
        with open("prices/{}.csv".format(symbol.lower()), "w+") as f:
            writer = csv.writer(f)
            writer.writerows(write)
    except Exception as e:
        print(e)
        print("Stock symbol too new for history from 2005")
    time.sleep(1)