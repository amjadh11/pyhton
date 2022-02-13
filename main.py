
def read_write_files(f1, f2, f3):
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    for i in range(len(lines1)):
        line = lines1[i]
        username = ''
        data = line.split(':')
        if len(data) == 5:
            username = data[1][0] + data[2][0] + data[3]
        if len(data) == 4:
            username = data[1][0] + data[2]

        username = username.lower()
        data.insert(1, username)
        line = ':' . join(data)
        lines1[i] = line

    for i in range(len(lines2)):
        line2 = lines2[i]
        username2 = ''
        data2 = line2.split(':')
        if len(data2) == 5:
            username2 = data2[1][0] + data2[2][0] + data2[3]
        if len(data2) == 4:
            username2 = data2[1][0] + data2[2]

        username2 = username2.lower()
        data2.insert(1, username2)
        line2 = ':'.join(data2)
        lines2[i] = line2

    f3.writelines(lines1)
    f3.write('\n')
    f3.writelines(lines2)
    f3.close()


if __name__ == '__main__':

    file1 = open('input_1.txt', 'r')
    file2 = open('input_2.txt', 'r')
    file3 = open('output.txt', 'w')
    read_write_files(file1, file2, file3)




