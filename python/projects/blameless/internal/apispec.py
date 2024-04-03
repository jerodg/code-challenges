"""
API Specification
"""
from blameless.internal.dist import UniformDist


class ApiSpec:
    """
    ApiSpec models specification  and simulates the operation of an API.  An
    API is uniquely identified by verb (e.g. POST) and resource (e.g. /api/foo).
    The API name is also unique across all APIs and is used to correlate the API
    spec, an access log line and a change log entry.

    :param seed: A seed used for initializing the random number generator
    :param name: A unique name for the API.  Uniqueness is not enforced, so it is
            up to the caller to enforce uniqueness
    :param email: The email address of the team that owns the API
    :param verb: The HTTP verb associated with this API (e.g. POST)
    :param resource: The resource that the verb acts on (e.g. /api/foobar)
    :param rate: The inbound request rate, in req/s, for this API (10 req/s)
    :param slo: The target SLO for this API (e.g. 0.999)
    :param window: The size of the SLO window in seconds
    """

    def __init__(self, seed, name, email, verb, resource, rate, slo, window):
        self.name = name
        self.email = email
        self.verb = verb
        self.resource = resource
        self.rate = rate
        self.error_dist = UniformDist(seed, 0, 1.0)
        self.error_prob = 0.0
        self.bugged = False
        self.slo = slo
        self.window = window
        secs_per_request = 1.0 / self.rate
        tolerance = secs_per_request * 0.1  # This distribution introduces jitter in the times
        self.time_dist = UniformDist(seed, secs_per_request - tolerance, secs_per_request + tolerance)

    def generate(self, curr_time):
        """
        Generate a search_stax access log line based on the current state of this API object
        """
        status = 200
        new_time = self._get_next_time(curr_time)
        if self.error_dist.random() < self.error_prob:
            status = 500

        return new_time, "{:.4f} {} {} {}".format(new_time, self.verb, self.resource, status)

    def introduce_bug(self, error_prob):
        """
        Simulates the introduction of a bug in this API, which generates an error at a given probability
        :param error_prob: probability of the simulated bug generating an error
        :return: None
        """
        self.bugged = True
        self.error_prob = error_prob

    def fix_bug(self):
        """
        Simulates a bug being fixed
        :return:
        """
        self.bugged = False
        self.error_prob = 0.0

    def has_bug(self):
        """
        :return: True if there is currently an ongoing bug in this API; otherwise False
        """
        return self.bugged

    def to_dict(self):
        """
        :return: dictionary representation of the API specification
        """
        return {'name'  : self.name, 'email': self.email, 'verb': self.verb, 'resource': self.resource, 'slo': self.slo,
                'window': self.window}

    def _get_next_time(self, curr_time):
        """
        Internal function used to draw the time of the next event in this API
        :param curr_time: The current time of the simulation
        :return: The time of the next event
        """
        return curr_time + self.time_dist.random()
