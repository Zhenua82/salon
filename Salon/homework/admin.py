from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Human, Profession, Review


class ReviewAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Review
        fields = '__all__'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'text')
    search_fields = ('title', 'created_at')
    fields = ('title', 'text')
    form = ReviewAdminForm


class NewsAdminForm(forms.ModelForm):
    biography = forms.CharField(label='Специализация', widget=CKEditorUploadingWidget())
    Last_name = forms.CharField(label='Портфолио', widget=CKEditorUploadingWidget())
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

class ProfAdminForm(forms.ModelForm):
    price = forms.CharField(label='Цена', widget=CKEditorUploadingWidget())
    class Meta:
        model = Profession
        fields = '__all__'
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title', 'price')
    search_fields = ['title']
    form = ProfAdminForm


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Review, ReviewAdmin)


