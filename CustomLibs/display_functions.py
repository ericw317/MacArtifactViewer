def one_value(name, list_name):
    spacing = len(name)

    output = []
    output.append(name)
    output.append("-" * spacing)

    for value in list_name:
        output.append(value)
    output.append("")

    return output

def two_values(name1, name2, list_name):
    # get spacing sizes
    list1_space = len(name1)
    for value in list_name:
        if len(value[0]) > list1_space:
            list1_space = len(value[0])

    list2_space = len(name2)
    for value in list_name:
        if len(value[1]) > list2_space:
            list2_space = len(value[1])

    total_space = list1_space + list2_space + 6

    # display values
    output = []
    output.append(f"{name1:<{list1_space}} | {name2}")
    output.append("-" * total_space)
    for value in list_name:
        output.append(f"{value[0]:<{list1_space}} | {value[1]}")
        output.append("-" * total_space)
    output.append("")

    return output

def three_values(name1, name2, name3, list_name):
    # getting spacing sizes
    list1_space = len(name1)
    for value in list_name:
        if len(value[0]) > list1_space:
            list1_space = len(value[0])

    list2_space = len(name2)
    for value in list_name:
        if len(value[1]) > list2_space:
            list2_space = len(value[1])

    list3_space = len(name3)
    for value in list_name:
        if len(value[2]) > list3_space:
            list3_space = len(value[2])

    total_space = list1_space + list2_space + list3_space + 9

    # display values
    output = []
    output.append(f"{name1:<{list1_space}} | {name2:<{list2_space}} | {name3}")
    output.append("-" * total_space)
    for value in list_name:
        output.append(
            f"{value[0]:<{list1_space}} | {value[1]:<{list2_space}} | {value[2]}")
        output.append("-" * total_space)
    output.append("")

    return output

def four_values(name1, name2, name3, name4, list_name):
    # getting spacing sizes
    list1_space = len(name1)
    for value in list_name:
        if len(value[0]) > list1_space:
            list1_space = len(value[0])

    list2_space = len(name2)
    for value in list_name:
        if len(value[1]) > list2_space:
            list2_space = len(value[1])

    list3_space = len(name3)
    for value in list_name:
        if len(value[2]) > list3_space:
            list3_space = len(value[2])

    list4_space = len(name4)
    for value in list_name:
        if len(value[3]) > list4_space:
            list4_space = len(value[3])

    total_space = list1_space + list2_space + list3_space + list4_space + 12

    # display values
    output = []
    output.append(f"{name1:<{list1_space}} | {name2:<{list2_space}} | {name3:<{list3_space}} | {name4}")
    output.append("-" * total_space)
    for value in list_name:
        output.append(f"{value[0]:<{list1_space}} | {value[1]:<{list2_space}} | {value[2]:<{list3_space}} | {value[3]:<{list4_space}}")
        output.append("-" * total_space)
    output.append("")

    return output

def five_values(name1, name2, name3, name4, name5, list_name):
    # getting spacing sizes
    list1_space = len(name1)
    for value in list_name:
        if len(value[0]) > list1_space:
            list1_space = len(value[0])

    list2_space = len(name2)
    for value in list_name:
        if len(value[1]) > list2_space:
            list2_space = len(value[1])

    list3_space = len(name3)
    for value in list_name:
        if len(value[2]) > list3_space:
            list3_space = len(value[2])

    list4_space = len(name4)
    for value in list_name:
        if len(value[3]) > list4_space:
            list4_space = len(value[3])

    list5_space = len(name5)
    for value in list_name:
        if len(value[4]) > list5_space:
            list5_space = len(value[4])

    total_space = list1_space + list2_space + list3_space + list4_space + list5_space + 15

    # display values
    output = []
    output.append(f"{name1:<{list1_space}} | {name2:<{list2_space}} | {name3:<{list3_space}} | {name4:<{list4_space}} | "
                  f"{name5}")
    output.append("-" * total_space)
    for value in list_name:
        output.append(f"{value[0]:<{list1_space}} | {value[1]:<{list2_space}} | {value[2]:<{list3_space}} | {value[3]:<{list4_space}} | "
                      f"{value[4]:<{list5_space}}")
        output.append("-" * total_space)
    output.append("")

    return output

