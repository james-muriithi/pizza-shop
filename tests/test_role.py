import unittest
from app.models import Role


class TestROle(unittest.TestCase):
    def setUp(self):
        self.role = Role(name="Test Category")

    def test_instance(self):
        self.assertTrue(isinstance(self.role, Role))