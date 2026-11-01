p = input().strip()
is_valid = True

length = 0
for char in p:
    length += 1

if length != 10:
    is_valid = False
else:
    if p[0] != 'R' or p[1] != 'J':
        is_valid = False
        
    if not ('0' <= p[2] <= '9') or not ('0' <= p[3] <= '9'):
        is_valid = False
        
    if not ('A' <= p[4] <= 'Z') or not ('A' <= p[5] <= 'Z'):
        is_valid = False
        
    if not ('0' <= p[6] <= '9') or not ('0' <= p[7] <= '9') or \
       not ('0' <= p[8] <= '9') or not ('0' <= p[9] <= '9'):
        is_valid = False

print(is_valid)