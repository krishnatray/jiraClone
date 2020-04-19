from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from . import models
# Create your views here.


class IssueCreate(generic.edit.CreateView):
    model = models.Issue
    fields = '__all__'


class IssueDetail(generic.detail.DetailView):
    model = models.Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if context['issue'].type == "ST":
            context['className'] = "badge badge-success"
        elif context['issue'].type == "BU":
            context['className'] = "badge badge-danger"
        else:
            context['className'] = "badge badge-primary"

        return context

class IssueList(generic.list.ListView):
    # paginate_by = 2 For 2 issues per page.
    model = models.Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for issue in context['issue_list']:
            if issue.type == "ST":
                issue.className = "list-group-item-warning"
                issue.textColor = "text-success"
            elif issue.type == "BU":
                issue.className = "list-group-item-danger"
                issue.textColor = "text-danger"
            else:
                issue.className = "list-group-item-primary"
                issue.textColor = "text-primary"
        return context
