from rest_framework import serializers

from egyNationalId.models import NationalID


class NationalIDSerializer(serializers.ModelSerializer):
    # The ID number that is entered from the user
    number = serializers.CharField(max_length=14)
    # The validity of the ID number which is extracted due to checking the ID number
    validity = serializers.SerializerMethodField()
    # The data extracted from the ID number due to its validation
    birth_year = serializers.ReadOnlyField()
    birth_month = serializers.ReadOnlyField()
    birth_day = serializers.ReadOnlyField()

    class Meta:
        model = NationalID
        fields = ('number', 'validity', 'birth_year', 'birth_month', 'birth_day')

    def get_validity(self, obj):
        """
        Returning the validity of the ID number
        """
        if obj.validity == True:
            return 'Valid ID number'
        else:
            return 'Invalid ID number'

    def validate(self, data):
        """
        Check the validity of the ID number and extracting the data provided from it. 
        """
        number = data.get('number')

        # The ID number must be 14 digits
        if len(number) < 14:
            raise serializers.ValidationError('Invalid input.')
        # The ID number must start with 2 or 3
        # If it starts with 2 the year will 1900 + The second 2 numbers
        # and month and day will the next 2 numbers to them, respectively
        elif number[0] == '2':
            data['validity'] = True
            data['birth_year'] = 1900 + int(number[1:3])
            data['birth_month'] = int(number[3:5])
            data['birth_day'] = int(number[5:7])
        # If it starts with 3 the year will 2000 + The second 2 numbers
        # and month and day will the next 2 numbers to them, respectively
        elif number[0] == '3':
            data['validity'] = True
            data['birth_year'] = 2000 + int(number[1:3])
            data['birth_month'] = int(number[3:5])
            data['birth_day'] = int(number[5:7])
        
        return data
