def camelcase(s):
    # Write your code here
    count=1
    for letter in s:
        if letter == letter.upper():
            count+=1
    return count

