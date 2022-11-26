from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='city.html',
            context={
                'boroughs': boroughs.keys()
            }
        )


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={
                'borough': borough,
                'activities': boroughs[borough].keys()
            },
        )


class ActivityView(View):
    def get(self, request, borough, activity):
        return render(
            request=request,
            template_name='activities.html',
            context={
                'borough': borough,
                'activity': activity,
                'venues': boroughs[borough][activity].keys(),
            },
        )

'''

Christy - If you look at the context in each of the three previous views you will see a definite pattern emerging.
You can use this pattern to help figure out how to set the context for 'VenueView'.

'''
class VenueView(View):
    pass
