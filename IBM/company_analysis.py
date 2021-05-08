import pandas as pd
import matplotlib.pyplot as plt


my_IBM = pd.read_csv("D:\MyPrj2\IBM.csv", delimiter=';')
my_df = pd.DataFrame(my_IBM)

arr_year = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
arr_month = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
             "декабрь"]
sum_vol = [0] * 12
count_close = [0] * 9
sum_on_close = [0] * 9

for i in range(len(my_df["<VOL>"])):
    temp = (my_df["<DATE>"][i])[3:5]
    if temp == "01":
        sum_vol[0] += my_df["<VOL>"][i]
    elif temp == "02":
        sum_vol[1] += my_df["<VOL>"][i]
    elif temp == "03":
        sum_vol[2] += my_df["<VOL>"][i]
    elif temp == "04":
        sum_vol[3] += my_df["<VOL>"][i]
    elif temp == "05":
        sum_vol[4] += my_df["<VOL>"][i]
    elif temp == "06":
        sum_vol[5] += my_df["<VOL>"][i]
    elif temp == "07":
        sum_vol[6] += my_df["<VOL>"][i]
    elif temp == "08":
        sum_vol[7] += my_df["<VOL>"][i]
    elif temp == "09":
        sum_vol[8] += my_df["<VOL>"][i]
    elif temp == "10":
        sum_vol[9] += my_df["<VOL>"][i]
    elif temp == "11":
        sum_vol[10] += my_df["<VOL>"][i]
    elif temp == "12":
        sum_vol[11] += my_df["<VOL>"][i]
table1 = pd.Series(sum_vol, arr_month)
print("Суммарный объем сделок по месяцам:")
print(table1)
for i in range(len(my_df["<CLOSE>"])):
    temp = (my_df["<DATE>"][i])[6:]
    if temp == "12":
        count_close[0] += 1
        sum_on_close[0] += my_df["<CLOSE>"][i]
    elif temp == "13":
        count_close[1] += 1
        sum_on_close[1] += my_df["<CLOSE>"][i]
    elif temp == "14":
        count_close[2] += 1
        sum_on_close[2] += my_df["<CLOSE>"][i]
    elif temp == "15":
        count_close[3] += 1
        sum_on_close[3] += my_df["<CLOSE>"][i]
    elif temp == "16":
        count_close[4] += 1
        sum_on_close[4] += my_df["<CLOSE>"][i]
    elif temp == "17":
        count_close[5] += 1
        sum_on_close[5] += my_df["<CLOSE>"][i]
    elif temp == "18":
        count_close[6] += 1
        sum_on_close[6] += my_df["<CLOSE>"][i]
    elif temp == "19":
        count_close[7] += 1
        sum_on_close[7] += my_df["<CLOSE>"][i]
    elif temp == "20":
        count_close[8] += 1
        sum_on_close[8] += my_df["<CLOSE>"][i]
sr_cost_close = [0] * 9
for i in range(9):
    sr_cost_close[i] = round(sum_on_close[i] / count_close[i], 3)
table2 = pd.Series(sr_cost_close, arr_year)
print("Средняя цена акций во время закрыий по годам:")
print(table2)

plt.figure(figsize=(12, 9))
plt.title("Суммарный объем сделок по месяцам", fontsize=16)
plt.bar(arr_month, sum_vol, color='green', edgecolor='black')
plt.show()