#Python3

durSeg = int(input())

durHora = 0
durMin = 0

durHora = durSeg // 3600
durSeg = durSeg % 3600

durMin = durSeg // 60
durSeg = durSeg % 60

print("{}:{}:{}".format(durHora,durMin,durSeg))

