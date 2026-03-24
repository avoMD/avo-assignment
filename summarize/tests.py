from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient


class SummarizeViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch("summarize.service.client.chat.completions.create")
    def test_summarize(self, mock_openai):
        mock_openai.return_value.choices[0].message.content = "• Chief complaint\n• Key finding\n• Plan"

        res = self.client.post("/api/summaries/", {"patient_info": "Patient is a 45-year-old with chest pain."}, format="json")

        self.assertEqual(res.status_code, 200)
        self.assertIn("result", res.data)

    def test_missing_patient_info(self):
        res = self.client.post("/api/summaries/", {}, format="json")
        self.assertEqual(res.status_code, 400)
