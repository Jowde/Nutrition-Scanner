class ScaleMeasure():
    def __init__(self, weight: float, food: Food) -> None:
        self.pWeight = weight
        self.pSugars = self.portionInfo(food.sugars)
        self.pCalories = self.portionInfo(food.calories)
        self.pProtein = self.portionInfo(food.protien)
        self.pCarbs = self.portionInfo(food.carbs)              #The "p" in front of the variable names
        self.pFiber = self.portionInfo(food.fiber)                  #stands for "portioned Sugars" etc.
        self.pAddedSugars = self.portionInfo(food.addedSugars)
        self.pSatFats = self.portionInfo(food.saturatedFats)
        self.pUnSatFat = self.portionInfo(food.unsaturatedFats)
        #self.pServingSize = self.portionInfo(food.serving) Commented out: Will be implemeted later.

    def portionInfo(self, nutritionValue):
        '''
        This is where the portion contents will be calculated
        The method will take in a food value and convert it from its
        serving size to its portion size
        returns portioned nutritionValue
        '''
        return 
    
    def __str__(self) -> str:
        '''
        Returns a list containing all portioned nutritional values
        '''
        return f"Weight:{self.pWeight}\nSugars:{self.pSugars}\nCalories:{self.pWeight}\Protein:{self.pProtein}\n"