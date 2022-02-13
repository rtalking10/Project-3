FILE_NAME = 'local_copy.log'

with open(FILE_NAME) as f:
    lines = [line.rstrip('\n') for line in f]
