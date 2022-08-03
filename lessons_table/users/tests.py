from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class RegistrationTaseCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "Sarvar",
                "first_name": "Sarvar",
                "last_name": "Rakhimov",
                "email": "test@gmail.com",
                "password": "qwqw1212"
            }
        )

        user = User.objects.get(username="Sarvar")

        self.assertEqual(user.first_name, "Sarvar")
        self.assertEqual(user.last_name, "Rakhimov")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertNotEqual(user.password, "qwqw1212")
        self.assertTrue(user.check_password("qwqw1212"))

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "Sarvar",
                "first_name": "Sarvar",
                "last_name": "Rakhimov",
                "email": "invalid-email",
                "password": "qwqw1212"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        # 1. create a user
        user = User.objects.create(
            username="Sarvar",
            first_name="Sarvar"
        )
        user.set_password("1212qwqw")
        user.save()

        # 2. TRy to create another user with that same username
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "Sarvar",
                "first_name": "Sarvar",
                "last_name": "Rakhimov",
                "email": "invalid-email",
                "password": "qwqw1212"
            }
        )
        # 3. check that the second user was not created
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        # 4. check that the form contains the error message
        self.assertFormError(response, "form", "username", "A user with that username already exists.")


class LoginTaseCase(TestCase):
    # DRY - Don't repeat yourself
    def setUp(self):
        self.db_user = User.objects.create(username="testname", first_name="testname")
        self.db_user.set_password("test123")
        self.db_user.save()

    def test_successful_login(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "testname",
                "password": "test123"
            }
        )
        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_wrong_credentials(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "wrong-testname",
                "password": "test123"
            }
        )
        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)

        # false
        self.client.post(
            reverse("users:login"),
            data={
                "username": "testname",
                "password": "somepassword"
            }
        )

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username="testname", password="test123")
        self.client.get(reverse("users:logout"))

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
