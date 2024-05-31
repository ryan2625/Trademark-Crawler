import openpyxl

cpm = [

]

arm = [

]

acom = [

]

other = [

]

def populateArr():
    df = openpyxl.load_workbook("prospects.xlsx")
    df1 = df.active
    for row in range(1, df1.max_row):
        print(row)
        if "CPM" in df1[row][3].value:
            cpm.append((df1[row][6].value, df1[row][7].value))
    
        elif "ARM" in df1[row][3].value:
            arm.append((df1[row][6].value, df1[row][7].value))
    
        elif "ACoM" in df1[row][3].value:
            acom.append((df1[row][6].value, df1[row][7].value))
        
        else:
            other.append((df1[row][6].value, df1[row][7].value))
            

    with open("CPM", "w") as file:
        for item in cpm:
            file.write(str(item) + ",\n")
    with open("arm", "w") as file:
        for item in arm:
            file.write(str(item) + ",\n")
    with open("acom", "w") as file:
        for item in acom:
            file.write(str(item) + ",\n")
    with open("other", "w") as file:
        for item in other:
            file.write(str(item) + ",\n")
    

populateArr()