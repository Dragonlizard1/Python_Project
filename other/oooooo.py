words = "It's thanksgiving day. It's my birthday,too!"

words.find("day")

words.replace("day", "month", 1)

x = [2,54,-2,7,12,98]

min(x)

max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
temp = x[0]
temp1 = x[(len(x)-1)]
newarr = [temp, temp1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
listarr = x[0:5:1]
listarr2 = x[5:len(x):1]
listarr2.insert(0,listarr)
