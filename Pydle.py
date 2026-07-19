#0
#first attempt
for x in range(5):
    if x < 3: pydle(x, 0, "", "blue")
    if x in (0, 2): pydle(x, 1, "", "blue")
    if x < 2: pydle(x, 2, "", "blue")
    if x in (2, 4): pydle(x, 2, "", "yellow")
    if x in (3,): pydle(x, 3, "", "yellow")
    if x in (2,): pydle(x, 4, "", "yellow")
for y in range(5):
    pydle(0, y, "", "blue") 
    
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

    
