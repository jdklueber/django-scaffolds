from django.test import SimpleTestCase
from project.viewtests import TestSuiteMixin

from .views import HomeView, AboutView


class HomePageViewTests(SimpleTestCase, TestSuiteMixin):
    def setUp(self):
        self.path = "/"
        self.name = "home"
        self.view = HomeView
        self.template = "home.html"
        self.text = "Home"
        self.setups()

class AboutPageViewTests(SimpleTestCase, TestSuiteMixin):
    def setUp(self):
        self.path = "/about"
        self.name = "about"
        self.view = AboutView
        self.template = "about.html"
        self.text = "About"
        self.setups()
