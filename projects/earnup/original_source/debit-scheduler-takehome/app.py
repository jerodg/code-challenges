#!/usr/bin/env python3.8
"""EarnUp Technical Assessment: Debit Scheduler
Copyright ©2022 Jerod Gawne <https://github.com/jerodg/>
Based on code created by EarnUp <https://github.com/EarnUp/debit-scheduler-takehome>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
import json
from datetime import timedelta

import pandas as pd
from delorean import parse
from holidays import country_holidays
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response


# fixme: The instructions are inconsistent with the examples and the tests are inconsistent with the instructions.
# Due to above I wasn't entirely sure exactly what the output should look like.
# I created an issue on the github project that explains in more detail.


class App(object):

    def __init__(self):
        self.url_map = Map([Rule('/', endpoint=''),
                            Rule('/get_next_debit', endpoint='get_next_debit')])

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)

        try:
            endpoint, values = adapter.match()
            return getattr(self, f'on_{endpoint}')(request, **values)
        except NotFound:
            # Whoopsies somebody either forgot to code this or they referenced something that does not exist.
            # return self.error_404()
            return Response(status='404 Not Found')
        except HTTPException as e:
            return e

    def on_get_next_debit(self, request):
        body = request.get_json()['loan']

        # Ensure that debit_day_of_week is a weekday
        if body['debit_day_of_week'].lower() in ['saturday', 'sunday']:
            return Response(response='debit_day_of_week must be on a weekday', status=f'400 Bad Request')

        start = parse(body['debit_start_date'], yearfirst=True, dayfirst=False)
        hdays = country_holidays('US', years=start.date.year)

        # Get a list of dates (up to 5) starting from the debit_start_date forward at debit_day_of_week
        date_rng = pd.date_range(start=start.date,
                                 end=start.date + timedelta(weeks=5),
                                 freq=f'2W-{body["debit_day_of_week"][:3].upper()}')

        # Filter out dates in other months, dates that are US bank holidays (federal), and a date that equals the start date
        date_rng = [x.date() for x in date_rng if
                    x.month == start.date.month and x.date() not in hdays and not x.date() == start.date]

        response = {'debit': {
                'amount': float(f'{(body["monthly_payment_amount"] / len(date_rng)):.2f}'),
                'date':   str(date_rng[0])}}

        return Response(json.dumps(response), mimetype='application/json')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app():
    app = App()
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple

    app = create_app()
    run_simple('0.0.0.0', 5000, app, use_debugger=True, use_reloader=True)
