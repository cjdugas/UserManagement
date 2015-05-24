from django.db import models
from django.core import validators
import uuid
import datetime


class User(models.Model):
    #id is the primary key, formatted as a UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    #email is automatically validated by Django's EmailValidator
    email = models.EmailField(unique=True, blank=False)

    #name must be at least 2 chars in length
    name = models.CharField(max_length=100, blank=False,
                            validators=[validators.MinLengthValidator(2)])

    #created_at and updated_at are datetimes formatted with ISO 8601
    #updated_at is initially set to the datetime it is created
    created_at = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), editable=False)

    #ordered according to json schema
    class Meta:
        # insert ordering attribute here
        ordering = ('id', 'email', 'name', 'created_at', 'updated_at')

    #unicode and string representation of User
    def __unicode__(self):
        return u'{\'id\': \'%s\', \'email\': \'%s\', \'name\': \'%s\', \'created_at\': \'%s\', \'updated_at\': \'%s\'}' \
               % (self.id, self.email, self.name, self.created_at, self.updated_at)


class Log(models.Model):
    #Set up action choices as 2-tuples of database format and human-readable format
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'
    ACTION_CHOICES = (
        (CREATE, 'Create'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete'),
    )

    #id is the primary key, formatted as a UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    #user_id of the user the action is being performed on,
    #length is restricted to the 36-char UUID
    user_id = models.CharField(max_length=36, blank=False)

    #the action logged from the set {'create', 'update', 'delete'}
    action = models.CharField(max_length=6, choices=ACTION_CHOICES, blank=False)

    #attributes is a json representation of all the user attributes
    attributes = models.TextField(blank=False)

    #created_at is a datetime formatted with ISO 8601
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.id
