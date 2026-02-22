map = {
#     "A":["B","C"],
#     "B":["B","C"],
#     "C":["B","C"],
#     "D":["B","C"],
#     "E":["B","C"],
#     "F":["B","C"],
# }

# def count_junction(map,start):
#     count =0
#     for junction in map[start]:
#         count = count + count_junction(map,junction)   #recursive call when the call itself the change the start 
#     return count
# print(count_junction(map,"A"))