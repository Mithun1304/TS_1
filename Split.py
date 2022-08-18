class Split:
    print("Example using replace()")
    print("-----------------------------------------------------------------------------")
    print(
        "Defination:The replace() method returns a copy of the string where the old substring is replaced with the new substring.\n"
        " The original string is unchanged. If the old substring is not found, it returns the copy of the original string.")
    print("-----------------------------------------------------------------------------")
    print("syntax of replace:  replace(String, Old_substring, New_substring);")
    print("------------------------------------------------------------------------------")
    example1 = 'bat ball'

    # replace b with c
    replace_example1 = example1.replace('b', 'c')
    print(replace_example1)