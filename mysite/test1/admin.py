from django.contrib import admin
from .models import Test1, Test2


class AuthorAdmin(admin.ModelAdmin):
    # fields = ('title', 'num',)
    list_display = ('id', 'title', 'num', 'price')


admin.site.register(Test1)
admin.site.register(Test2, AuthorAdmin)
