

def str_to_bytes(ip : str):
	fragments = ip.split('.')
	bytes_ip = [int(byte_str) for byte_str in fragments]
	return bytes_ip

def int_to_mask(mask_int : int):
	mask = 0
	if mask_int >= 0 and mask_int <= 32:
		for i in range(mask_int):
			mask |= 1 << (32 - i - 1)
	return mask

def int_to_bytes(ip : int):
	bytes_ip = []
	for i in range(4):
		bytes_ip.append((ip >> (24 - 8 * i)) & 0xff)
	return bytes_ip

def bytes_to_int(bytes : list[int]):
	value = 0
	value = bytes[0] << 24
	value |= bytes[1] << 16
	value |= bytes[2] << 8
	value |= bytes[3] << 0
	return value

def bytes_to_str(ip : list[int]):
	return f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}"

def network_address(ip : list[int], mask : list[int]):
	return [ip_byte & mask_byte for ip_byte, mask_byte in zip(ip, mask)]

def broadcast_address(ip : list[int], mask : list[int]):
	network = network_address(ip, mask)
	network_value = bytes_to_int(network)
	mask_value = bytes_to_int(mask)
	broadcast_value = network_value | ~mask_value
	return int_to_bytes(broadcast_value)

def hosts(mask : int):
	return 2**(32 - mask) - 2

while True:
	ip = input("\nip: ")
	if ip in ["exit", "quit", "/"]:
		break
	mask = input("mask: /")
	try:
		bytes_ip = str_to_bytes(ip)
		bytes_mask = int_to_bytes(int_to_mask(int(mask)))
		print("IP:", ip)
		print("MASK:", bytes_to_str(bytes_mask))
		print("NETWORK:", bytes_to_str(network_address(bytes_ip, bytes_mask)))
		print("BROADCAST:", bytes_to_str(broadcast_address(bytes_ip, bytes_mask)))
		print("HOSTS:", hosts(int(mask)), "or (without router):", hosts(int(mask)) - 1)
	except:
		print("Bad ip format")

