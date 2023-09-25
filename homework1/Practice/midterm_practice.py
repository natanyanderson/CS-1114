acc = 0
for i in range(5,16,5):
    var = i
    while var > 0:
        var //= 2
        acc += var
        print("i=",i," var=",var)
    print("acc=",acc)