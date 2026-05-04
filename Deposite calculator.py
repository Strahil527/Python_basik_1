def depositeCalculator():
    deposite_sum = int(input("Въведи депозирана сума: "))
    deposite_month = int(input("Въведи месеци на депозита: "))
    year_percent = float(input("Въведи годишен лихвен процент: "))

    sum = deposite_sum + deposite_month * ((deposite_sum * year_percent / 100) / 12)
    print(sum)

depositeCalculator()