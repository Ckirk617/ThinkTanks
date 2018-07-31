from django.shortcuts import render
from django.http import HttpResponse
from . import models




def index(request):
    policy_areas = models.PolicyArea.objects.all()
    return HttpResponse(str(policy_areas))

