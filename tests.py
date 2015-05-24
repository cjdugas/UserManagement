from django.test import TestCase
from django.db import models
from django.core.urlresolvers import reverse
from .models import Log, User
import uuid


    #FIELD INPUT TESTS

    #test format and uniqueness responses of email field
    #test uniqueness and minlength responses of Name Field


    #USERS TESTS

    #Users index page with no users: verify 200 Response Code, queryset == []
    #User detail page with non-existent user: verify 404 Response Code, Response contains 'Detail: Not found'
    #User creation:
        #Verify user detail page contains accurate user information
        #Verify created log creation
        #Verify User.objects.all() contains new User
    #User update posted:
        #Verify updated name / email
        #Verify that updated_at >= created_at
        #Verify update log creation
    #User deleted:
        #Verify user detail page 404 Response Code
        #Verify User not found in database
        #Verify deleted log creation

    #LOG TESTS

    #Log index page with no entries: verify 200 Response Code, queryset == []
    #Log detail page with non-existent user: verify 404 Response Code, Response contains 'Detail: Not found'
