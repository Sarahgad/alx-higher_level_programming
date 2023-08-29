class employee:
# intialize function(construction)
    def __init__ (self,name, age, department, ismanager, rating, salary):
        self.name = name
        self.age = age
        self.department= department
        self.ismanager = ismanager
        self.rating = rating
        self.salary = salary
#how to add function aka class methods
    def is_excellent(self):
        if self.rating > 4.5:
            return True
        else:
            return False
        
    def bounus(self):
        if self.age == 60:
            self.salary += 500
            print("congratulation")
        else:
            print("goodluck")




#object from class
#import class is must

employee1 = employee("sarah", 60, "engineer", False, 5, 1000)


print(employee1.name)
print(employee1.age, employee1.department, employee1.ismanager, employee1.rating)
print(employee1.is_excellent())
print(employee1.salary)
employee1.bounus()
print(employee1.salary)




