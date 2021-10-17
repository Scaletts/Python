"""
Author: DuongTruongTho
Date: 09/08/2021
Program: Exersice_01_page_158.py
Problem:
      Give three examples of real-world objects that behave like a dictionary.

Solution:
    daily_price = {"ticker": "AAPL", "close price": 150.00, "daily high": 151.0, "daily low": 149.0, "volume": 2000000, "date": "2019-02-20"}
    
    price_history = [
    {"ticker": "AAPL", "close price": 148.00, "daily high": 152.0, "daily low": 147.0, "volume": 2000000, "date": "2019-02-18"},
    {"ticker": "AAPL", "close price": 149.00, "daily high": 150.0, "daily low": 146.0, "volume": 2000000, "date": "2019-02-19"},
    {"ticker": "AAPL", "close price": 150.00, "daily high": 151.0, "daily low": 149.0, "volume": 2000000, "date": "2019-02-20"}
    ]
    for dict in price_history:
    print("Date: %s" % dict['date'])
    print(dict['close price'])

    ftp_info = {"user_name": "bob", "password": "123abc", "host": ftp.whatever.com", "port": 22}
"""