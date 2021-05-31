numbers = []
for i in range(3):
    a = []
    for j in range(3):
        a.append(3*i + j+1)
    numbers.append(a)
numbers[2][2] = 0
# print(numbers)
# print(numbers[2][2])
# gra musi zawierać powyższą listę żeby możliwy był ruch i późniejsze sprawdzenie czy zadanie zostało wykonane

def movement(list, rng = 3):  # tutaj brakuje jeszcze uzupełnienia o zmianę pozycji obrazków
    _i = 0
    _j = 0
    for i in range(rng):  # pętla która znajduje pustą kratkę
        for j in range(rng):
            if list[i][j] == 0:
                _i = i
                _j = j
    if _i != 0:  #ruch do góry
        list[_i][_j] = list[_i - 1][_j]
        list[_i - 1][_j] = 0
    elif _i != 2:  #ruch do góry
        list[_i][_j] = list[_i + 1][_j]
        list[_i + 1][_j] = 0
    elif _j != 0:  #ruch w lewo
        list[_i][_j] = list[_i - 1][_j]
        list[_i - 1][_j] = 0
    elif _j != 2:  #ruch w prawo
        list[_i][_j] = list[_i][_j + 1]
        list[_i][_j + 1] = 0

# tu sobie tak testowałem czy to działa w ogóle i działa :D
# print(numbers)
# movement(numbers)
# print(numbers)
# movement(numbers)
# print(numbers)
# movement(numbers)
# print(numbers)
