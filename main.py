import Omicron_Engine as OE

if __name__ == "__main__":
    display = OE.MainDisplay(
                                current_screen='start_screen', 
                                display_title='Program 4', 
                                quick_boot = True
                             )
    display.main_loop()