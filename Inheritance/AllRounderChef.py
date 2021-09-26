from Chef import Chef

class AllRounderChef(Chef):
    def make_friedrice(self):
        print("The Chef is making Fried rice.")
    def make_specialdish(self): # We are overwriting this function because we need a different dish
        print("The Chef is making Paneer Chilli Dry")
    def make_Naan(self):
        print("The Chef is making Naan.")
