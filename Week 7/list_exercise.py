'''
def list_stats(user_list=[]):
    if isinstance(user_list, list):
        while True:
            user = input("Enter a number: ").strip()
            if len(user) == 0:
                break
            user = float(user)
            user_list.append(user)
        avg = sum(user_list) / len(user_list)

        maximum = max(user_list)
        minimum = min(user_list)
        average = sum(user_list) / len(user_list)
    
        return [maximum, minimum, average]
    else:
        print("Error: the argument must be a list object")
        return None
    
result = list_stats()
if not result == None:
    print(result)
'''

def max_length(lst, length):
    if isinstace(lst, list):
        if isinstance(length, int) and length >= 0:
            new_list = []
            for element in lst:
                if isinstance(element, str):
                    if len(element) <= length:
                        new_list.append(element)
            return new_list
        else:
            print("Error: length must be an int greater or equal to 0")
    else:
        print("error: lst must be a list")
        return None

lst1 = ["university", False, "oregon", "cat", 2.4]
filtered_list = max_length(lst1, 20)
print(filtered_list)
