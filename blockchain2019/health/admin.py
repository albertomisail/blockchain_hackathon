from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Person)
admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(CreditCard)
