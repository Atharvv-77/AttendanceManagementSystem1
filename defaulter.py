
def check_defaulter(attendance_percentage):
    if attendance_percentage < 75:
        return "Defaulter"
    else:
        return "Regular"


percentage = float(input("Enter attendance percentage: "))
print(check_defaulter(percentage))