def nine_values(name1, name2, name3, name4, name5, name6, name7, name8, name9, list_name):
    # getting spacing sizes
    list1_space = len(name1)
    for value in list_name:
        if len(value[0]) > list1_space:
            list1_space = len(value[0])

    list2_space = len(name2)
    for value in list_name:
        if len(value[1]) > list2_space:
            list2_space = len(value[1])

    list3_space = len(name3)
    for value in list_name:
        if len(value[2]) > list3_space:
            list3_space = len(value[2])

    list4_space = len(name4)
    for value in list_name:
        if len(value[3]) > list4_space:
            list4_space = len(value[3])

    list5_space = len(name5)
    for value in list_name:
        if len(value[4]) > list5_space:
            list5_space = len(value[4])

    list6_space = len(name6)
    for value in list_name:
        if len(value[5]) > list6_space:
            list6_space = len(value[5])

    list7_space = len(name7)
    for value in list_name:
        if len(value[6]) > list7_space:
            list7_space = len(value[6])

    list8_space = len(name8)
    for value in list_name:
        if len(value[7]) > list8_space:
            list8_space = len(value[7])

    list9_space = len(name9)
    for value in list_name:
        if len(value[8]) > list9_space:
            list9_space = len(value[8])

    total_space = list1_space + list2_space + list3_space + list4_space + list5_space + list6_space + list7_space
    total_space += list8_space + list9_space + 27

    # display values
    output = []
    output.append(f"{name1:<{list1_space}} | {name2:<{list2_space}} | {name3:<{list3_space}} | {name4:<{list4_space}} "
                  f"| {name5:<{list5_space}} | {name6:<{list6_space}} | {name7:<{list7_space}} | {name8:<{list8_space}} "
                  f"| {name9:<{list9_space}}")
    output.append("-" * total_space)
    for value in list_name:
        output.append(f"{value[0]:<{list1_space}} | {value[1]:<{list2_space}} | {value[2]:<{list3_space}} | "
                      f"{value[3]:<{list4_space}} | {value[4]:<{list5_space}} | {value[5]:<{list6_space}} | "
                      f"{value[6]:<{list7_space}} | {value[7]:<{list8_space}} | {value[8]}")
        output.append("-" * total_space)
    output.append("")

    return output

def eleven_values(name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11, list_name):
    # getting spacing sizes
    list1_space = len(name1)
    for value in list_name:
        if len(value[0]) > list1_space:
            list1_space = len(value[0])

    list2_space = len(name2)
    for value in list_name:
        if len(value[1]) > list2_space:
            list2_space = len(value[1])

    list3_space = len(name3)
    for value in list_name:
        if len(value[2]) > list3_space:
            list3_space = len(value[2])

    list4_space = len(name4)
    for value in list_name:
        if len(value[3]) > list4_space:
            list4_space = len(value[3])

    list5_space = len(name5)
    for value in list_name:
        if len(value[4]) > list5_space:
            list5_space = len(value[4])

    list6_space = len(name6)
    for value in list_name:
        if len(value[5]) > list6_space:
            list6_space = len(value[5])

    list7_space = len(name7)
    for value in list_name:
        if len(value[6]) > list7_space:
            list7_space = len(value[6])

    list8_space = len(name8)
    for value in list_name:
        if len(value[7]) > list8_space:
            list8_space = len(value[7])

    list9_space = len(name9)
    for value in list_name:
        if len(value[8]) > list9_space:
            list9_space = len(value[8])

    list10_space = len(name10)
    for value in list_name:
        if len(value[9]) > list10_space:
            list10_space = len(value[9])

    list11_space = len(name11)
    for value in list_name:
        if len(value[10]) > list11_space:
            list11_space = len(value[10])

    total_space = list1_space + list2_space + list3_space + list4_space + list5_space + list6_space + list7_space
    total_space += list8_space + list9_space + list10_space + list11_space + 33

    # display values
    output = []
    output.append(f"{name1:<{list1_space}} | {name2:<{list2_space}} | {name3:<{list3_space}} | {name4:<{list4_space}} "
                  f"| {name5:<{list5_space}} | {name6:<{list6_space}} | {name7:<{list7_space}} | {name8:<{list8_space}}"
                  f"| {name9:<{list9_space}} | {name10:<{list10_space}} | {name11:<{list11_space}}")
    output.append("-" * total_space)
    for value in list_name:
        output.append(f"{value[0]:<{list1_space}} | {value[1]:<{list2_space}} | {value[2]:<{list3_space}} | "
                      f"{value[3]:<{list4_space}} | {value[4]:<{list5_space}} | {value[5]:<{list6_space}} | "
                      f"{value[6]:<{list7_space}} | {value[7]:<{list8_space}} | {value[8]:<{list9_space}} | "
                      f"{value[9]:<{list10_space}} | {value[10]}")
        output.append("-" * total_space)
    output.append("")

    return output
