from django.http import Http404
from django.shortcuts import render
from django.views import View

import tours.data as tod
import random

contents = {'title': 'Stepik Travel',
            'departures': tod.departures}


class MainView(View):

    def get(self, request):

        count = 6
        first_six = {}

        while len(first_six) < count:
            k, v = random.choice(list(tod.tours.items()))
            if k not in first_six:
                first_six[k] = v

        text = {
            'subtitle': tod.subtitle,
            'description': tod.description,
            'tours_part': first_six}

        return render(request, 'index.html', dict(contents, **text))


class DepartureView(View):

    def get(self, request, departure):
        new_dict_depart = {}
        if departure in tod.departures:
            new_dict_depart = {'departure_from': tod.departures[departure],
                               'tours_filtered': {k: v for k, v in tod.tours.items() if
                                                  v['departure'] == departure}}

        else:
            raise Http404

        return render(request, 'departure.html', dict(contents, **new_dict_depart))


class TourView(View):

    def get(self, request, id):

        if id in tod.tours:

            tour = tod.tours[id]
            text = {
                'tour': tour,
                'departure_from': tod.departures[tour['departure']]
            }
        else:
            raise Http404
        return render(request, 'tour.html', dict(contents, **text))
