from food import Food
class InfoHandler:
    '''
    Handles saving from and retireving from csv file
    
    loadfromfile creates the self.food_dict variable with all the data from the csv file
    
    savetofile saves any changes to food_dict and places it in the csv file
    '''
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.food_dict = {}
        self.loadfromfile()
    
    def savetofile(self): # Saves dict to file
        foods = open(self.file_path, 'w')
        for food in self.food_dict:
            current_food = self.food_dict[food]
            print(current_food['calories'])
            foods.write(f"{food},{current_food['serving_size']},{current_food['calories']},{current_food['fat']},{current_food['saturated_fat']},{current_food['unsaturated_fat']},{current_food['carbs']},{current_food['fiber']},{current_food['sugars']},{current_food['added_sugar']},{current_food['protein']}")
        foods.close()
    
    def loadfromfile(self): # converts file to dict
        foods = open(self.file_path)
        foodslist = foods.readlines()
        for line in foodslist:
            
            line.replace('','\n')
            foodinfo = line.split(',') # should probably add serving size in grams lol
            self.food_dict[foodinfo[0]] = { 'serving_size':foodinfo[1],
                                            'calories':foodinfo[2], 
                                            'fat': foodinfo[3],
                                            'saturated_fat':foodinfo[4],
                                            'unsaturated_fat':foodinfo[5],
                                            'carbs':foodinfo[6], 
                                            'fiber': foodinfo[7],
                                            'sugars':foodinfo[8], 
                                            'added_sugars': foodinfo[9], 
                                            'protein': foodinfo[10]
                                            }
        foods.close()

    def add_item(self, food: Food):
        self.food_dict[food.food_name] = food.convert_to_dict()
            
    def remove_item(self, foodName):
        del self.food_dict[foodName.food_name]
    
            
    
    def food_from_dict(self, name:str):
            return Food(food_name= name, 
                        serving_size=self.food_dict[name]['serving_size'], 
                        calories=self.food_dict[name]['calories'], 
                        fat=self.food_dict[name]['fat'], 
                        saturated_fat=self.food_dict[name]['saturated_fat'], 
                        unsaturated_fat=self.food_dict[name]['unsaturated_fat'],
                        carbs=self.food_dict[name]['carbs'],
                        fiber=self.food_dict[name]['fiber'],
                        sugars=self.food_dict[name]['sugars'],
                        added_sugars=self.food_dict[name]['added_sugars'],
                        protein=self.food_dict[name]['protein'])


if __name__ =='__main__':       
    foodinfo = InfoHandler('foods.csv')
    apple = Food(food_name='apple', calories=100, protein = 10, fat = 10, carbs =102)
    burger = Food(food_name='burger', calories=120, protein=26, carbs= 20)
    
    foodinfo.add_item(burger)
    for item in foodinfo.food_dict:
        print(foodinfo.food_dict[item])
    foodinfo.remove_item(burger)
    for item in foodinfo.food_dict:
        print(foodinfo.food_dict[item])
    foodinfo.food_dict[apple.food_name] = apple.return_dict()
    
    foodinfo.savetofile()