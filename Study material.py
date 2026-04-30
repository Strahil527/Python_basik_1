def studyMaterial():
    packet_pen_price = 5.80
    packet_marker_price = 7.20
    preparate_price = 1.20

    quantity_packet_pen = int(input("Enter pen packets: "))
    quantity_packet_maerker = int(input("Enter marker packets: "))
    preparate_liters = int(input("Enter preparate liters: "))
    discount_percent = int(input("Enter discount: "))

    pen_sum = quantity_packet_pen * packet_pen_price
    marker_sum = quantity_packet_maerker * packet_marker_price
    preparate_sum = preparate_liters * preparate_price

    all_sum = pen_sum + marker_sum + preparate_sum
    sum_after_discount = all_sum - (all_sum * discount_percent / 100)

    print(sum_after_discount)

studyMaterial()