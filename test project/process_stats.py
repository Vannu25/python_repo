import datetime

datta = [{'MID': 1805, 'PID_HASH': 1285896725309595,
          'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ),
          'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 0, 59, 37, 930000, ), 'GAP_SEC': 375},
         {'MID': 1805, 'PID_HASH': 118456077994942089,
          'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ),
          'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 0, 59, 37, 930000, ), 'GAP_SEC': 375},
         {'MID': 1805, 'PID_HASH': 161073884322823003,
          'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ),
          'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 0, 59, 37, 930000, ), 'GAP_SEC': 375},
         {'MID': 1805, 'PID_HASH': 192671312674272578,
          'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ),
          'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 0, 59, 37, 930000, ), 'GAP_SEC': 375},
         {'MID': 1805, 'PID_HASH': 442694657434307420, 'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ),
          'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 0, 59, 37, 930000, ), 'GAP_SEC': 375},
         {'MID': 1805, 'PID_HASH': 664543017811446637, 'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ),
          'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 1, 9, 38, 5000, ), 'GAP_SEC': 976},
         {'MID': 1805, 'PID_HASH': 706082801958385974, 'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ),
          'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 0, 59, 37, 930000, ), 'GAP_SEC': 375},
         {'MID': 1805, 'PID_HASH': 718558081432445764, 'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ), 'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 0, 59, 37, 930000, ), 'GAP_SEC': 375}, {'MID': 1805, 'PID_HASH': 744450177882346045, 'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ), 'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 0, 59, 37, 930000, ), 'GAP_SEC': 375}, {'MID': 1805, 'PID_HASH': 1822904733764500226, 'CREATED_TIME': datetime.datetime(2023, 2, 24, 0, 53, 22, 520000, ), 'CREATED_TIME_NEXT': datetime.datetime(2023, 2, 24, 1, 0, 37, 932000, ), 'GAP_SEC': 435}]
pid_hash = set()
createdTime = set()
createdNextTime = set()


for dat in datta:
    pid_hash.add((dat['PID_HASH']))
    createdTime.add(dat['CREATED_TIME'])
    createdNextTime.add(dat['CREATED_TIME_NEXT'])
print(len(createdTime))
print(len(createdNextTime))
assert len(createdTime) == 1, "Created Time is not unique for PID_HASHs"
assert len(createdNextTime) == 1, "Created Next Time is not unique for PID_HASHs"