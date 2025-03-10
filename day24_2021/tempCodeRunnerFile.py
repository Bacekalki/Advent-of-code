for i in range(45_999_999_999_999, 45_000_000_000_000, -1):
    if ans == i:
        print("Here is the answer")
        break
    str_num = str(i)
    if (str_num == str(new_ans)):
        print(dp)
        break
    if '0' not in str_num:
        dp = check_num(str_num, commands, inp_indexes, dp)