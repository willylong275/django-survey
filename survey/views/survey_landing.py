# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from survey.forms import ResponseForm
from survey.models import Category, Survey, Assignments, Queues


class SurveyLanding(View):
    def get(self, request, *args, **kwargs):

        template_name = "survey/queue_survey_landing.html"
        survey = Survey.objects.get(**kwargs)
        queue = Queues.objects.get(survey_id=kwargs['id'])
        my_assignments = Assignments.objects.filter(queue_id=queue.id, user_id=request.user.id, completed=False)
        assignment_urls = {}
        for assignment in my_assignments:
            assignment_urls[assignment.id] = assignment.queue_id.survey.get_absolute_url()
        context = {'survey': survey,
                   'my_assignments': my_assignments,
                   'assignment_urls': assignment_urls}

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):

        template_name = "survey/queue_survey_landing.html"
        context = {}
        return render(request, template_name, context)