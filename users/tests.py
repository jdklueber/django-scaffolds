from django.contrib.auth import get_user_model
from django.test import TestCase
from project.viewtests import TestSuiteMixin

from .views import SignUpPageView
from .forms import CustomUserCreationForm

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='jason',
            email='jason@jason.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'jason')
        self.assertEqual(user.email, 'jason@jason.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='super',
            email='super@jason.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'super')
        self.assertEqual(user.email, 'super@jason.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)



class SignupPageViewTests(TestCase, TestSuiteMixin):
    def setUp(self):
        self.path = "/accounts/signup/"
        self.name = "signup"
        self.view = SignUpPageView
        self.template = "signup.html"
        self.text = "Sign Up"
        self.setups()

    def testSignupForm(self):
        form = self.rsp.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.rsp, "csrfmiddlewaretoken")