# class Simplegradebook:
#     def __init__(self):
#         self._grades = {}
    
#     def add_student(self,name):
#         self._grades[name] =[]
    
#     def report_grade(self,name,score):
#         self._grades[name].append(score)
    
#     def average_grade(self,name):
#         grades =self._grades[name]
#         return sum(grades)/len(grades)
   


# book = Simplegradebook()
# book.add_student('Alice')
# book.report_grade('Alice',90)
# book.report_grade('Alice',95)
# book.report_grade('Alice',100)
# print(book.average_grade('Alice'))

from collections import defaultdict

# class BySubjectGradebook:
#     def __init__(self):
#         self._grades = {}
    
#     def add_student(self,name):
#         self._grades[name] = defaultdict(list)
    
#     def report_grade(self,name,subject,score):
#         self._grades[name][subject].append(score)
        

#     def report_grade1(self,name,subject,grade):
#         by_subject = self._grades[name]
#         grade_list = by_subject[subject]
#         grade_list.append(grade)
    
#     def average_grade(self,name):        
#         by_subject  =  self._grades[name]
#         total,count = 0,0
#         for _,scores in by_subject.items():
#             for score in scores:
#                 total += score
#                 count += 1
#         return total/count
    
#     def average_grade1(self,name):
#         by_subject = self._grades[name]
#         total,count = 0,0
#         for grades in by_subject.values():
#             total += sum(grades)
#             count += len(grades)
#         return total/count
    
# book = BySubjectGradebook()
# book.add_student('Bob')
# book.report_grade('Bob','math',90)
# book.report_grade('Bob','math',85)
# book.report_grade('Bob','gym',90)
# book.report_grade('Bob','gym',100)
# book.average_grade('Bob')
# print(book.average_grade1('Bob'))

class WeightGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self,name):
        self._grades[name] = defaultdict(list)

    def report_grade(self,name,subject,score,weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score,weight))
    
    def average_grade(self,name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject,scores in by_subject.items():
            subject_avg,total_weight = 0,0
            for score,weight in scores:
                subject_avg += score*weight
                total_weight += weight
            score_sum += subject_avg/total_weight
            score_count += 1
        return score_sum/score_count
    
book = WeightGradebook()
book.add_student('Alice')
book.report_grade('Alice','Math',95,0.05)
book.report_grade('Alice','Math',60,0.15)
book.report_grade('Alice','Gym',90,0.10)
book.report_grade('Alice','Gym',30,0.05)
print(book.average_grade('Alice'))




grades = []
grades.append((95,0.05))
grades.append((80,0.15))
total = sum( score*weight for score,weight in grades)
total_weihght =sum(weight for _,weight in grades)
average_grade = total/total_weihght

grades = []
grades.append((95,0.05,'w'))
grades.append((80,0.15,'e'))
total = sum( score*weight for score,weight,_ in grades)
total_weihght =sum(weight for _,weight,_ in grades)
average_grade = total/total_weihght

from collections import namedtuple
Grade = namedtuple('Grade',('score','weight'))

class Subject:
    def __init__(self):
        self._grades = []
    def report_grade(self,score,weight):
        self._grades.append(Grade(score,weight))    
    
    def average_grade(self):
        total,total_weight = 0,0
        for grade in self._grades:
            total += grade.score*grade.weight
            total_weight += grade.weight
        return total/total_weight
    
class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)
    
    def get_subject(self,name):
        return self._subjects[name]
    
    def average_grade(self):
        total,count = 0,0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)
        
    def get_students(self,name):
        return self._students[name]
    
book = Gradebook()
alert =book.get_students('alert')
math = alert.get_subject('math')
math.report_grade(90,0.10)
math.report_grade(95,0.85)
math.report_grade(75,0.05)
gym = alert.get_subject('gym')
gym.report_grade(100,0.10)
gym.report_grade(85,0.85)
gym.report_grade(90,0.05)

print(alert.average_grade())
        
        