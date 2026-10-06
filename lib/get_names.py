def get_names(names):
    if len(names) == 1:
        return names[0]
    elif names == []:
        return ""
    else:
        return ", ".join(names[0:-1]) + " & " + names[-1] 