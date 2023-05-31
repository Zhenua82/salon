from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Human, Profession

class NewsAdminForm(forms.ModelForm):
    biography = forms.CharField(label='Биография', widget=CKEditorUploadingWidget())
    Last_name = forms.CharField(label='Фамилия', widget=CKEditorUploadingWidget())
    class Meta:
        model = Human
        fields = '__all__'


class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Last_name', 'age', 'profession', 'get_photo', 'is_published')
    list_display_links = ('id', 'Name', 'Last_name')
    search_fields = ('Name', 'Last_name')
    list_editable = ['is_published', 'profession']
    fields = ('Name', 'Last_name', 'age', 'biography', 'profession', 'photo', 'get_photo', 'is_published')
    readonly_fields = ['get_photo']
    form = NewsAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото нет'

    get_photo_description = 'Миниатюра'
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)

