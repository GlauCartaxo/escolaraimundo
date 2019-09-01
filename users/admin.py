from django.contrib import admin
from users.models import Usuario, Aluno, Professor
from users.forms import UsuarioAdmin, AlunoAdmin, ProfessorAdmin
from django.contrib.auth.models import Group
# Now register the new UserAdmin...
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)