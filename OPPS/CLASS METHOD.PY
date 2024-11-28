class person:
    """ class variable"""
    name = "Adarsh"
    school="jsp qsp pysp"
    """ instance variable """
    def __init__(self,course,age,email,aadhar,address):
        
        self.course = course
        self.age = age
        self.email =email  
        self.aadhar= aadhar
        self.address=address
        
    '''instance method'''
    def stu_details(self):
        print(f'''
        person_name:{self.name}
        institute:{self.school}
        course:{self.course}
        age:{self.age}
        email:{self.email}
        aadhar:{self.aadhar}
        address:{self.address}
        ''')
    @classmethod
    def display_(cls):
            print(f'''
            name:{cls.name}
            school={cls.school}
            ''')
s1=person('python', 23, '@gmail.com', 53567, 'AP')
s1.stu_details()
person.stu_details(s1)
person.display_()
s1.display_()