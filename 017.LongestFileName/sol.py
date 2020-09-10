import os

class FileEntry:
    def __init__(self, indent, name):
        self.indent = indent
        self.name = name

def convert_line(line):
    tabs = 0
    while line.startswith("\t"):
        tabs += 1
        line = line[1:]
    return FileEntry(tabs, line)

def total_length(path):
    total = 0
    for part in path:
        total += len(part)
    return total + len(path) - 1


input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
result = 0
lines = input.splitlines()
current_path = []

for line in lines:
    print("current_path: %s" % current_path)
    entry = convert_line(line)
    if len(current_path) == 0:
        current_path.append(entry.name)
    else:
        if entry.indent == len(current_path)-1:
            current_path.pop()
            current_path.append(entry.name)
        elif entry.indent == len(current_path):
            current_path.append(entry.name)
        elif entry.indent < len(current_path)-1:
            current_path = current_path[0:entry.indent]
            current_path.append(entry.name)
        else:
            raise("invalid indent: %d after %d" % (entry.indent, len(current_path)))

    if total_length(current_path) > result:
        result = total_length(current_path)

print("result: %d" % result)

