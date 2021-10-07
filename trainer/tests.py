from django.test import TestCase
import datetime
from django.urls import reverse
from trainer.models import Trainer



class TrainerModelTestCase(TestCase):
    def setUp(self):
        self.trainer=Trainer(first_name="Peter",
                            last_name="John",
                            age=20,
                            gender="male",
                            nationality="Kenyan",
                            phone_number="07981298198",
                            id="092189h",
                            email="peter@gmail.com")


    def test_full_name_contains_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
    
    def test_full_name_contains_last_name(self):
        self.assertIn(self.trainer.last_name,self.trainer.full_name())

    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.trainer.age
        self.assertEqual(year,self.trainer.year_of_birth())

    def test_trainer_registration_view(self):
        url=reverse("register_trainers")
        data={ 
              "first_name":self.trainer,
              "last_name":self.trainer,
              "age":self.trainer,
              "gender":self.trainer,
              "nationality":self.trainer,
              "phone_number":self.trainer,
              "id":self.trainer,
              "email":self.trainer
              }

        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)

# Create your tests here.
