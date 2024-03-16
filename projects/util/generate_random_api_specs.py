import sys
import random

words_fd = open("/usr/share/dict/words", "r")
all_words = words_fd.readlines()
all_words = [word.strip() for word in all_words]

if len(sys.argv) < 2:
    print("Usage: Must specify a single integer argument!")
    sys.exit()

# req/s, SLO, SLI calculation window
req_per_s = [1, 5, 10]
slos = [0.9] + 2 * [0.99] + 4 * [0.999] + 4 * [0.9999]
windows = [30]
verbs = ["GET", "POST"]

num_api_specs = int(sys.argv[1])

for i in range(num_api_specs):
    name = random.choice(all_words)
    email_name = random.choice(all_words)
    email_domain = random.choice(all_words)
    api_resource = random.choice(all_words)
    verb = random.choice(verbs)
    req_s = random.choice(req_per_s)
    slo = random.choice(slos)
    window = random.choice(windows)
    print('ApiSpec({}, ' + '"{}", "{}@{}.com", "{}", "/api/v1/{}", {}, {:.5f}, {})'.format(name, email_name, email_domain, verb,
                                                                                           api_resource, req_s, slo, window))
