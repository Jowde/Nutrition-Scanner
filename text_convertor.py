from food import Food

MACRO_LIST = ['serving size', 'calories','total fat', 'saturated fat', 'unsaturated fat', 'total carbohydrate',  'dietary fiber','total sugars', 'added sugars', 'protein']

class TextConvertor:
    def __init__(self, food_name: str, debug: bool = False):
        self.food_name = food_name
        self.macro_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.debug = debug
    
    def text_parser(self, string: str, return_list: bool = False) -> list[int]:
        '''
        parses text created by camera and extracts macro values from it
        '''
        text = string.lower()
        text = text.replace('\n',' ')
        text = ''.join(letter for letter in text if letter.isalnum() or letter == ' ')
        macro_grams_list = []
        for macro in MACRO_LIST:
            grams = self.grams_per_macro_finder(text, macro)
            macro_grams_list.append(grams)
            if self.debug:
                print(f'{macro}: {grams}')
        if return_list:
            return macro_grams_list
        else:
            self.list_to_variables(macro_grams_list)
            
            
    def grams_per_macro_finder(self, text: str, macro: str) -> int:
        '''
        checks if an amount in grams can be extract from the photo text 
        If not returns 0 
        '''
        index = text.find(macro)
        spaced_parse = False
        grams = ''
        if index >=0:
            index = index + len(macro)
            while True:
                if text[index].isdigit():
                    grams += text[index]
                elif not spaced_parse:
                    spaced_parse = True
                else:
                    break
                index+=1
                
            if grams =='':
                grams = 0
            return int(grams) 
        return 0
    
    def list_to_variables(self, new_macro_list: list[int]):
        '''
        Takes a list and sets the variables of class to them if they are greater than 0 and less than the previous value
        the variables should in the order serving size, calories, fat, saturated fat, unsaturated fat, carbs, fiber, sugar, added sugar, protein  
        '''
        for index in range(len(self.macro_list)):
            if self.macro_list[index] == 0 or self.macro_list[index] > new_macro_list[index]:
                self.macro_list[index] = new_macro_list[index] 
    
    def create_food_item(self):
        '''
        Creates a food item using the macros gotten from the image
        '''
        return Food(self.food_name, self.macro_list[0], self.macro_list[1], self.macro_list[2], self.macro_list[3], self.macro_list[4], self.macro_list[5], self.macro_list[6], self.macro_list[7], self.macro_list[8], self.macro_list[9])