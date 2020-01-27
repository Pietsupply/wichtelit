from django import http

from wichtelit.forms import GruppenForm, MemberForm
from wichtelit.models import Wichtelgruppe
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class MyTemplateView(TemplateView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active'] = self.name
        return context


class HomeView(MyTemplateView):
    name = 'home'
    template_name = 'home.html'


class ImprintView(MyTemplateView):
    name = 'impressum'
    template_name = 'impressum.html'


class GruppenView(FormView):
    template_name = 'form_GruppenForm.html'
    form_class = GruppenForm

    def form_valid(self, form):
        self.temp_object = form.save()
        return super().form_valid(form)
        # return http.HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return str(self.temp_object.id)


class MemberView(FormView):
    template_name = 'form_MemberForm.html'
    form_class = MemberForm

    def form_valid(self, form):
        try:
            # Hier hole ich mir die Wichtelgruppe aus der Datenbank.
            wichtelgruppe_id = self.kwargs.pop('wichtelgruppe_id')
            wichtelgruppe = Wichtelgruppe.objects.get(id=wichtelgruppe_id)
            # Hier erstelle ich aus der Eingabemaske das potentielle Objekt.
            self.object = form.save(commit=False)
            # Nun die wichtelgruppe von oben hinzufügen
            self.object.wichtelgruppe = wichtelgruppe
            wichtelgruppe.budget = wichtelgruppe.budget or 0 + form.cleaned_data['budget']
            self.object.save()
            wichtelgruppe.save()
            return http.HttpResponse(
                f"Viel Spaß beim wichteln. + {self.object.wichtelgruppe.wichteldatum} wird gewichtelt."
            )
        except Wichtelgruppe.DoesNotExist:
            return http.HttpResponseNotFound(
                "Die Wichtelgruppe scheint es nicht mehr zu geben."
            )