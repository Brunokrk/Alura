from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_display_links = ('id', 'nome')
    search_field = ('nome',)
    list_per_page = 10
# Register your models here.
admin.site.register(Pessoa, ListandoPessoas)