from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class FeedTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_reverse_login(self):
        self.assertEquals(reverse("login"), "/login")

    def test_anon_access(self):
        response = self.client.get(reverse("feed"))
        self.assertEquals(response.status_code, 302)

    def test_auth_access(self):
        u = User.objects.create_user(
            username="user",
            password="user"
        )

        login_status = self.client.login(
            username="user",
            password="user"
        )

        self.assertEquals(login_status, True)
        response = self.client.get(reverse("feed"))
        self.assertEquals(response.status_code, 200)
        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code, 302)
