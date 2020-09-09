
class Student():

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def greeting(self):
        return "I'm" + self.name + "and I'm in grade" + self.grade
    
s = Student('Shelby', 6)


assert s.name == "Shelby", 'Test Failed'
print('PASSED')

assert s.grade == 6, 'Test Failed'
print('PASSED')


assert s.greeting() == "I'm Shelby and I'm in grade 6", 'Test Failed'
print('PASSED')

def separate_into_words(string):
    final_list = []
    final_list = string.split(' ')
    return final_list
print(separate_into_words("look the dog ran fast"))