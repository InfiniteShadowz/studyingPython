#python3

segundos = int(input())

dias = segundos // (3600 * 24)
segundosRest = segundos % (3600 *24)

horas = segundosRest // 3600
segundosRest %= 3600

minutos = segundosRest // 60
segundosRest %= 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundosRest, "segundos")

