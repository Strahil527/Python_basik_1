def basketballEquipment():
    annul_fee_one_year = int(input("Въведете годишната сума: "))
    shoes_price = annul_fee_one_year - (annul_fee_one_year * 0.40)
    team_price = shoes_price - (shoes_price * 0.20)
    basketball_ball = team_price / 4
    basketball_accessoar = basketball_ball / 5

    need_sum = annul_fee_one_year + shoes_price + team_price + basketball_ball + basketball_accessoar

    print(need_sum)

basketballEquipment()