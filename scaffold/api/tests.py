from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class HealthCheckTest(TestCase):
    def test_health(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)


class MigrationTest(TestCase):
    def test_no_missing_migrations(self):
        call_command("makemigrations", "--check", "--dry-run", stdout=StringIO())
