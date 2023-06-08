import time

card_data = [{'IMAGE_REPO': '602401143452.dkr.ecr.us-west-2.amazonaws.com/amazon-k8s-cni', 'TAG': 'v1.10.4-eksbuild.1',
'CONTAINER_TYPE': 'DOCKER', 'IMAGE_CREATED_TIME': 1655102644061,
'SIZE': '304491232', 'CONTAINER_COUNT': '2', 'MACHINE_COUNT': '2', 'USER_COUNT': '1',
'OS': 'Linux', 'VULN_SUMMARY': None, 'IMAGE_SCAN_STATUS': None, 'VULN_START_TIME': None,
'SCAN_CREATED_TIME': None, 'VULN_EVAL_GUID': None,
'IMAGE_ID': 'sha256:327f18c78eff7ae9c812d87698d813deb5a232055ffebdff5575bdf9f8fb9573'}]

current_time = int(time.time() * 1000)  # Convert current timestamp to milliseconds

if card_data[0]['IMAGE_CREATED_TIME'] > current_time:
    print("ERROR: IMAGE_CREATED_TIME is greater than the current time.")
else:
    print("IMAGE_CREATED_TIME is valid.")
