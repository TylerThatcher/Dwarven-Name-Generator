#!/usr/bin/env python
# coding: utf-8

# In[6]:


def dwarven_name_generator():

    print('Welcome to the Dwarven name generator')
    firstname = input('What is your first name: ')

    eng_char = list(firstname.lower())

    if len(eng_char) > 4:

        firstname_split_char = eng_char[::2]

        firstname_split_string = ''.join(str(x) for x in firstname_split_char)

        dwarf_firstname = firstname_split_string.replace('a', 'a').replace('b', 'ba').replace('c', 'ca').replace('d','du').replace('e','e').replace('f','thu').replace('g','gaz').replace('h','h').replace('i','i').replace('j','ju').replace('k','ku').replace('l','lo').replace('m','ma').replace('n','nu').replace('o','o').replace('p','p').replace('q','ka').replace('r','ru').replace('s','ss').replace('t','tul').replace('u','ur').replace('v','').replace('w','uv').replace('x','ax').replace('y','u').replace('z','az')

        print('Your Dwarven name is:')
        print(dwarf_firstname.capitalize())

    else:

        firstname_split_string = ''.join(str(x) for x in eng_char)

        dwarf_firstname = firstname_split_string.replace('a', 'a').replace('b', 'ba').replace('c', 'ca').replace('d','du').replace('e','e').replace('f','thu').replace('g','gaz').replace('h','h').replace('i','i').replace('j','ju').replace('k','ku').replace('l','lo').replace('m','ma').replace('n','nu').replace('o','o').replace('p','p').replace('q','ka').replace('r','ru').replace('s','ss').replace('t','tul').replace('u','ur').replace('v','').replace('w','uv').replace('x','ax').replace('y','u').replace('z','az')

        print('Your Dwarven name is:')
        print(dwarf_firstname.capitalize())

    surname_question = input('Would you like a surname? Y/N: ').lower().startswith('y')

    if surname_question is False:
        print('Goodbye')
        
    else:
        
        surname = input('What is your surname: ')
        
        eng_sur_char = list(surname.lower())

        if len(eng_sur_char) > 4:

            sur_split_char = eng_sur_char[::2]

            sur_split_string = ''.join(str(x) for x in sur_split_char)

            dwarf_surname = sur_split_string.replace('a', 'a').replace('b', 'ba').replace('c', 'ca').replace('d','du').replace('e','e').replace('f','thu').replace('g','gaz').replace('h','h').replace('i','i').replace('j','ju').replace('k','ku').replace('l','lo').replace('m','ma').replace('n','nu').replace('o','o').replace('p','p').replace('q','ka').replace('r','ru').replace('s','ss').replace('t','tul').replace('u','ur').replace('v','').replace('w','uv').replace('x','ax').replace('y','u').replace('z','az')

            print('Your full Dwarven name is:')
            print(dwarf_firstname.capitalize() + ' ' + dwarf_surname.capitalize())
            
        else:

            sur_split_string = ''.join(str(x) for x in eng_sur_char)

            dwarf_surname = sur_split_string.replace('a', 'a').replace('b', 'ba').replace('c', 'ca').replace('d','du').replace('e','e').replace('f','thu').replace('g','gaz').replace('h','h').replace('i','i').replace('j','ju').replace('k','ku').replace('l','lo').replace('m','ma').replace('n','nu').replace('o','o').replace('p','p').replace('q','ka').replace('r','ru').replace('s','ss').replace('t','tul').replace('u','ur').replace('v','').replace('w','uv').replace('x','ax').replace('y','u').replace('z','az')

            print('Your full Dwarven name is:')
            print(dwarf_firstname.capitalize() + ' ' + dwarf_surname.capitalize())

