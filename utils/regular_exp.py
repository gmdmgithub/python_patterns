"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String
\       - Escape character


[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

#Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


"""


import re
from os.path import dirname,join


simple_str = 'Serching in 3 string with 23 regular expression 34 is simple - very simple 32-345 +44234654234 test@git.com'

#search - two parameters returs group
result = re.search(r'v\w\w\w',simple_str) # only 4 character start from v
print('search', result.group())

# findall(reg,str) - two parameters returns all the substrings matches as a list (empty if not)
# match(reg,str) -return first match if not None

result = re.findall('v\w\w\w',simple_str) # only 4 character start from v
print('findall',result)
print(dir(re))

result = re.match('S\w\w\w', simple_str)  # only at the begining of the string!!!
print('match', result, result.group())# group from matching gives string

result=re.split(r'\d+', simple_str)
print('replace all with regexp', result)

result = re.sub(r'simple','complicated', simple_str)  # replace all
print('split with regexp', result)


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
moad_sd.pc@delj.com
moad-sd.pc12@delj23.com
moad-sd.pc12@delj23.eu
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''


def search_and_print(mathces):
    for match in matches:
        print('match', match)
    print('mathes:', matches)


def read_sample_file():
    try:
        #with open(dirname(__file__) + "\\" + 'pattern-test.txt','r',encoding='utf-8') as f:
        with open(join(dirname(__file__), 'pattern-test.txt'),'r',encoding='utf-8') as f:
            conttent = f.read()
            return conttent
    except Exception as e:
        print(str(e))
        return text_to_search


#pattern to test
pattern = re.compile(r'Mr')  #r - givs raw example "\tno" will be '    no"
pattern = re.compile(r'\.aaaa')  #only dot (\) - escape character

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

pattern = re.compile(r'[89]0\d[.-]\d\d\d[.-]\d\d\d\d')

pattern = re.compile(r'[a-zA-Z-0-9_.-]+@[a-zA-Z-0-9_.-]+\.(com|net|edu)')  #only emails from domain com net or edu

# only search when call directly
if __name__ == "__main__":
    #finditter to get itteration object
    matches = pattern.finditer(text_to_search)
    #matches = pattern.finditer(read_sample_file())

    search_and_print(matches)


def check_username_pattern(username):
    """ Check if the pattern is corrct for the username name.
    Arguments:
        :username: name to check in the given pattern
    """
    username_pattern = re.compile(r'[^[0-9_]\w+')  #cannot start from letter only word
    return username_pattern.fullmatch(username)  #fullmatch search at start


if __name__ == "__main__":
    print('check:', check_username_pattern('0testme'))
    print('check 2', check_username_pattern('testme0'))
