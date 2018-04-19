

#定义一个学生类

class Student():
   #一个孔磊，pass代表直接跳过
    pass

#定义一个对象
mingyue = Student()

#再定义一个类，用来描述py的学生
class PyStudent():
    name = None
    age = 18
    course = "Python"


    def doHomework(self):
        print("I 在做作业")

        return None

yueyue = PyStudent()
yueyue.name
yueyue.age
#注意成员函数调用没有传递进入参数
yueyue.doHomework()
