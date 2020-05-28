# Listas / Arrays / Vetores

```py

WipedOut = ["Prey", "Cry Baby", "Wiped Out!", "The Beach", "Daddy Issues", "Greetings From California", "Single", "R.I.P 2 My Youth"]

Romance = ["Shameless", "Should`ve Said It", "Liar", "Bad Kind Of Butterflies", "Easy", "Feel It Twice", "Cry For Me", "This Love", "Used To This", "First Man"]

playlist_FShinoda = ["Void", "Comes Then Goes", "Touch", "Alive", "7", "Honey Sweet", "Mr.Brightside", "Middle Of Somewhere", "Mystery Of Love"]

# playlist_FShinoda[0] -----> OUTPUT: 'Void'
# len(playlist_FShinoda) ------> OUTPUT: 9
# playlist_FShinoda[9] -----> OUTPUT: IndexError: list index out of range.
# playlist_FShinoda[-1] -----> OUTPUT: 'Mystery Of Love'
# playlist_FShinoda.append("Cool To You")
# playlist_FShinoda[4] = "7 - acoustic"
# new_playlist = []

classf_mus = [ 10, 10, 9, 10, 8, 9, 8, 9, 9]

# MANIP

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

primos[1:3] --> OUTPUT: [3, 5]
primos[:12] --> OUTPUT: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
primos[12:] --> OUTPUT: [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

final = primos[12:]

# CLONE
playlist1 = ["Stay", "Void", "Last One"]

playlist2 = playlist1

playlist2[1] = "Volcanic Love"

# Ambas apontam para o mesmo objeto! Não é um bom jeito de clonar uma lista!!

# clone:

playlist1 = ["Stay", "Void", "Last One"]

playlist2 = playlist1[:]

playlist2[0] = "Colors"
playlist2[1] = "Mystery of Love"
playlist2[2] = "7"

#pertinencia 

if "Void" in lista1:
    print("está")
else:
    print("não está")

#Concatenação de listas em listas

playlistOfc = playlist1 + playlist2


# DELETAR ELEMENTOS

a = [1, 2, 3, 4]

# del a[2] --> OUTPUT: [1, 2, 4]




        



```        
