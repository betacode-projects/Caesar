import caesar

data1 = "happy birthday"
caesars = caesar.CaesarCipher()
print("["+ caesars.GetMoveString(data1, 4) +"]")

data2 = "lettc fmvxlhec"
print("["+ caesars.GetMoveString(data2, -4) +"]")

for data_ in caesars.GetMoveStringAll(data1):
    print(data_)

