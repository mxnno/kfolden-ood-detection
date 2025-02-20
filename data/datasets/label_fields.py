#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# file: label_fields.py


def get_labels(data_sign, dist_sign="id"):
    if data_sign == "agnews_ext":
        if dist_sign == "id":
            return ["World", "Sports", "Business", "Sci/Tech"]
        return ["World", "Sports", "Business", "Sci/Tech"]
    elif data_sign == "reuters_mk_nl":
        # default is Reuters-7K-3L
        if dist_sign == "id":
            return ["Acq", "Corn", "Earn", "Grain", "Interest", "Money-fx", "Ship"]
        return ["Crude", "Trade", "Wheat"]
    elif data_sign == "20news_6s":
        if dist_sign == "id":
            return ["comp", "rec", "sci", "religion", "politics", "misc"]
        return ["comp", "rec", "sci", "religion", "politics", "misc"]
    elif data_sign == "yahoo_agnews_five":
        if dist_sign == "id":
            return ["Health", "Science & Mathematics", "Sports", "Entertainment & Music", "Business & Finance"]
        return ["Health", "Sci/Tech", "Sports", "Entertainment", "Business"]
    elif data_sign == "agnews_fl":
        if dist_sign == "id":
            return ["World", "Sports", "Business", "Sci/Tech"]
        return ["U.S.", "Europe", "Italia", "Software and Developement"]
    elif data_sign == "agnews_fm":
        if dist_sign == "id":
            return ["World", "Sports", "Business", "Sci/Tech"]
        return ["Entertainment", "Health", "Top Stories", "Music Feeds"]
    elif data_sign == "yahoo_answers_fm":
        if dist_sign == "id":
            return ["Health", "Science & Mathematics", "Sports", "Entertainment & Music", "Business & Finance"]
        return ["Society & Culture", "Education & Reference", "Computers & Internet", "Family & Relationships", "Politics & Government"]
    elif data_sign == "clinc":
        if dist_sign == "id":
            #return ['exchange_rate', 'car_rental', 'vaccines', 'international_visa', 'translate', 'carry_on', 'book_flight', 'timezone', 'flight_status', 'lost_luggage', 'book_hotel', 'plug_type', 'travel_alert', 'travel_notification', 'travel_suggestion']
            return ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
        #return ['exchange_rate', 'car_rental', 'vaccines', 'international_visa', 'translate', 'carry_on', 'book_flight', 'timezone', 'flight_status', 'lost_luggage', 'book_hotel', 'plug_type', 'travel_alert', 'travel_notification', 'travel_suggestion']
        return ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]

    return [0, 1]
