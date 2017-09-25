
# Created by: James Lee
# Created on: Sept 2017
# Created for: ICS3U
# This program is the Address program, but with a button

import ui

def show_address_touch_up_inside(sender):
    #print ('Hello, World!')
    view['name_label'].text = ("James Lee")
    view['city_label'].text = ("Ottawa")
    view['country_label'].text = ("Canada")
    
view = ui.load_view()
view.present('sheet')
