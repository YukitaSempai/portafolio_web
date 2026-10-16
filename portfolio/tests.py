from django.test import TestCase
from django.urls import reverse


class PortfolioPagesTests(TestCase):
    def test_homepage_renders_portfolio_and_contact_actions(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jesús Carreño")
        self.assertContains(response, "wa.me/584243822294")
        self.assertContains(response, "/static/sintesis_curricular.pdf")

    def test_health_check_returns_plain_text_ok(self):
        response = self.client.get(reverse("health"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")
        self.assertEqual(response["Content-Type"], "text/plain")
