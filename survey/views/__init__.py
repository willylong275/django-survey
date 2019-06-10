# -*- coding: utf-8 -*-

from survey.views.confirm_view import ConfirmView
from survey.views.index_view import IndexView
from survey.views.survey_completed import SurveyCompleted
from survey.views.survey_detail import SurveyDetail
from survey.views.queue_assignment import QueueAssignment
from survey.views.survey_landing import SurveyLanding

__all__ = ["SurveyCompleted", "IndexView", "ConfirmView", "SurveyDetail", "QueueAssignment", "SurveyLanding"]
