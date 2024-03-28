"""
Events
"""
import sys
import uuid
from datetime import datetime
from random import Random
from blameless.internal.dist import UniformChoiceDist, UniformDist
from blameless.internal.apispec import ApiSpec


class AccessLog(object):
    def __init__(self, api_specs, start_time):
        """
        This object represents a simulated access log for one or more APIs.  The simulation
        is driven by repeated calls to `generate()`.  Each call will return a single access log
        line from a single API, where that API is the next to generate an event in the simulation.

        :param api_specs: A list of APISpec objects that are used to simulate the access log
        :param start_time: The start time of the simulation (e.g. time.now())
        """
        self.api_specs = api_specs
        self.curr_idx = 0
        self.curr_time = start_time
        self.next_draws = [api_spec.generate(self.curr_time) for api_spec in api_specs]
        self.min_idx = -1
        self._update_min_idx()

    def get_curr_time(self):
        """
        Accessor for current time
        :return: The current time in the simulation
        """
        return self.curr_time

    def generate(self):
        """
        Generate a log line from one of the APIs
        :return: The next access log line ion the simulation
        """
        self.curr_time, log_line = self._get_next_line()
        return log_line

    def _get_next_line(self):
        """
        Internal helper to determine the next event in the simulation by polling all of the
        involved APIs
        :return:  A current time, access log line tuple
        """
        curr_time, log_line = self.next_draws[self.min_idx]
        self.next_draws[self.min_idx] = self.api_specs[self.min_idx].generate(curr_time)
        self._update_min_idx()
        return curr_time, log_line

    def _update_min_idx(self):
        """
        Internal function to update the index of the APISpec that has the next event
        :return: None
        """
        min_draw = sys.maxsize
        for i in range(len(self.next_draws)):
            if self.next_draws[i][0] < min_draw:
                self.min_idx = i
                min_draw = self.next_draws[i][0]


class ChangeEntry(object):
    """
            This object represents a single change to an API

            :param name: The name of the API affected by the change
            :param email: The email address of the entity that applied the change
            :param ts: Timestamp of when the change was applied
    """

    def __init__(self, name, email, ts):
        self.name = name
        self.email = email
        self.ts = ts
        self.commit = uuid.uuid4().hex

    def to_dict(self):
        """
        A dictionary representation of the change entry
        :return: A dictionary representatin of the change entry
        """
        return {'name': self.name, 'email': self.email, 'ts': self.ts, 'commit': self.commit}

    def to_log_entry(self):
        """
        The git-like representation of the change entry
        :return: The git-like representation of the change entry
        """
        str = 'commit: ' + self.commit + '\n'
        str += 'Author: <' + self.email + '>\n'
        str += 'Date: {}\n'.format(datetime.fromtimestamp(self.ts))
        str += 'Service: ' + self.name + '\n'
        return str

    def __str__(self):
        """
        A single-line representation of the change entry
        :return: A single-line representation of the change entry
        """
        return "'name': {}, 'email': {}, 'ts': {}, 'commit': {}".format(self.name, self.email, self.ts, self.commit)


class ChangeLog(object):
    """
            This object holds the state for a simulated change log.  The simulation is driven by repeated
            calls to `generate()`

            :param seed: A seed used for initializing the random number generator
            :param api_specs: A list of APISpec objects that are used to simulate the access log
            :param change_rate: The average rate of changes to all APIs
            :param prob_of_bug: The probability of a bug being introduced, given a change has occurred
            :param prob_of_error: The probability of a request error, given a bug has been introduced
            """

    def __init__(self, seed, api_specs, change_rate, prob_of_bug, prob_of_error):

        # of changes per request of each API
        self.time_between_changes = float(1) / change_rate
        self.last_change_ts = 0
        self.api_specs = api_specs
        # Probability of a change introducing a bug
        self.prob_of_bug = prob_of_bug
        # Probability of a bug leading to a request error
        self.prob_of_error = prob_of_error
        self.bug_dist = UniformDist(seed, 0, 1.0)
        self.api_selector = UniformChoiceDist(seed)

    def generate(self, curr_time):
        """
        Generate a change log event
        :param curr_time: The current time in the simulation
        :return: a change log event if one should happen; otherwise, return None
        """
        api_spec = self.api_selector.choice(self.api_specs)

        # Only introduce change at the prescribed rate
        if curr_time - self.last_change_ts < self.time_between_changes:
            return None

        # Assume this change fixed the previous bug
        if api_spec.has_bug():
            api_spec.fix_bug()
        # If there is no bug, see if this change introduces one
        elif self.bug_dist.random() < self.prob_of_bug:
            api_spec.introduce_bug(self.prob_of_error)

        self.last_change_ts = curr_time

        return ChangeEntry(api_spec.name, api_spec.email, curr_time).to_log_entry()


class EventStream(object):
    """
            An event stream simulation, which is composed of access log and change log events.  The event
            stream is randomly seeded with APISpec from ./api_specs, determined by a seeded random number
            generator.

            Events are randomly generated and realized by repeatedly calling `generate_event()`.  There are three
            types of events:

            - Change log event: Each event represents a change to a specific API
            - Access log event: Each event represents a request to a specific API
            - End-of-stream: This event means there are no more events to process

            :param name: The name of the event stream
            :param start_time: The start time of the simulation
            :param max_events: The maximum number of events to emit
            :param seed: A seed to use across all random number generators in the simulation.
                This ensures a deterministic stream of events for testing.
            :param change_rate: The rate of change across all APIs
            :param prob_of_bug: The probability of a bug being introduced, given a change has occurred
            :param prob_of_error: The probability of a request error, given a bug has been introduced
            """

    def __init__(self, name, start_time, max_events, seed, change_rate, prob_of_bug, prob_of_error):
        self.name = name

        # todo: use json instead of eval
        api_spec_fd = open('./api_specs')
        api_specs = api_spec_fd.readlines()
        api_spec_fd.close()
        api_specs = [eval(api_spec.strip().format(seed)) for api_spec in api_specs]

        # todo: not random
        api_specs = api_specs[:10]
        Random(seed).shuffle(api_specs[:10])

        self.api_specs = api_specs
        self.access_log = AccessLog(api_specs, start_time)
        self.change_log = ChangeLog(seed, api_specs, change_rate, prob_of_bug, prob_of_error)
        self.max_events = max_events
        self.num_events = 0

    def __enter__(self):
        return self

    def generate_event(self):
        """
        Generate an event from the event stream based on its current state
        :return: An access log, change log or end-of-stream event
        """
        # print('event:', self.num_events)
        if self.num_events >= self.max_events:
            return {'type': 'end-of-stream', 'value': 'end-of-stream'}

        curr_time = self.access_log.get_curr_time()
        self.num_events += 1

        change_log_event = self.change_log.generate(curr_time)

        if change_log_event is not None:
            return {'type': 'change', 'value': change_log_event}
        else:
            access_log_entry = self.access_log.generate()
            return {'type': 'access', 'value': access_log_entry}

    def get_api_specs(self):
        """
        Get the APISpec objects associated with this event stream
        :return: A list of APISpec objects
        """
        return self.api_specs

    def get_info(self):
        """
        Get a dictionary-formatted list of APISpecs associated with this event stream
        :return:
        """
        infos = []
        for api_spec in self.api_specs:
            infos.append(api_spec.to_dict())
        return infos
