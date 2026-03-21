# 22. Join the IP address string with . operator I/P: 192 11 1 0 O/P : 192.11.1.0

ip_address = input("Enter the IP address (separated by space):")
ip_address_parts = ip_address.split()
joined_ip_address = ".".join(ip_address_parts)
print("Joined IP Address:",joined_ip_address)


# otherr way using for loop

ip_address2 = input("Enter the IP address(separated by space):")
ip_address_parts2 = ip_address2.split()

joined_ip_address2 = ""

for part in ip_address_parts2:
    joined_ip_address2 = joined_ip_address2 + "." + part

print("Joined IP Address (method 2):", joined_ip_address2)  # [1:] to remove the leading dot
    
    