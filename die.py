from random import randrange

def compute_randnum():
    num = randrange(1,7)
    return num

test_condition = 2
comp_values = []
while test_condition == 2:
    tmp_var = compute_randnum()

    if tmp_var != 1:
        comp_values.append(tmp_var)

    if tmp_var == 1:
        test_condition = 3
        sum_comp_values = sum(comp_values)

        str_comp_values = str(comp_values)

        print("YAY you win dice gam3!! \n Here's what you rolled: ", str_comp_values + "\n This is your total score: ",
              sum_comp_values)
