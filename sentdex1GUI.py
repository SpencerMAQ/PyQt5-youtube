inp = str(input("Enter: "))


#dasd = "dasdasd"
#dasd.len()
#print(inp[1])

let = 0
dig = 0

for i in range(len(inp)):
    if inp[i].isalpha():
        let += 1

    elif inp[i].isdigit():
        dig += 1

    else:
        pass

print("LET {0} NUM {1}".format(let, dig))
