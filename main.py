# import os, time
# from influxdb_client_3 import InfluxDBClient3, Point

# token = "5Yr5yAQeXGZvBtAnxmmEO-1QB_yNm_Wcl4QucNPQAYxkdFt3s5W4nJoZytJr5NsSDhF-hKqbO4QwG4amZ4GoBQ=="
# org = "cb4877f469d97302"
# host = "https://us-east-1-1.aws.cloud2.influxdata.com"


# client = InfluxDBClient3(host=host, token=token, org=org)


# database="test"

# data = {
#   "point1": {
#     "location": "Klamath",
#     "species": "bees",
#     "count": 23,
#   },
#   "point2": {
#     "location": "Portland",
#     "species": "ants",
#     "count": 30,
#   },
#   "point3": {
#     "location": "Klamath",
#     "species": "bees",
#     "count": 28,
#   },
#   "point4": {
#     "location": "Portland",
#     "species": "ants",
#     "count": 32,
#   },
#   "point5": {
#     "location": "Klamath",
#     "species": "bees",
#     "count": 29,
#   },
#   "point6": {
#     "location": "Portland",
#     "species": "ants",
#     "count": 40,
#   },
# }

# for key in data:
#   point = (
#     Point("census")
#     .tag("location", data[key]["location"])
#     .field(data[key]["species"], data[key]["count"])
#   )
#   client.write(database=database, record=point)
#   time.sleep(1) # separate points by 1 second

# print("Complete. Return to the InfluxDB UI.")


x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = list();

for i in range(x+1):
    for j in range(y+1):
      for k in range(z+1): 
        #  if i + j + k != n:
        print([i, j, k])
        result.append([i, j, k])

      
# print(result)

# print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))