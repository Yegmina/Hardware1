def power(local_n, local_power):
    try:
        #n=int(input("number"))
        if local_power==0:
            return 1
        result=int(local_n)**int(local_power)
        #print(result)
        return int(result)
    except Exception as e:
        print(e)

#n=int(input("number "))


def converting_int_to_base_10(local_number, local_base):
    try:
        local_length=int(len(str(local_number)))
        local_number=int(local_number)
        local_base=int(local_base)
        local_sum=int(0)
        for i in range(local_length):
            current_digit = (local_number // (10 ** i)) % 10
            #print(current_digit)
            #print(local_sum)
            local_sum=local_sum+power(local_base,i)*current_digit

        return local_sum

    except Exception as e:
        print(e)


"""
print(converting_int_to_base_10(101,3))
print(converting_int_to_base_10(1000,2))
print(converting_int_to_base_10(10001,2))
"""

#print(bin(ord("E")))
print(converting_int_to_base_10(10001,2))

