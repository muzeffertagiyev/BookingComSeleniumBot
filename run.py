from booking.booking import Booking



try:
    with Booking(teardown=False) as bot:
        bot.land_first_page()
        bot.change_currency('eur')
        bot.select_place_to_go(input("Where do you go? (city name): "))
        bot.select_dates(input("Check in date(yyyy-mm-dd): "), input("Check out date(yyyy-mm-dd): "))
        bot.select_adults_num(int(input("Number of people: ")))
        bot.click_search()
        bot.apply_filtration()
        bot.report_results(input("Please add your email: "))
        
        
except Exception as e:

    if "in PATH" in str(e):

        print(
            'You are trying to run the bot from command line\n'
            'Please add to the PATH your Selenium Drivers \n'
            'Windows: \n'
            '   set PATH=%PATH%;C:path-to-your-folder\n\n'
            'Linux: \n'
            '   PATH=$PATH:/path/toyour/folder\n'
        )
        
    else:
        raise


