from django.contrib import admin

from .models import Bd, Rubric


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')  # посл-ть имён полей, кот. выводятся в списке записей
    list_display_links = ('title', 'content')  # посл-ть имён полей, кот. должны преобр-ны в гиперссылки, ведущие на стр. правки записи
    search_fields = ('title', 'content', )  # посл-ть имён полей, по кот. должна вып-ся фильтрация


admin.site.register(Bd, BdAdmin)
admin.site.register(Rubric)
