from django.test import TestCase
from .models import NationalID
from .serializers import NationalIDSerializer

def create_nationalId(number):
    """
    Create a nationl ID with the given 'number'.
    """
    return NationalID.objects.create(number=number)


class NationalIDModelTests(TestCase):

    def test_checking_ID_number(self):
        """
        Test the validation of correct id number
        """
        national_id = create_nationalId(29505271202117)
        serializer = NationalIDSerializer(national_id)
        data = serializer.data
        self.assertEqual(data['validity'], 'Valid ID number')
    
    def test_checking_ID_number(self):
        """
        Test the validation of wrong id number
        """
        national_id = create_nationalId(49505271202117)
        serializer = NationalIDSerializer(national_id)
        data = serializer.data
        self.assertEqual(data['validity'], 'Invalid ID number')
