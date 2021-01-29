from django.contrib import admin
from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    fields = ['full_name', 'date_of_birth','year_of_experience', 'departmnet_Id','resume']

admin.site.register(Candidate,CandidateAdmin)