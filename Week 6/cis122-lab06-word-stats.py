'''
CIS 122 Summer 2020 Lab 6
Author: Morgan Bartlett
Credit:
Description: Program gives different stats about the words in a .txt file
'''
import math

def word_count():
    # Open file
    fin = open("words_alpha.txt")
    # Count the amount of words in the file
    count = 0
    for line in fin:
        count = count + 1
    # Close file
    fin.close()
    # Print results
    return count

def long_word():
    # Initialize an empty string for the longest word
    long_word = ''
    # Open file
    fin = open("words_alpha.txt")
    # Loop over all the words
    for word in fin:
        # Check to see if word is longer than long_word
        if len(word) > len(long_word):
            long_word = word
    # Close file
    fin.close()
    w_count = 0
    w_count = len(long_word) - 1
    # Return the longest word
    return long_word + " ("+str(w_count)+")"

def short_word():
    # Initialize an empty string for the shortest word
    short_word = ''
    # Open file
    fin = open("words_alpha.txt")
    # Loop over all the words
    for word in fin:
        # Check to see if word is shorter than short_word
        if len(word) < len(short_word):
            short_word = word
    # Close file
    fin.close()
    # Return the shortest word
    w_count = 0
    w_count = len(short_word) + 1
    return short_word + " ("+str(w_count)+")"

# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
# The above link is how I learned to format the percentages

def palindrome():
    fin = open("words_alpha.txt")
    percent = 0
    p_count = 0
    for word in fin:
        txt = word.lower().split()
        for i in txt:
            if i == i[::-1]:
                p_count = p_count + 1
    fin.close()
    percent = p_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(p_count) + " ("+str(f_percent)+")"
'''
The following functions match and count each letter to the corresponding
character at index 0. Returns the count when called
'''
def count_a():
    l_count = 0
    alphabet = 'a'
    fin = open("words_alpha.txt")
    percent = 0
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_b():
    l_count = 0
    alphabet = 'b'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_c():
    l_count = 0
    alphabet = 'c'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_d():
    l_count = 0
    alphabet = 'd'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_e():
    l_count = 0
    alphabet = 'e'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_f():
    l_count = 0
    alphabet = 'f '
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_g():
    l_count = 0
    alphabet = 'g'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_h():
    l_count = 0
    alphabet = 'h'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_i():
    l_count = 0
    alphabet = 'i'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_j():
    l_count = 0
    alphabet = 'j'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_k():
    l_count = 0
    alphabet = 'k'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_l():
    l_count = 0
    alphabet = 'l'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_m():
    l_count = 0
    alphabet = 'm'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_n():
    l_count = 0
    alphabet = 'n'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_o():
    l_count = 0
    alphabet = 'o'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_p():
    l_count = 0
    alphabet = 'p'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_q():
    l_count = 0
    alphabet = 'q'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_r():
    l_count = 0
    alphabet = 'r'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_s():
    l_count = 0
    alphabet = 's'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_t():
    l_count = 0
    alphabet = 't'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_u():
    l_count = 0
    alphabet = 'u'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_u():
    l_count = 0
    alphabet = 'u'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_v():
    l_count = 0
    alphabet = 'v'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_w():
    l_count = 0
    alphabet = 'w'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_x():
    l_count = 0
    alphabet = 'x'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_y():
    l_count = 0
    alphabet = 'y'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_z():
    l_count = 0
    alphabet = 'z'
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

def count_():
    l_count = 0
    alphabet = ' '
    fin = open("words_alpha.txt")
    for letter in alphabet:
        for char in fin:
            if letter == char[0]:
                l_count += 1
    fin.close()
    percent = l_count / 370099
    f_percent = "{:.2%}".format(percent)
    return str(l_count) + " ("+str(f_percent)+")"

print("Count:",word_count())
print("Longest word is",long_word())
print("Shortest word is",short_word())
print("Palindromes:",palindrome())
print("First letter counts")
print("A:",count_a())
print("B:",count_b())
print("C:",count_c())
print("D:",count_d())
print("E:",count_e())
print("F:",count_f())
print("G:",count_g())
print("H:",count_h())
print("I:",count_i())
print("J:",count_j())
print("K:",count_k())
print("L:",count_l())
print("M:",count_m())
print("N:",count_n())
print("O:",count_o())
print("P:",count_p())
print("Q:",count_q())
print("R:",count_r())
print("S:",count_s())
print("T:",count_t())
print("U:",count_u())
print("V:",count_v())
print("W:",count_w())
print("X:",count_x())
print("Y:",count_y())
print("Z:",count_z())
print("Other:",count_())
