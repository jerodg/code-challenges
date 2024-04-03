#!/usr/bin/env python3.8
"""API Monitor

Copyright © 2020 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# It is assumed that you have implemented the functions below:
#
# event_stream is of type EventStream (see internal.events.EventStream)
#
# You create an object that is instantiated and assigned to service_monitor.  This
# class must implement mttr(), api_histogram() and incident_details() as described
# in README.md
from dataclasses import dataclass, field
from datetime import datetime, datetime as dt
from pprint import pformat
from typing import List, NoReturn, Optional, Union

from blameless.internal.events import EventStream


def totimestamp(dt, epoch=datetime(1970, 1, 1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10 ** 6) / 10 ** 9


@dataclass()
class LogEntry:
    type: str
    value: str

    @property
    def dict(self):
        d = self.__dict__
        del d['value']
        return d


@dataclass()
class Access(LogEntry):
    dts: float = None  # Date/Time Stamp
    verb: str = None  # HTTP Verb
    ep: str = None  # End Point
    rc: str = None  # Return Code

    def __post_init__(self):
        assert self.type == 'access'
        self.dts, self.verb, self.ep, self.rc = self.value.split()
        self.dts = float(self.dts)


@dataclass()
class Change(LogEntry):
    commit: str = None
    author: str = None
    dts: float = None
    service: str = None

    def __post_init__(self):
        assert self.type == 'change'
        commit, author, dts, service = self.value.strip().split('\n')
        self.commit = commit.split(':')[1].strip()
        self.service = service.split(':')[1].strip()
        self.dts = round(
            (dt.strptime(dts.split('Date:')[1].strip(), '%Y-%m-%d %H:%M:%S.%f') - dt.utcfromtimestamp(0)).total_seconds(), 4)
        self.service = service.split(':')[1].strip()


@dataclass()
class Window:
    changes: int = 0
    successes: int = 0
    failures: int = 0
    unknowns: int = 0
    events: List[Union[LogEntry, Change, Access, dict]] = field(default_factory=list)

    def __post_init__(self):
        for event in self.events:
            # print('window_event:', event)
            if event.type == 'change':
                self.changes += 1
            elif event.rc == '200':
                self.successes += 1
            elif event.rc == '500':
                self.failures += 1
            else:
                self.unknowns += 1

        # print('chg', self.changes, 'suc', self.successes, 'fail', self.failures)

    @property
    def sli(self):
        try:
            return self.successes / (self.failures + self.successes)
        except ZeroDivisionError:
            return 1.0  # print('error', self.__dict__)


@dataclass()
class EndPoint:
    """EndPoint"""
    name: str
    email: str
    verb: str
    resource: str
    slo: float
    window: int
    events: List[Union[LogEntry, Change, Access, dict]] = field(default_factory=list)
    windows: List[Window] = field(default_factory=list)

    def __repr__(self):
        return pformat(self.__dict__, indent=2, sort_dicts=False, compact=True)

    def process_events(self):
        pass

    def process_windows(self):
        while self.events:
            win_events = []
            start_dts = self.events[0].dts
            end_dts = start_dts + 30

            while 1 and self.events:
                event = self.events.pop()
                if start_dts <= event.dts <= end_dts:
                    win_events.append(event)
                else:
                    break

            # print('win_events:', win_events)
            if win_events:
                self.windows.append(Window(events=win_events))

            # try:  #     while :  #         event = self.events.pop()  #         # print('event:', event)  #  # except
            # IndexError:  #     self.windows.append(Window(events=win_events))

            # print(*win_events, sep='\n')  # self.windows.append(Window(events=win_events))

        # print(*self.windows, sep='\n')


class ServiceMonitor(EventStream):
    """Phantom API Client"""

    specs: dict
    resources: dict

    def __init__(self, name, start_time, max_events, seed, change_rate, prob_of_bug, prob_of_error):
        super().__init__(name, start_time, max_events, seed, change_rate, prob_of_bug, prob_of_error)
        # self.__process_api_spec()

        self.specs = {x.name: EndPoint(**x.to_dict()) for x in self.api_specs}
        self.resources = {v.resource: v.name for k, v in self.specs.items()}

    def __enter__(self):
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> NoReturn:
        pass

    def __process_api_spec(self):
        self.specs = {x.name: EndPoint(**x) for x in self.api_specs}

    def mttr(self):
        pass

    def api_histogram(self):
        pass

    def incident_details(self, endpoint: Optional[str] = None):
        pass

    def __process_stream_info(self):
        pass

    def process_events(self):
        for _ in range(0, self.max_events + 1):
            entry = self.generate_event()
            # print('entry:', entry)

            if entry['type'] == 'access':
                event = Access(**entry)
                key = self.resources[event.ep]
            elif entry['type'] == 'change':
                event = Change(**entry)
                key = event.service
            else:
                continue

            self.specs[key].events.append(event)


if __name__ == '__main__':
    print(__doc__)
