from django.test import TestCase

# Create your tests here.
from .models import *

# test image class


class ImageTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
            first_name='mzee',
            last_name='mzima'
        )
        Image.objects.create(
            image_name='test_image',
            image_caption='test image',
            profile_id=user.id,
            user_id=user.id
        )

    def test_image_name(self):
        image = Image.objects.get(image_name='test_image')
        self.assertEqual(image.image_name, 'test_image')