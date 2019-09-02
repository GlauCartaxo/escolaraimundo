from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import forms as auth_forms


from users.models import Usuario, Aluno, Professor


class UsuarioCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UsuarioChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'password', 'is_aluno', 'is_professor', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UsuarioAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin  
    # that reference specific fields on auth.User.
    list_display = ('nome', 'email', )
    list_filter = ('is_admin', 'is_professor', 'is_aluno')
    fieldsets = (
        (None, {'fields': ('nome', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_professor', 'is_aluno')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



class AlunoCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'rg', 'cpf', 'matricula']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        aluno = super().save(commit=False)
        aluno.set_password(self.cleaned_data["password1"])
        aluno.is_aluno = True
        if commit:
            aluno.save()
        return aluno

class AlunoChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'rg', 'cpf']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AlunoAdmin(admin.ModelAdmin):
    
    change_form = AlunoChangeForm
    add_form = AlunoCreationForm
 
    list_display = ('nome', 'email', 'rg', 'cpf')
    #fieldsets = (
    #     ('Informações', {'fields': ('nome', 'email', 'password', 'rg', 'cpf')}),
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'email', 'rg', 'cpf', 'password1', 'password2')}
        ),
    )

    search_fields = ('nome', 'email', 'rg', 'cpf')
    ordering = ('email',)
    filter_horizontal = ()

    readonly_fields = ('last_login', )


    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(AlunoAdmin, self).get_form(request, obj, **kwargs)
    


# /////////////////////////////////////////////////////////////////////////////


class ProfessorUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Professor
        fields = ['nome', 'email', 'IDProfessor']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        professor = super().save(commit=False)
        professor.set_password(self.cleaned_data["password1"])
        professor.is_professor = True
        if commit:
            professor.save()
        return professor

class ProfessorUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Professor
        fields = ['nome', 'email', 'IDProfessor']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class ProfessorAdmin(admin.ModelAdmin):

    change_form = ProfessorUserChangeForm
    add_form = ProfessorUserCreationForm
 
    list_display = ('nome', 'email', 'IDProfessor')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'email', 'IDProfessor', 'password1', 'password2')}
        ),
    )

    search_fields = ('nome', 'email', 'IDProfessor')
    ordering = ('email',)
    filter_horizontal = ()

    readonly_fields = ('last_login', )


    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(ProfessorAdmin, self).get_form(request, obj, **kwargs)