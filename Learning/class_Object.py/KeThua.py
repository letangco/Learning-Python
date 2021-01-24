class Person:
    def __init__(self, Ho, Ten):
        super().__init__()
        self.ho = Ho
        self.ten = Ten
    def ExportFullName(self):
        print(self.ho, self.ten)

class Children(Person):
    def __init__(self, Ho, Ten):
        super().__init__(Ho, Ten)
        Person.__init__(self, Ho, Ten)
    
x = Children('Le', 'Tang Co')
x.ExportFullName()