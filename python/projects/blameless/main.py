import argparse
import time

# from blameless.internal.events import EventStream
from blameless.solution.monitor import ServiceMonitor


class ProbabilityRange(object):
    def __eq__(self, other):
        return 0.0 <= other <= 1.0

    def __str__(self):
        return '0.0 <= val <= 1.0'


parser = argparse.ArgumentParser(description='Change and acceess event stream processor')
parser.add_argument('--seed', type=int, default=1337, help='Random number generator seed value')
parser.add_argument('--max-events', type=int, default=500, help='Max number of events to generate')
parser.add_argument('--prob-bug', type=float, default=0.95, choices=[ProbabilityRange()], help='Probability change introduces bug')
parser.add_argument('--prob-error', type=float, default=0.95, choices=[ProbabilityRange()],
                    help='Probability of a request error, given a bug has been introduced')
args = parser.parse_args()

if __name__ == '__main__':
    curr_time = time.time()
    # name, start_time, seed, change_rate, prob_of_bug, prob_of_error):
    # Fixing change rate to 1 every 10 seconds tro keep things simple
    # event_stream = EventStream("foo", curr_time, args.max_events, args.seed, 0.1, args.prob_bug, args.prob_error)

    # It is assumed that you have implemented the functions below:
    #
    # event_stream is of type EventStream (see internal.events.EventStream)
    #
    # You create an object that is instantiated and assigned to service_monitor.  This
    # class must implement mttr(), api_histogram() and incident_details() as described
    # in README.mdm

    # implement all arguments as cli args
    with ServiceMonitor('foo', curr_time, args.max_events, args.seed, 0.1, args.prob_bug, args.prob_error) as sm:
        sm.process_events()

        for k, v in sm.specs.items():
            v.process_windows()
            # print(v)
            for window in v.windows:
                # print(window)
                if window.sli < v.slo:
                    print(window)

                # print(window.sli)

            # for window in v.windows:  #     print(window.events)

        # for k, v in sm.specs.items()

        # for k, v in sm.specs.items():  #     print(v)

        # for k, v in sm.resources.items():  #     print(k, v)

        # print(sm.get_api_specs())  # print(sm.get_api_specs())  # print(sm.get_info())  # print(*[x.__dict__ for x in
        # sm.get_api_specs()], sep='\n')  # print('=' * 80)  #  # print(*[x.to_dict() for x in sm.get_api_specs()], sep='\n')  #
        # print('=' * 80)  #  # #  # for _ in range(0, args.max_events + 1):  #     print(sm.generate_event())

        # sm.process_events()

        # print('=' * 80)  #  # [print(k, v) for k, v in sm.events.items()]

    # service_monitor = get_service_monitor(event_stream)  # print(service_monitor.mttr())  # print(
    # service_monitor.api_histogram())  # print(service_monitor.incident_details())
