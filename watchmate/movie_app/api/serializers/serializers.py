from rest_framework import serializers
from ...models import Movie


def description_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Description is too short!")


class MovieSerializer(serializers.Serializer):
    #  it is incremented by database, read only = true meaning not updatable (client can read it but not write it)
    # read_only is a Core Argument
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    #  3rd Type validation - validators
    description = serializers.CharField(validators=[description_length])
    active = serializers.BooleanField()

    # 1st Type of validation - field validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value

    #  2nd Type validation - object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description should be different!")
        else:
            return data

    def create(self, validated_data):
        # Create and return a new `Snippet` instance, given the validated data.

        return Movie.objects.create(**validated_data)

    def update(self, database_instance, updated_object):
        # Update and return an existing `Snippet` instance, given the validated data.
        database_instance.name = updated_object.get('name', database_instance.name)
        database_instance.description = updated_object.get('description', database_instance.description)
        database_instance.active = updated_object.get('active', database_instance.active)
        database_instance.save()
        return database_instance
