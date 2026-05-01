import pandas as pd

# Series: Use for 1D array
data = [100,200,300]
series = pd.Series(data, index=["a","b","c"])
print(series)

#-----------------------------------------------------#
# # DataFrame: Use for tabular data
# data = {
#     "Name": ["Ali","ALina","Aliza"],
#     "Job": ["Yapper","Capper","Wrapper"]
# }
# df = pd.DataFrame(data, index=["Id 1","ID 2","ID 3"])
# #adding a column
# df["Salary"] = ["0.10000$","50000 pkr","60000 pkr"]
# #Adding a row
# new_row_data = [{"Name":"Aliya", "Job":"Mapper", "Salary":"20000 pkr"}]
# new_row = pd.DataFrame(new_row_data, index=["ID 4"])
# df = pd.concat([df,new_row])
# print(df)
