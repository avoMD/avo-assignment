from django.db import migrations


def seed(apps, schema_editor):
    Seed = apps.get_model("api", "Seed")
    Seed.objects.create(key="status", value="ok")


class Migration(migrations.Migration):
    dependencies = [("api", "0001_initial")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
