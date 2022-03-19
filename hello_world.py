import string

# how to remove all the non string elements



# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#  digits = '0123456789'
#  ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#  hexdigits = '0123456789abcdefABCDEF'
# octdigits = '01234567'
#  printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# whitespace = ' \t\n\r\x0b\x0c'
def extra_strings(stringof):
    uppercase = string.ascii_letters
    digits = string.digits
    hexadecimals = string.hexdigits
    printable = string.printable
    whitespace = string.whitespace
    punctation = string.punctuation
    n_var = [digits, whitespace, punctation]
    length_of_string = len(stringof)

    for i in stringof:
        k = 0
        print("value of k is:" + str(k))
        while k<=2:
            for j in n_var[k]:
                if i == str(j):
                    length_of_string = length_of_string - 1
                print("value of i is:" +str(i))
                print("value of j is:" +str(j))
            k = k+1

    print(length_of_string)










def funtime():
    print("this is the way to concatenate>>")
    stringof = str(input("enter the string you want:"))

    extra_strings(stringof)
    print(stringof)


funtime()