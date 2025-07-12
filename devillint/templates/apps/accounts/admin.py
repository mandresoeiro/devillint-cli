# admin.py - exemplo de conteúdo
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Campos que serão exibidos na lista de usuários no admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')

    # Campos que podem ser pesquisados
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Campos somente leitura
    readonly_fields = ('date_joined', 'last_login')

    # Agrupamentos na visualização de edição
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('role',)}),
    )
