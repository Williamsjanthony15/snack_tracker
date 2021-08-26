from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

# class snacksTest(SimpleTestCase):
#     def test_home_page(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#     def test_home_page_template(self):
#         url = reverse('home')
#         response = self.client('home')
#         self.assertTemplateUsed(response, 'home.html')
#         self.assertTemplateUsed(response, 'base.html')
    
#     def test_about_page(self):
#         url = reverse('about')
#         response = self.client.get(url)
#         self.assertEqua(response.status_code, 200)