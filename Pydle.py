#146
#first attempt
for x in range(5):
    pydle(x, 0, "", "green")
    if x % 2 == 0: pydle(x, 1, "", "green")
    if x % 2 == 0: pydle(x, 4, "", "green")
    if x != 2: pydle(x, 2, "", "green")
for y in range(5):
    pydle(0, y, "", "green")
    pydle(4, y, "", "green")

    
