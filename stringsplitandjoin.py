def split_and_join(line):
    # write your code here
    splitstr=line.split()
    joinstr="-".join(splitstr)
    return joinstr
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)