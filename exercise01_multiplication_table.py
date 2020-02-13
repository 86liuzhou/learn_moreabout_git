def multiple_table():

    row = 1
    while row < 10:
        col = 1
        while col <= row:
            # print("*",end=" ")
            print("%d * %d = %d" %(row,col,row*col) ,end="\t")
            col += 1
        print("")
        row += 1
multiple_table()

