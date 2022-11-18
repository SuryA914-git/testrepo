import pandas as pd
pd.read_excel('Records Matching Task.xlsx')
pd.read_excel('Records Matching Task.xlsx')
Data_1 = pd.read_excel('Records Matching Task.xlsx', usecols = "A:B", sheet_name = 0)
Data_2 = pd.read_excel('Records Matching Task.xlsx', usecols = "A:B", sheet_name = 1)
#print(Data_1)
#print()
#print(Data_2)
order_id_1 = list(Data_1.Order_ID)
product_id_1 = list(Data_1.Product_ID)
order_id_2 = list(Data_2.Order_ID)
product_id_2 = list(Data_2.Product_ID)
data_1_dict = {}
data_1_list = []
for order in order_id_1:
    for product in product_id_1:
        data_1_dict[order] = {product}
        #data_1_list.append([order,product])

#print(data_1_dict)
data_2_dict = {}
#data_2_list = []
for order in order_id_1:
    for product in product_id_1:
        data_2_dict[order] = {product}
        #data_1_list.append([order,product])

#print(data_2_dict)

len_data1 = len(data_1_dict)
print(len_data1)

len_data2 = len(data_2_dict)
print(len_data2)
number = 0
i=0
j=0
for i in range(len_data1):
    for j in range(len_data2):
        if data_1_dict[i] == data_2_dict[j]:
            number+= 1
print(number)
