# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import redirect
from survey.models import Survey, Assignments, Queues
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login





class IndexView(TemplateView):
    template_name = "survey/list.html"
    login_template = "accounts/login.html"

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)
        # if not self.request.user.is_authenticated:
        #     return redirect(viewArticles, year = "2045", month = "02"
        surveys = Survey.objects.filter(is_published=True, queue_survey=False)
        queue_surveys = Survey.objects.filter(is_published=True, queue_survey=True)

        if not self.request.user.is_authenticated:
            surveys = surveys.filter(need_logged_user=False)

        my_assignments = Assignments.objects.filter(user_id=self.request.user.id, completed=False)

        context["my_assigments"] = my_assignments
        context["surveys"] = surveys
        context["queue_surveys"] = queue_surveys

        my_survey_names = {}
        for assignnment in my_assignments:
            assignment_queue = Queues.objects.get(id=assignnment.queue_id_id)
            assignment_survey = Survey.objects.get(id=assignment_queue.survey_id)
            #my_survey_names[assignment_survey.name] = assignnment.queue_id.survey.get_landing_url()
            my_survey_names[assignment_survey.name] = assignnment.queue_id.survey.id
        context["my_survey_names"] = my_survey_names

        all_assignments = Assignments.objects.filter(completed=False).exclude(user_id=self.request.user.id )
        #all_filtered = Assignments.objects.exclude(user_id=self.request.user.id in all_assignments)
        #context["all_assignments"] = all_filtered
        context["all_assignments"]=all_assignments

        # survey_links = {}
        # for survey in Survey.objects.filter(is_published=True, queue_survey=True):
        #     for assingnment in my_assignments:
        #         # if assingnment.queue_id_id == survey.id:
        #         survey_links[assingnment.id] = assingnment.queue_id.survey.get_absolute_url()


        context["my_completed_assigments"] = Assignments.objects.filter(user_id=self.request.user.id, completed=True)
        return context

