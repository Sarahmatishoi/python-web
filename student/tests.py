from django.test import TestCase
from .models import Student
import datetime
from django.urls import reverse

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="loveLace",
                            last_name="AkiraChix",
                            age=20,
                            gender="female",
                            nationality="Kenyan",
                            phone_number="07981298198",
                            id="092189h",
                            parent_name="Peter",
                            class_room="AnitaB",
                            email="sarahmatishoi@gmail.com")


    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())
    
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_student_registration_view(self):
        url=reverse("register_student")
        data={"first_name":self.student,
              "last_name":self.student,
              "age":self.student,
              "gender":self.student,
              "nationality":self.student,
              "phone_number":self.student,
              "id":self.student,
              "parent_name":self.student,
              "class_room":self.student,
              "email":self.student}

        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)

# Create your tests here.
