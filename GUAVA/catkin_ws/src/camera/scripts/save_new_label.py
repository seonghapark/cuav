import os

# bus, car, person
label = ['5', '6', '14']


def changed_label(index, line):
    new_line = ""
    if index == '5' or index == '6':
        new_line = line.replace(index, '1')
    elif index == '14':
        new_line = line.replace(index, '2')

    return new_line


def main():
    path = "/Users/dojinkim/Desktop/YOLO/label/"
    dir_list = os.listdir(path)

    for txt in sorted(dir_list):
        data = []
        with open(path + txt) as file:
            print(txt)
            # txt 파일 내에 labelling 된 부분 나눈다
            for line in file:
                index = line[:2].rstrip()

                # label이 bus, car, person중 하나라면, 번호를 바꿔서 저장한다
                if index in label:
                    data.append(changed_label(index, line))

        # 만약 bus, car, person이 있다면...새로운 라벨로 대체
        if len(data) > 0:
            with open(path+txt, "w") as file:
                for d in data:
                    file.write(d)
        # 만약 없다면 해당 파일이름 변경
        else:
            os.rename(path+txt, path+"remove_"+txt)


if __name__ == '__main__':
    main()
