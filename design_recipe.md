## 1 problem - user story
```
As a member of a group chat,
I want the chat's participants shown as a single readable line,
so that I can see at a glance who's in the conversation.

Acceptance criteria:

No participants: the line is empty.
[] => ""

One participant: just their name.
["Bart"] => "Bart"

Two participants: joined with an ampersand.
["Bart", "Lisa"] => "Bart & Lisa"

Three or more participants: commas between names, with an ampersand before the last one.
["Bart", "Lisa", "Maggie"] => "Bart, Lisa & Maggie"

Order is kept: names appear in the same order they were given.
```
## 2 function signature
```python
# Parameters:
# - names - a list of names from a list of strings that are names
# Return type:
# - string of names 
#   1= name
    2 - name & name
    3 or more name, name & name
# Side Effects:
# - none
def get_names():
    pass
```

## 3 exampples
```python
# scenario 1
1 name would be - get_names("Bart") => "Bart"

# scenario 2
2 names
get_names(["Bart", "Lisa"]) => "Bart & Lisa" 
# scenario 3
 more than 2
 get_names(["Bart", "Lisa", "Maggie"]) => "Bart, Lisa & Maggie"

#scenario 4
empty
get_names([]) => ""