#Python3

idadeDia = int(input())

idadeAno = idadeDia // 365
idadeDia = idadeDia % 365

idadeMes = idadeDia // 30
idadeDia = idadeDia % 30

print("{} ano(s)".format(idadeAno))
print("{} mes(es)".format(idadeMes))
print("{} dia(s)".format(idadeDia))

