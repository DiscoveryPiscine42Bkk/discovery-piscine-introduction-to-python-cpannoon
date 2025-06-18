import sys

if len(sys.argv) != 3:
    print("none")
    sys.exit(1)

keyword = sys.argv[1]
search_string = sys.argv[2]

count = search_string.count(keyword)

if count == 0:
    print("none")
else:
    print(count)