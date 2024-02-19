from pydantic import BaseModel, validator

class StudentDTO(BaseModel):
    first_name: str
    last_name: str
    age: int
    course: int
    mean_grade: int

    @validator('first_name')
    def validate_first_name(cls, first_name):
        if first_name[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            raise ValueError("First name should start from capital letter")

        return first_name

    @validator('last_name')
    def validate_last_name(cls, last_name):
        if last_name[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            raise ValueError("Last name should start from capital letter")

        return last_name

    @validator('age')
    def validate_age(age):
        if age < 18 or age > 30:
            raise ValueError("Age should be between 18 and 30.")

        return age

    @validator('course')
    def validate_course(cls, course):
        if course < 1 or course > 6:
            raise ValueError("Course should be between 1 and 6.")

        return course

    @validator('mean_grade')
    def validate_grade(cls, mean_grade):
        if mean_grade < 1 or mean_grade > 100:
            raise ValueError("Grade should be between 1 and 100.")

        return mean_grade

student_dto = StudentDTO(**{'first_name': 'John', 'last_name':'Doe', 'age': 30, 'course': 3, 'mean_grade': 88})
print(student_dto)