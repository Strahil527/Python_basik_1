def requiredReading():
    number_page_current_book = int(input("Enter current book page: "))
    reading_page_hour = int(input("Enter page who reading per hour: "))
    number_day_read_book = int(input("Enter days who need to read book: "))

    need_time_read_book = number_page_current_book / reading_page_hour
    need_hour_per_day = need_time_read_book / number_day_read_book

    print(need_hour_per_day)

requiredReading()