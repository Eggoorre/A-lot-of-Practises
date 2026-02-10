def equasion_sol() -> None:
    '''
    function solving hod+hod+hod=mat and printing all solutions
    :return: None
    '''
    solutions = []

    for h in range(1, 10):
        for o in range(10):
            for d in range(10):
                hod = int(str(h) + str(o) + str(d))
                mat = hod * 3

                if mat > 999:
                    continue

                m = int(str(mat)[0])
                a = int(str(mat)[1])
                t = int(str(mat)[2])

                if m == 0:
                    continue

                digits = {h, o, d, m, a, t}
                if len(digits) != 6:
                    continue

                solutions.append((hod, mat))

    for hod, mat in solutions:
        print(f'{hod}+{hod}+{hod}={mat}')


def main() -> None:
    '''
    main function
    :return:
    '''
    equasion_sol()


if __name__ == "__main__":
    main()
