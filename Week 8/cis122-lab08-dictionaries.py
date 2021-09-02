'''
CIS 122 Summer 2020 Lab 8
Author: Morgan Bartlett
Credit:
Description: Dictionary exercises
'''
def pad_string(data, size, dir = 'L', chr = ' '):
    '''
    Function that determines the amount of spacing given an object
    '''
  data = str(data)
  if len(data) > size:
    return data
  elif dir.upper() == 'L':
    return chr * (size - len(data)) + data
  else:
    return data + chr * (size - len(data))

def get_max_dict_key_size(d):
    '''
    Function returns the largest key in a dictionary
    '''
  max_key_len = 0

  # Find maximum length of all dictionary keys
  for key in d:
    if len(key) > max_key_len:
      max_key_len = len(key)

  return max_key_len

def get_max_dict_value_size(d):
    '''
    Function returns the largest key value in a dictionary
    '''
  # Note: Adapted from get_max_dict_key_size() function
  max_value_len = 0
  
  # Find maximum length of all dictionary values
  values = d.values()
  for val in values:
      if len(val) > max_value_len:
          max_value_len = len(val)

  return max_value_len

def create_dictionary(d):
    '''
    Function continously asks the user to input a key and a key value
    for a dictionary
    '''
  # Use input() for keys and key values
  while True:
      user_k = input("Enter dictionary key (empty to exit): ")
      if user_k == '':
          break
      user_v = input("Enter value for that key (empty to exit): ")
      if user_v == '':
          break
      d[user_k] = user_v
        
def print_dictionary(d):
    '''
    Function prints the dictionary into two columns: Keys and Values
    '''
  # Function constants
  # Column spacing value (integer)
  # Key column header
    print(pad_string("Key",7,dir='R'),end='')
  # Value column header
    print("Value")
    print(pad_string("-----",7,dir='R'),end='')
    print("-----")
    
    for key in d:
        print(pad_string(key,7,dir='R'),end='')
        print(d[key])
        
  # Get maximum dictionary key length
  # Use conditional to ensure maximum key length is at least
  # the length of the length of the key column header

  # Get maximum dictionary value length
  # Use conditional to ensure maximum value length is at least
  # the length of the length of the value column header

  # Calculate column padding length

  # Output column headers with key column header right padded

  # Output column header and dictionary data separator

  # Output dictionary keys (right padded) and dictionary values

def start():
  my_dictionary = {}
  create_dictionary(my_dictionary)
  print_dictionary(my_dictionary)
