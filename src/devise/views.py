from django.shortcuts import render, redirect

import api

# Create your views here.
def redirect_index(request):
    return redirect("home", days_range=30, currencies="GNF")

def dashboard(request, days_range=60, currencies="CAD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Hebdomadaire", 30: "Mensuel", 90: "Trimestruel", 120: "Semestruel", 365: "Annuel"}.get(days_range, "Personnalisé")
    return render(request, "devise/index.html", context={"data": rates,
                                                         "days_labels": days,
                                                         "currencies": currencies,
                                                         "page_label": page_label})