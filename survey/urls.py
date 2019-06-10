# -*- coding: utf-8 -*-

from django.conf.urls import url, re_path

from survey.views import ConfirmView, IndexView, SurveyCompleted, SurveyDetail, QueueAssignment, SurveyLanding
from survey.views.survey_result import serve_result_csv

urlpatterns = [
    url(r"^$", IndexView.as_view(), name="survey-list"),
    url(r"^(?P<id>\d+)/(?P<assignment_id>\d+)", SurveyDetail.as_view(), name="survey-detail"),
    url(r"^(?P<id>\d+)/", SurveyDetail.as_view(), name="survey-detail"),
    # url(r"^(?P<id>\d+)/(?P<assignment_id>\d+)", SurveyDetail.as_view(), name="survey-detail"),

    url(r"^landing/(?P<id>\d+)", SurveyLanding.as_view(), name="survey-landing"),
    url(r"^csv/(?P<primary_key>\d+)/", serve_result_csv, name="survey-result"),
    url(r"^(?P<id>\d+)/completed/", SurveyCompleted.as_view(), name="survey-completed"),
    url(
        r"^(?P<id>\d+)-(?P<step>\d+)/",
        SurveyDetail.as_view(),
        name="survey-detail-step",
    ),
    url(r"^confirm/(?P<uuid>\w+)/", ConfirmView.as_view(), name="survey-confirmation"),
    re_path(r".*test.*/", QueueAssignment.as_view(), name="queue-assignment"),

]
