class student:

    def __init__(self, firstName, lastName, districtCode, enrollCredit):
        self.firstName = firstName
        self.lastName = lastName
        self.districtCode = districtCode
        self.enrollCredit = enrollCredit
    
    def tuitionOwed(self):
        if self.districtCode == 'I':
            ratePerCredit = 250
        else:
            ratePerCredit = 500

        self.tuition = self.enrollCredit * ratePerCredit
        return self.tuition
       
student1 = student('Frank', 'Alvino', 'I', 3)
student2 = student('Jim', 'Tomes', 'O', 3)


print(f"Student: {student1.firstName} {student1.lastName}")
print(f"District Code: {student1.districtCode}")
print(f"Enrolled Credits: {student1.enrollCredit}")

print(student2.firstName)
print(student2.tuitionOwed()) 

