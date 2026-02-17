full_name = "DoprajnaSaiVadlamudi"
L = len(full_name)
r = int(input("Enter no of resource requests:"))
req = []

for i in range(r):
    res = int(input("Enter the resource request:"))
    req += [res]

low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []
valid_requests = 0
removed = 0
no_demand = 0

for i in range(r):
    if(req[i] < 0):
        print(req[i],"-->Invalid Request")
        invalid_requests += [req[i]]

    elif(req[i] == 0):
        print(req[i],"-->No Demand")
        valid_requests += 1
        no_demand += 1

    elif(req[i] <= 20):
        print(req[i],"-->Low Demand")
        low_demand += [req[i]]
        valid_requests += 1

    elif(req[i] <= 50):
        print(req[i],"-->Moderate Demand")
        moderate_demand += [req[i]]
        valid_requests += 1

    elif(req[i] > 50 ):
        print(req[i],"-->High Demand")
        high_demand += [req[i]]
        valid_requests += 1

print("Before personalization:")
print("Invalid Request",invalid_requests)
print("Low Demand",low_demand)
print("Moderate Demand",moderate_demand)
print("High Demand",high_demand)
print("Total Valid Students:",valid_requests)

print("Full Name:",full_name)
print("length of full name(L):",L)
PLI = L % 3
print("PLI:",PLI)

print("After Personalization:")
if(PLI == 0):
    print("As PLI = 0 Remove all Low Demand requests")
    removed = len(low_demand)
    low_demand = []

elif(PLI == 1):
    print("As PLI = 1 Remove all high Demand requests")
    removed = len(high_demand)
    high_demand = []

elif(PLI == 2):
    print("As PLI = 2 Keep only moderate Demand requests")
    removed = len(low_demand) + len(high_demand) + no_demand + len(invalid_requests)
    low_demand = []
    high_demand = []
    invalid_requests = []

print("Removed due to personalization:",removed)
print("invalid requests:",invalid_requests)
print("Low Demand",low_demand)
print("Moderate Demand",moderate_demand)
print("High Demand",high_demand)


