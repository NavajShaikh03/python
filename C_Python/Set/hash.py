# "name" → hash value → memory location → value found
# Python internally uses hashing and hashable objects to make operations fast.
# The hash value itself is NOT the actual memory address.
# It is used to calculate/index the place where data should be stored.

d = {
    "name" : "Mahi",
}
print(d["name"])     # directed find the value 
print(hash("name"))