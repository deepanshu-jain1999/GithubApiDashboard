hour = int(input())
minute = int(input())
hour_degree = hour*30 + minute/2
minute_degree = minute*6
print(abs(hour_degree-minute_degree))
