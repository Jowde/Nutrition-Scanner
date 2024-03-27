class Food:
    '''
    A class that organizes the macro-nutritional values in food.

    Eleven values are tracked:
    Type Int: [calories,fat,protein,carbs,sugars,fiber, 
                added_sugars,saturated_fat,unsaturated_fat,]
    Type Float: [serving_size]
    Type String: [serving_size_unit]

    Class variable: valid_serving_units :list
    valid units: ["teaspoon","tsp","tablespoon","tbsp","fluid ounce","fl oz","ounce","oz","cup","pint",
                  "quart","gallon","pound","gram","kilogram","liter","milliliter"]
    '''
    valid_serving_units = ["teaspoon","tsp","tablespoon","tbsp","fluid ounce","fl oz","ounce","oz","cup","pint",
                           "quart","gallon","pound","gram","kilogram","liter","milliliter"]

    def __init__(self,calories,fat,protein,carbs,sugars,fiber,
                 added_sugars,saturated_fat,unsaturated_fat,serving_size,serving_size_unit) -> None:
        self.calories=calories
        self.fat=fat
        self.protein=protein
        self.carbs=carbs
        self.sugars=sugars
        self.fiber=fiber
        self.added_sugars=added_sugars
        self.saturated_fat=saturated_fat
        self.unsaturated_fat=unsaturated_fat
        self.serving_size=serving_size
        self.serving_size_unit=serving_size_unit
    
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
    def serving_size_unit(self):
        return self._serving_size_unit
    @serving_size_unit.setter
    def serving_size_unit(self, value:str):
        if value.lower() in self.valid_serving_units:
            self._serving_size_unit = value
        else:
            self._serving_size_unit=None
    
    