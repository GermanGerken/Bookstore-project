from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):


    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Will',
            email='Will@mail.com',
            password='testpass1234'
        )
        self.assertEqual(user.username, 'Will')
        self.assertEqual(user.email, 'Will@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@mail.com',
            password='testpass1234'
        )

        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)