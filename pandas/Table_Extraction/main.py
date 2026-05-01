import pandas as pd

data = pd.read_csv("https://www.football-data.co.uk/mmz4281/2526/E0.csv")

update_data = data.rename(columns={"Date": "tareeq",
                                   "Time": "Waqt"
                                   })
print(update_data)