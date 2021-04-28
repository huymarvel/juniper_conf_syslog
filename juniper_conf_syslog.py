import napalm
import pprint
from napalm import get_network_driver
#IP_lo0 = "123.29.12.96"
while True:
	IP_lo0 = input("Please enter your IP lo0: ")
	if IP_lo0 != "exit" and IP_lo0 != "quit":
		print(IP_lo0)
		device={
			"hostname": IP_lo0,
			"username":"tdhuy",
			"password":"muahoado1C",
			"optional_args": {"port":22}
			}
		driver = napalm.get_network_driver("junos")
		try:
			print("Connecting to {}...".format(device["hostname"]))
			conn = driver(**device)
			conn.open()
		except:
			print("Check IP, username, password, port")
		else:
			print()
			print("Connected successful")
			print()
			print("Loading configuration...")
			conn.load_merge_candidate(filename="syslog_MX.cfg")
			print("Done")

			print()
			print("Comparing configuration...")
			diff = conn.compare_config()
			print(diff)

			conn.commit_config()
			print("Done")

			print()
			print("************* Verification *************")
			output = conn.cli(["show configuration system syslog file messages"])
			print(output["show configuration system syslog file messages"])

			conn.close()
	else:
		break
