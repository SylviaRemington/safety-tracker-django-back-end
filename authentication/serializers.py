from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation # function runs when creating superuser
from django.contrib.auth.hashers import make_password # hashes password for us
from django.core.exceptions import ValidationError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer): # never converted to json and returned in response
    password = serializers.CharField(write_only=True) # write_only=True ensures never sent back in JSON
    password_confirmation = serializers.CharField(write_only=True)

    # This validate function below does the following:
    # checks if passwords match
    # hash passwords
    # adds back to database
    def validate(self, data): # data comes from the request body
        print('DATA',data)
        # remove fields from request body and save to vars
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        # check if they match
        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'do not match'})

        # checks if password is valid, comment this out so it works
        try:
            password_validation.validate_password(password=password)
        except ValidationError as err:
            print('VALIDATION ERROR')
            raise ValidationError({ 'password': err.messages })

        # hash the password, reassigning value 
        data['password'] = make_password(password)

        print('DATA ->', data)
        return data

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'profile_image', 'password', 'password_confirmation')



