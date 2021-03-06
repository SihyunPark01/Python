


class Person:
    def __init__(self, name):
        self.name = name

    def work(self):
        print('%s working...' % self.name)

class Student(Person):
    def work(self):
        print('%s studying...' % self.name)

class Developer(Person):
    def work(self):
        print('%s programming...' % self.name)

if __name__ == '__main__':

    obj1 = Person('김유신')
    obj2 = Student('김춘추')
    obj3 = Developer('장보고')

    people = [obj1, obj2, obj3]

    for person in people:
        person.work()

