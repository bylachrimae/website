from django.contrib import admin
from .models import Category,Project,MySkill,Personal

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','category','programming_languages')
    
class MySkillAdmin(admin.ModelAdmin):
    list_display = ('title','percentage')
    
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('title','image','turkishCV','englishCV','linkedin_url','github_url','youtube_url')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(MySkill,MySkillAdmin)
admin.site.register(Personal,PersonalAdmin)

