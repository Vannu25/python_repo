node_list = []

with open('pod_details.txt') as infile:
    for line in infile:
        if line.__contains__("windows"):
            name, node = line.split()[0], line.split()[6]
            entry = {"Name": name, "NODE": node}
            node_list.append(entry)

pod_list = []

with open('node_details.txt') as infile:
    for line in infile:
        if line.__contains__("Windows Server"):
            name, ip, os = line.split()[0], line.split()[6], line.split()[7]
            entry = {"Name": name, "EXTERNAL-IP": ip, "OS-IMAGE": os}
            pod_list.append(entry)
            # print(results)

    for node in node_list:
        for pod in pod_list:
            if node['Name'] == pod['NODE']:
                pod_name = pod['Name']
            else:
                print("name is coming as : {}", pod_name)
