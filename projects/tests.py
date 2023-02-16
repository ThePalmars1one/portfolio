from django.forms import ValidationError
from django.test import TestCase

from django.test import TestCase
from .models import Programate_projects

class Programate_projectsTestCase(TestCase):
    def setUp(self):
        self.project = Programate_projects.objects.create(
            title="Proyecto 1",
            description="Descripcion del proyecto 1",
            image="path/to/image1.jpg",
            link="https://www.example.com/project1"
        )

    def test_project_creation(self):
        project = Programate_projects.objects.get(title="Proyecto 1")
        self.assertEqual(project.description, "Descripcion del proyecto 1")
        self.assertEqual(project.image, "path/to/image1.jpg")
        self.assertEqual(project.link, "https://www.example.com/project1")

    def test_project_link(self):
        project = Programate_projects.objects.get(title="Proyecto 1")
        self.assertTrue(project.link.startswith("http"))


