#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.19

"""
import csv
import sys
import traceback

if __name__ == '__main__':
    try:
        with open('./screen_share_interview_data.csv') as cs:
            rdr = csv.reader(cs)
            rows = [r for r in rdr]
            # sites = [r[2] for r in rdr]
            # counts = Counter(sites)
            # top_sites = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
            # print(*top_sites, sep='\n')
            # sites = set([r[2] for r in rows])
            # # print(sites)
            # total = {k: [0, 0] for k in sites}
            # # print(total)
            # for r in rows:
            #     # print(r)
            #     try:
            #         total[r[2]][0] += int(r[3])
            #         total[r[2]][1] += int(r[4])
            #     except ValueError:
            #         pass
            #
            # total = sorted(total.items(), key=operator.itemgetter(1), reverse=True)
            # [print(r[0], r[1]) for r in total]
            # for row in rows:
            #     row.append(row[-1] + row[-2])
            #
            # sorted_rows = sorted(rows, key=operator.itemgetter(5), reverse=True)
            # groups = itertools.groupby(sorted_rows, key=operator.itemgetter(5))
            #
            # [print(a) for a in groups]
            # # print(*groups, sep='\n')
            # for k, v in groups:

            # timestamps = set([r[1] for r in rows])
            # total = {k: 0 for k in timestamps}
            # for r in rows:
            #     # print(r)
            #     try:
            #         total[r[1]] += int(r[3])
            #         total[r[1]] += int(r[4])
            #     except ValueError:
            #         pass
            #
            # total = sorted(total.items(), key=operator.itemgetter(1), reverse=True)
            # [print(r[0], r[1]) for r in total]

            twt = [r for r in rows if r[2] == 'twitter.com']
            tot_in = 0
            for r in twt:
                try:
                    tot_in += int(r[3])
                except ValueError:
                    pass

            avg_total_bytes = tot_in / (300 * len(twt))
            print(avg_total_bytes * 8)

    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
