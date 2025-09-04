t =0 
for i in range(1,8):
    n = float(input(f"Enter temperatur of day {i} in °C: "))
    t +=n

avg = t/7

print("Average of 7 day temperatures = ", avg,"°C")