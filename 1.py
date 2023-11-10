
for column in range(1,11):
    if column < 10:
        new_number = []
        new_number.append(f"умножение на {column}||")
        for  line in range(1,11):
            if line < 10:
                num = column * line
                new_number.append(num)
               
            else:
                print (new_number)
                continue
    else:
        break

    
