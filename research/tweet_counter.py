import json
import matplotlib.pyplot as plt

f = open("tweet_data.json")
data = json.load(f)

d = {}
for i in range(0, 24): 
    for j in range(0, 56, 5): 
        d[f"{int(i/10)}{i%10}:{int(j/10)}{j%10}"] = 0 

for i in data:
    data_str = i['date'].split(":")
    hour = data_str[0][-2:]
    minute = data_str[1]

    for j in d:
        hour_dict = int(j.split(":")[0])
        minute_dict = int(j.split(":")[1])

        hour_str = j.split(":")[0]
        minute_str = j.split(":")[1]

        if (int(hour) == hour_dict and (int(minute) >= minute_dict and int(minute) < minute_dict + 5)): d[f"{hour_str}:{minute_str}"] += 1

X = [i for i in range(288)]        
Y = [d[i] for i in d]

plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes()
ax.plot(X, Y)
plt.axvline(x = 179, color = 'r')
plt.axvline(x = 191, color = 'r')
plt.show()