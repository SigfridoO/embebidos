from django.shortcuts import render
from django.views.generic.base import TemplateView

class ChatView(TemplateView):
    template_name = "chat.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
