class Food:
    '''
    A class that organizes the macro-nutritional values in food.

    __init__() requires food_name as a parameter, everything else can revert to default values

    Twelve values are tracked:
    Type Int: [calories,fat,protein,carbs,sugars,fiber, 
                added_sugars,saturated_fat,unsaturated_fat,]
    Type Float: [serving_size]
    Type String: [serving_size_unit,food_name]

    all units for macros are grams unless otherwise stated
    
    exceptions:
    - calories
    - serving size

    valid units for serving size: ["teaspoon","tsp","tablespoon","tbsp","fluid ounce","fl oz","ounce","oz","cup","pint",
                  "quart","gallon","pound","gram","kilogram","liter","milliliter"]
    '''
    valid_serving_units = ["teaspoon","tsp","tablespoon","tbsp","fluid ounce","fl oz","ounce","oz","cup","pint",
                           "quart","gallon","pound","gram","kilogram","liter","milliliter"]

    def __init__(self, food_name:str, serving_size:float=0, calories:int=0, fat: int=0, saturated_fat:int=0,unsaturated_fat:int=0,carbs:int=0,fiber:int=0, sugars:int=0,
                 added_sugars:int=0, protein:int=0) -> None:
        self.food_name= str(food_name)
        
        self.serving_size= int(serving_size)
        self.calories=int(calories)
        self.carbs=int(carbs)
        self.fat=int(fat)
        self.saturated_fat=int(saturated_fat)
        self.unsaturated_fat=int(unsaturated_fat)
        self.fiber=int(fiber)
        self.sugars=int(sugars)
        self.added_sugars=int(added_sugars)
        self.protein=int(protein)
        
        
    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, value:int=0):
        if value>0:
            self._calories = value
        else:
            self._calories = 0
    
    @property
    def fat(self):
        return self._fat
    @fat.setter
    def fat(self, value:int=0):
        if value>0:
            self._fat = value
        else:
            self._fat = 0
    
    @property
    def protein(self):
        return self._protein
    @protein.setter
    def protein(self, value:int=0):
        if value>0:
            self._protein = value
        else:
            self._protein = 0
    
    @property
    def carbs(self):
        return self._carbs
    @carbs.setter
    def carbs(self, value:int=0):
        if value>0:
            self._carbs = value
        else:
            self._carbs = 0
    
    @property
    def sugars(self):
        return self._sugars
    @sugars.setter
    def sugars(self, value:int=0):
        if value>0:
            self._sugars = value
        else:
            self._sugars = 0
    
    @property
    def fiber(self):
        return self._fiber
    @fiber.setter
    def fiber(self, value:int=0):
        if value>0:
            self._fiber = value
        else:
            self._fiber = 0
    
    @property
    def added_sugars(self):
        return self._added_sugars
    @added_sugars.setter
    def added_sugars(self, value:int=0):
        if value>0:
            self._added_sugars = value
        else:
            self._added_sugars = 0
    
    @property
    def saturated_fat(self):
        return self._saturated_fat
    @saturated_fat.setter
    def saturated_fat(self, value:int=0):
        if value>0:
            self._saturated_fat = value
        else:
            self._saturated_fat = 0
    
    @property
    def unsaturated_fat(self):
        return self._unsaturated_fat
    @unsaturated_fat.setter
    def unsaturated_fat(self, value:int=0):
        if value>0:
            self._unsaturated_fat = value
        else:
            self._unsaturated_fat = 0
    
    @property
    def serving_size(self):
        return self._serving_size
    @serving_size.setter
    def serving_size(self, value:float=0):
        if value>0:
            self._serving_size = value
        else:
            self._serving_size = 0

    @property
    def food_name(self):
        return self._food_name
    @food_name.setter
    def food_name(self, value:str):
        self._food_name = value
    
    
    def return_dict(self):
        '''
        returns dictionary of items for the info handler 
        '''
        return  {'serving_size':self.serving_size,
                'calories':self.calories, 
                'fat':self.fat, 
                'saturated_fat':self.saturated_fat, 
                'unsaturated_fat':self.unsaturated_fat,
                'carbs':self.carbs, 
                'fiber':self.fiber, 
                'sugars':self.sugars,
                'added_sugars':self.added_sugars, 
                'protein':str(self.protein) + '\n'
                }
            
    def __str__(self):
        # includes major macros [calories,fat,protein,carbs,sugars,fiber]
        ret = f"food item: {self.food_name}, {self.calories} cal, {self.fat}g fat,\n"
        ret+= f"{self.protein}g protein, {self.carbs}g carbs, {self.sugars}g sugars, {self.fiber}g fiber"
        return ret
    
if __name__ == '__name__':
    apple = Food()
    print(apple)