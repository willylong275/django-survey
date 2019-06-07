from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from survey.views import IndexView

from survey.models import Assignments, Survey


class QueueAssignment(TemplateView):

    template_name = "survey/list.html"

    def get_context_data(self, **kwargs):
        assignment_id = self.request.GET.get('assignment_id')
        record = Assignments.objects.get(id=assignment_id)
        record.user_id = self.request.user.id
        record.save()

        context = super(QueueAssignment, self).get_context_data(**kwargs)
        surveys = Survey.objects.filter(is_published=True, queue_survey=False)

        queue_surveys = Survey.objects.filter(is_published=True, queue_survey=True)

        if not self.request.user.is_authenticated:
            surveys = surveys.filter(need_logged_user=False)

        context["surveys"] = surveys

        my_assignments = Assignments.objects.filter(user_id=self.request.user.id, completed=False)

        context["my_assigments"] = my_assignments

        all_assignments = Assignments.objects.filter(completed=False).exclude(user_id=self.request.user.id)
        # all_filtered = Assignments.objects.exclude(user_id=self.request.user.id in all_assignments)
        # context["all_assignments"] = all_filtered
        context["all_assignments"] = all_assignments

        survey_links = {}
        for survey in Survey.objects.filter(is_published=True, queue_survey=True):
            for assingnment in my_assignments:
                # if assingnment.queue_id_id == survey.id:
                survey_links[assingnment.id] = assingnment.queue_id.survey.get_absolute_url()

        context["my_completed_assigments"] = Assignments.objects.filter(user_id=self.request.user.id, completed=True)




        return context
