ls = [1, 2, 3, 4, 5, 6, 7]

ind = input()

try:
    print(ls[int(ind)])

except ValueError:
    print("Not valid input!")
except IndexError:
    print("Not in range!")
else:
    print("Suxess!")
finally:
    print("Fineshed!")
