from django.contrib import admin
from .models import Pricing,Post,Contact,Category,About
# Register your models here.

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Pricing)