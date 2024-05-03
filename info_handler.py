from food import Food
class InfoHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.food_dict = {}
        self.loadfromfile()
    
    def savetofile(self): # Saves dict to file
        foods = open(self.file_path, 'w')
        for food in self.food_dict:
            current_food = self.food_dict[food]
            print(current_food['calories'])
            foods.write(f"{food},{current_food['calories']},{current_food['fat']},{current_food['protein']},{current_food['carbs']},{current_food['sugars']},{current_food['fiber']},{current_food['added_sugar']},{current_food['saturated_fat']},{current_food['unsaturated_fat']},{current_food['serving_size']},{current_food['serving_size_unit']}")
        foods.close()
    
    def loadfromfile(self): # converts file to dict
        foods = open(self.file_path)
        foodslist = foods.readlines()
        for line in foodslist:
            
            line.replace('','\n')
            foodinfo = line.split(',') # should probably add serving size in grams lol
            self.food_dict[foodinfo[0]] = { 'calories':foodinfo[1], 
                                            'fat':foodinfo[2],
                                            'protein':foodinfo[3], 
                                            'carbs':foodinfo[4], 
                                            'sugars':foodinfo[4], 
                                            'fiber': foodinfo[5],
                                            'added_sugars': foodinfo[6], 
                                            'saturated_fat':foodinfo[7],
                                            'unsaturated_fat':foodinfo[8], 
                                            'serving_size':foodinfo[9],
                                            'serving_size_unit': foodinfo[10]}
        foods.close()

    def add_item(self, food: Food):
        self.food_dict[food.food_name] = food.convert_to_dict()
            
    def remove_item(self, foodName):
        del self.food_dict[foodName.food_name]
    

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
    foodinfo.savetofile()