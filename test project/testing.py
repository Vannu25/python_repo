import json
import logging
from datetime import datetime

import pytest
from pytz.tzinfo import DstTzInfo

container_data = [{'LSN': 4611686018430410792, 'MID': 6613139932061915, 'CONTAINER_TYPE': 'containerd',
                   'NAME': 'lwdatacollector',
                   'CONTAINER_ID': '2b13491673885e2223e6ad9e9e37f949eee43e4daa4a4d637d78d0d2c70d9c36',
                   'IMAGE_ID': 'sha256:4ff4abed7fe120b98a579febd19acbf8afd4681d763e2f7e2dae02a10d75f462',
                   'PRIVILEGED': 1, 'NETWORK_MODE': 'None', 'PID_MODE': 'Hosts', 'IPV4': '', 'IPV6': '',
                   'LISTEN_PORT_MAP': '{}', 'PID_HASH': 114926280824756489,
                   'REPO': 'docker.io/lacework/datacollector-windows',
                   'TAG': '1.4.0.3081',
                   'PROPS_LABEL': '{\n  "annotation.io.kubernetes.container.hash": "4e339e46",'
                                  '\n  "annotation.io.kubernetes.container.restartCount": "0",'
                                  '\n  "annotation.io.kubernetes.container.terminationMessagePath": '
                                  '"/dev/termination-log",'
                                  '\n  "annotation.io.kubernetes.container.terminationMessagePolicy": "File",'
                                  '\n  "annotation.io.kubernetes.pod.terminationGracePeriod": "40",'
                                  '\n  "io.kubernetes.container.name": "lwdatacollector",'
                                  '\n  "io.kubernetes.pod.name": "lacework-agent-windows-9wngg",'
                                  '\n  "io.kubernetes.pod.namespace": "default",\n  "io.kubernetes.pod.uid": '
                                  '"23fc08df-7343-49a7-98a7-e990a190bf50"\n}',
                   'PROPS_ENV': None, 'PROPS': None, 'KEYS': None, 'OS': 'Windows'}]


# props_label_dict = json.loads(container_data[0]['PROPS_LABEL'])
#
# for key, value in props_label_dict.items():
#     print(f"{key}: {value}")

# for data in container_data:
#     props_label = data['PROPS_LABEL']
#     props_label_dict = json.loads(props_label)
#     if props_label_dict.get('io.kubernetes.pod.name') is None:
#         print("io.kubernetes.pod.name should not be null")
#     if props_label_dict.get('annotation.io.kubernetes.container.restartCount') != "0":
#         print("restart count is zero")
#     else:
#         pytest.fail('the restart count is not 0')
#
# for data in container_data:
#     if data["NAME"] != 'lwdatacollector':
#         if data["PID_MODE"] != 'Hosts':
#             print("error : The pid mode is not set as host")


for data in container_data:
    assert data['OS'] is not None or data['OS'] == "Windows", "os is empty"





