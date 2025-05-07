from django.contrib import admin
from .models import Link


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            self.readonly_fields = ('key', 'name')
        else:
            self.readonly_fields = ('created', 'updated')
        return self.readonly_fields


admin.site.register(Link, LinkAdmin)
