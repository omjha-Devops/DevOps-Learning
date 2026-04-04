is_male = False
is_tall = False

if is_male and is_tall:
    print("You are male and you are tall")
elif not(is_male) and is_tall:
    print("You are not male but you are tall")
elif is_male and not(is_tall):
    print("You are male but not tall")
else:
    print("You are not male and not tall")