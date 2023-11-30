"""Technical interview"""

def find_peak(list_of_integers):
    if list_of_integers is None:
        return None
    i = int(len(list_of_integers) - 1 / 2)
    if i > 0 and list_of_integers[i] >= list_of_integers [i - 1] and \
   list_of_integers[i] >= list_of_integers [i + 1]:
        return list_of_integers[i]
    
    if i >0 and list_of_integers[i] >= list_of_integers [i - 1] and \
    list_of_integers[i] < list_of_integers [i + 1]:
        return find_peak(list_of_integers[:i])
    
