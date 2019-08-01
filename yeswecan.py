def get_highest_num (num, sequence):
    a = str(num)
    b = []

    for loop in range (len(a)-(sequence)+1):
        b.append(a[loop:sequence+loop])
        b.sort()
    return print('Yang terbesar', b[-1], 'dan inilah bukti') #untuk mencari yang paling besar

get_highest_num(12345,3)
# get_highest_num(17941077,3)
# get_highest_num(87173114, 5)


def sum_triangle(num):
    a = []
    b = 0
    c = 0
    e = 0
    z = ''
    for loop in range (num):
        for loop1 in range (1+loop):
            b +=1
            a.append(b)
            if loop1 == loop:
                z += '[' + str(a[c]) + ']'
                e += a[c]
            else:
                z += str(a[c]) + ' '
            c += 1
        z += '\n'
    return print(z,'sum of each last part of triangle',e,'\n')


sum_triangle(6)
# sum_triangle(3)
# sum_triangle(6)
        
    


