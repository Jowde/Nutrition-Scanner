from food import Food

class DimensionalAnalysis:
    def __init__(self, inWeight: int, foodItem: Food) -> None:
        self.food = foodItem
        self.input_weight = inWeight
        self.serving_size = self.food.serving_size
        self.new_calories = self.convert(self.input_weight, self.serving_size, self.food.calories)
        self.new_carbs = self.convert(self.input_weight, self.serving_size, self.food.carbs)
        self.new_fat = self.convert(self.input_weight, self.serving_size, self.food.fat)
        self.new_satfat =self.convert(self.input_weight, self.serving_size, self.food.saturated_fat)
        self.new_unsatfat = self.convert(self.input_weight, self.serving_size, self.food.unsaturated_fat)
        self.new_fiber = self.convert(self.input_weight, self.serving_size, self.food.fiber)
        self.new_sugars = self.convert(self.input_weight, self.serving_size, self.food.sugars)
        self.new_added_sugar = self.convert(self.input_weight, self.serving_size, self.food.added_sugars)
        self.new_protein = self.convert(self.input_weight, self.serving_size, self.food.protein)

        self.newFood = Food(self.food.food_name, self.input_weight, self.new_calories, self.new_fat, self.new_satfat, self.new_unsatfat, self.new_carbs, self.new_fiber, self.new_sugars, self.new_added_sugar, self.new_protein)
    
    def convert(self, inWeight, baseServing, macro):
        newMacro = macro * (float(inWeight)//float(baseServing))
        print(newMacro)
        return newMacro