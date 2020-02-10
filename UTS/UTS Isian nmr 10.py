trips = [[x-1,x,x+1] for x in range(1,4)]
for t in trips:
    t.remove(2)
trips.reverse()
print(trips)
