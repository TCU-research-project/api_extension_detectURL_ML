# Program starts
import codecs
import decimal
import mechanize
import urllib.request
import enchant  # version 3.2.1
from hyphenate import hyphenate_word  # version 1.1.0
from ipwhois import IPWhois  # version 0.11.0
from tld import get_tld  # version 0.12.6
import math  # version 1.0.1
from collections import Counter
import urllib.parse
import string
import tldextract  # version 3.1.2
import time
from datetime import datetime, date  # version 2.0.2
import requests  # version 2.25.1
from bs4 import BeautifulSoup  # version 4.9.3
import numpy  # version 1.19.5
import whois  # version 0.7.3
import socket  # version 0.1.5
from warnings import filterwarnings
import pandas as pd
filterwarnings(action="ignore")
import distutils.spawn
from urllib.request import Request, urlopen
import csv
import os.path
# Following list is defined to check user type mistake keyboards. for check Deep Feature: insertion, replacement

qwerty = {'1': '2q', '2': '3wq1', '3': '4ew2', '4': '5re3', '5': '6tr4', '6': '7yt5', '7': '8uy6', '8': '9iu7',
          '9': '0oi8', '0': 'po9', 'q': '12wa', 'w': '3esaq2', 'e': '4rdsw3', 'r': '5tfde4', 't': '6ygfr5',
          'y': '7uhgt6', 'u': '8ijhy7', 'i': '9okju8', 'o': '0plki9', 'p': 'lo0', 'a': 'qwsz', 's': 'edxzaw',
          'd': 'rfcxse', 'f': 'tgvcdr', 'g': 'yhbvft', 'h': 'ujnbgy', 'j': 'ikmnhu', 'k': 'olmji', 'l': 'kop',
          'z': 'asx', 'x': 'zsdc', 'c': 'xdfv', 'v': 'cfgb', 'b': 'vghn', 'n': 'bhjm', 'm': 'njk'}

qwertz = {'1': '2q', '2': '3wq1', '3': '4ew2', '4': '5re3', '5': '6tr4', '6': '7zt5', '7': '8uz6', '8': '9iu7',
          '9': '0oi8', '0': 'po9', 'q': '12wa', 'w': '3esaq2', 'e': '4rdsw3', 'r': '5tfde4', 't': '6zgfr5',
          'z': '7uhgt6', 'u': '8ijhz7', 'i': '9okju8', 'o': '0plki9', 'p': 'lo0', 'a': 'qwsy', 's': 'edxyaw',
          'd': 'rfcxse', 'f': 'tgvcdr', 'g': 'zhbvft', 'h': 'ujnbgz', 'j': 'ikmnhu', 'k': 'olmji', 'l': 'kop',
          'y': 'asx', 'x': 'ysdc', 'c': 'xdfv', 'v': 'cfgb', 'b': 'vghn', 'n': 'bhjm', 'm': 'njk'}

azerty = {'1': '2a', '2': '3za1', '3': '4ez2', '4': '5re3', '5': '6tr4', '6': '7yt5', '7': '8uy6', '8': '9iu7',
          '9': '0oi8', '0': 'po9', 'a': '2zq1', 'z': '3esqa2', 'e': '4rdsz3', 'r': '5tfde4', 't': '6ygfr5',
          'y': '7uhgt6', 'u': '8ijhy7', 'i': '9okju8', 'o': '0plki9', 'p': 'lo0m', 'q': 'zswa', 's': 'edxwqz',
          'd': 'rfcxse', 'f': 'tgvcdr', 'g': 'yhbvft', 'h': 'ujnbgy', 'j': 'iknhu', 'k': 'olji', 'l': 'kopm',
          'm': 'lp', 'w': 'sxq', 'x': 'wsdc', 'c': 'xdfv', 'v': 'cfgb', 'b': 'vghn', 'n': 'bhj'}

keyboards = [qwerty, qwertz, azerty]

homo_dictionary = {}


# Function to calculate the total time taken for the execution of the program

def functionoftime():
    start_time = time.time()
    print("--- Execution Time is %s seconds ---" % (time.time() - start_time))


def is_registered(domain_name):
    try:
        w = whois(domain_name)
        print(w)
    except Exception:
        return 0
    else:
        return bool(w.domain_name)


def load_letters():
    with codecs.open('homoglyph', 'rU', encoding='utf8') as f:
        for line in f:
            key_value = line.split('\n')[0].split(',')
            homo_dictionary[key_value[0]] = key_value[1].split(' ')


# Function to count numeric characters Feature13

def NumericCharCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of numeric characters
    numeric = set("0123456789")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If numeric character is present
        # in set numeric
        if num in numeric:
            count = count + 1

    return count


# Function to count english letters Feature14

def EnglishLetterCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of english letters
    engletter = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If english letter is present
        # in set engletter
        if num in engletter:
            count = count + 1

    return count


# Function to count Special Characters Feature15

def SpecialCharCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of special characters
    specialchar = set("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\"")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If special character is present
        # in set specialchar
        if num in specialchar:
            count = count + 1

    return count


# Function to count Dots Feature16

def DotCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Dot
    dot = set(".")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If dot character is present
        # in set dot
        if num in dot:
            count = count + 1

    return count


# Function to count Semi-colon Feature17

def SemiColCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Semi-colon
    semicolon = set(";")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If semi-colon character is present
        # in set semicolon
        if num in semicolon:
            count = count + 1

    return count


# Function to count Underscore Feature18

def UnderscoreCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Underscore
    underscore = set("_")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If underscore character is present
        # in set underscore
        if num in underscore:
            count = count + 1

    return count


# Function to count Question Mark Feature19

def QuesMarkCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Question Mark
    quesmark = set("?")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If Question Mark character is present
        # in set QuesMark
        if num in quesmark:
            count = count + 1

    return count


# Function to count Hash Character Feature20

def HashCharCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Hash Character
    hashchar = set("#")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If Hash Character is present
        # in set hashchar
        if num in hashchar:
            count = count + 1

    return count


# Function to count Equals to Character Feature21

def EqualCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Equals to Character
    equalchar = set("=")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If Equals to Character character is present
        # in set equalchar
        if num in equalchar:
            count = count + 1

    return count


# Function to count Percentage Character Feature22

def PercentCharCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Percentage Character
    percentchar = set("%")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If Percentage Character is present
        # in set percentchar
        if num in percentchar:
            count = count + 1

    return count


# Function to count Ampersand Character Feature23

def AmpersandCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Ampersand Character
    ampersandchar = set("&")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If Ampersand Character is present
        # in set ampersandchar
        if num in ampersandchar:
            count = count + 1

    return count


# Function to count Dash Character Feature24

def DashCharCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Dash Character
    dashchar = set("-")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If Dash Character is present
        # in set dashchar
        if num in dashchar:
            count = count + 1

    return count


# Function to count Delimiters Feature25

def DelimiterCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Delimiter Characters
    delim = set("(){}[]<>'\"")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If Delimiter Character is present
        # in set delimiter
        if num in delim:
            count = count + 1

    str1 = str.lower()
    # In string, what is the count that <? occurs
    a = str1.count("<?")
    if a != 0:
        count = count - a

    str2 = str.lower()
    # In string, what is the count that ?> occurs
    b = str2.count("?>")
    if b != 0:
        count = count - b

    str3 = str.lower()
    # In string, what is the count that <% occurs
    c = str3.count("<%")
    if c != 0:
        count = count - c

    str4 = str.lower()
    # In string, what is the count that %> occurs
    d = str4.count("%>")
    if d != 0:
        count = count - d

    str5 = str.lower()
    # In string, what is the count that /* occurs
    e = str5.count("/*")

    str6 = str.lower()
    # In string, what is the count that */ occurs
    f = str6.count("*/")

    return count + a + b + c + d + e + f


# Function to count At Character Feature26

def AtCharCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of At Character
    atchar = set("@")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If At Character is present
        # in set atchar
        if num in atchar:
            count = count + 1

    return count


# Function to count Tilde Character Feature27

def TildeCharCount(str):
    # Initializing count variable to 0
    count = 0

    # Creating a set of Tilde Character
    tildechar = set("~")

    # Loop to traverse the num
    # in the given string
    for num in str:

        # If Tilde Character character is present
        # in set tildechar
        if num in tildechar:
            count = count + 1

    return count


# Function to count Double Slash Feature28

def DoubleSlashCount(str):
    str = str.lower()
    # In string, what is the count that // occurs
    count = str.count("//")
    return count


# Function to calculate ratio of digits to alphabets Feature09

def DigitAlphabetRatio(str):
    digit = 0
    numeric = set("0123456789")

    for num in str:
        if num in numeric:
            digit = digit + 1

    alphabet = 0
    engletter = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    flag = "Undefined"
    for num in str:
        if num in engletter:
            alphabet = alphabet + 1

    if alphabet != 0:
        ratio = digit / alphabet
        return ratio

    else:
        return flag


# Function to calculate ratio of special characters to alphabets Feature10

def SpecialcharAlphabetRatio(str):
    schar = 0
    specialchar = set("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\"")

    for num in str:
        if num in specialchar:
            schar = schar + 1

    alphabet = 0
    engletter = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    flag = "Undefined"
    for num in str:
        if num in engletter:
            alphabet = alphabet + 1

    if alphabet != 0:
        ratio = schar / alphabet
        return ratio

    else:
        return flag


# Function to calculate ratio of uppercase letters to lowercase letters Feature11

def UppercaseLowercaseRatio(str):
    ucase = 0
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for num in str:
        if num in uppercase:
            ucase = ucase + 1

    lcase = 0
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    flag = "Undefined"

    for num in str:
        if num in lowercase:
            lcase = lcase + 1

    if lcase != 0:
        ratio = ucase / lcase
        return ratio

    else:
        return flag


# Function to find length of the URL Feature01

def URLLength(str):
    length = len(str)
    # print ("The length of the URL is: ", length)
    return length


# Function to compute entropy of the URL Feature51

def Entropy(data, unit='natural'):
    base = {
        'shannon': 2.,
        'natural': math.exp(1),
        'hartley': 10.
    }

    if len(data) <= 1:
        return 0

    counts = Counter()

    for d in data:
        counts[d] += 1

    ent = 0

    probs = [float(c) / len(data) for c in counts.values()]
    for p in probs:
        if p > 0.:
            ent -= p * math.log(p, base[unit])

    return ent


# Function to check if IP address is used in hostname Feature02

def CheckIPAsHostName(stri):
    parsed_url = urllib.parse.urlparse(stri)
    # print(parsed_url)
    h = parsed_url.netloc
    if type(h) == str:
        flag = 1
    else:
        flag = 0
    return flag


# Function to find the length of the host name Feature37

def HostNameLength(str):
    parsed_url = urllib.parse.urlparse(str)
    # print(parsed_url.netloc)
    return len(parsed_url.netloc)


# Function to find the length of the path of the URL Feature38

def PathLength(str):
    parsed_url = urllib.parse.urlparse(str)
    # print(parsed_url.path)
    return len(parsed_url.path)


# Function to find the length of the Query of the URL Feature39

def QueryLength(str):
    parsed_url = urllib.parse.urlparse(str)
    # print(parsed_url.query)
    return len(parsed_url.query)


# Function to find if there is https occurs in host name Feature36

def HttpsInHostName(str):
    parsed_url = urllib.parse.urlparse(str)
    hostname = parsed_url.netloc
    # print(hostname)
    hostname = hostname.lower()
    # In string, what is the count that // occurs
    count = 0
    count = hostname.count("https")
    if count == 0:
        # print("Not present")
        return 0
    else:
        if count != 0:
            # print("Present")
            return 1


# Function to calculate ratio of Domain length to URL length Feature12

def DomainURLRatio(str):
    urllength = len(str)

    parsed_url = urllib.parse.urlparse(str)
    domain = parsed_url.netloc
    domainlength = len(domain)
    flag = "Undefined"

    if urllength != 0:
        ratio = domainlength / urllength
        return ratio

    else:
        return flag


# Function to find TLD of the URL Feature30


def TLD(str):
    if not (str.startswith('http://') or str.startswith('https://')):
        str = 'http://{}'.format(str)
    else:
        return get_tld(str)
    return get_tld(str)


# Function to check if the URL is hashed or not Feature29

def IsHashed(str):
    def is_hex(str):

        hex_digits = set(string.hexdigits)

        return all(c in hex_digits for c in str)

    ishash = False
    if len(str) == 16 or len(str) == 32 or len(str) == 64 and str.isdigit == True:
        ishash = True
        # print("Hashed")

    if (len(str) == 32 or len(str) == 64 or len(str) == 128) and is_hex(str) == True:
        ishash = True
        return 1
    else:
        # print("Not Hashed")
        return 0


# Function to check if TLD or ccTLD is used in the subdomain of website URL Feature34

def TLDInSubdomain(str):
    res = get_tld(str, fix_protocol=True)
    subdom1 = (tldextract.extract(str))
    subdom2 = (subdom1.subdomain)
    if res in subdom2:
        # print("Yes")
        return 1
    else:
        # print("No")
        return 0


# Function to check if TLD or ccTLD is used in the path of website URL Feature35

def TLDInPath(str):
    parsed_url = urllib.parse.urlparse(str)
    h = parsed_url.path
    # print(h)
    res = get_tld(str, fix_protocol=True)
    if res in h:
        # print("Yes")
        return 1
    else:
        # print("No")
        return 0


# Function to check if https is used in the website URL Feature32

def HttpsInUrl(str):
    res = "https"
    if res in str:
        # print("Yes")
        return 1
    else:
        # print("No")
        return 0


# Function to find the distance of digit to alphabet Feature31

def DistDigitAlphabet(str):
    r_avg = 0
    letters = sum(c.isalpha() for c in str)
    # print(letters)
    numbers = sum(c.isdigit() for c in str)
    # print(numbers)
    number_ratio = numbers / len(str)
    alphabet_ratio = letters / len(str)
    # print(alphabet_ratio)
    # print(number_ratio)

    if alphabet_ratio != 0:
        r_avg = r_avg + (number_ratio / alphabet_ratio)
    elif alphabet_ratio == 0:
        r_avg = r_avg + 1

    # print(r_avg)
    # x = number_ratio / alphabet_ratio
    # print(x)

    if alphabet_ratio != 0:
        r_distance = r_avg - (number_ratio / alphabet_ratio)
    elif alphabet_ratio == 0:
        r_distance = r_avg - 1

    return r_distance


# Function to check if the domain name is an English word Feature41

def IsDomainEnglishWord(str):
    parsedurl = tldextract.extract(str)
    dom = parsedurl.domain
    # print(dom)

    res = dom.isalpha()
    if res == True:
        return 1
    else:
        return  0


# Function to check whether the domain name is meaningful Feature42

def IsDomainMeaningful(str):
    dictionary = enchant.Dict("en_US")
    parsedurl = tldextract.extract(str)
    dom = parsedurl.domain
    # print(dom)

    res = dom.isalpha()
    # print(res)

    if res == True:
        res2 = dictionary.check(dom)
        if res2 == True:
            # print("Meaningful")
            return 1
        else:
            # print("Not meaningful")
            return 0


# Function to check whether the domain name is pronounceable Feature43

def IsDomainPronounceable(str):
    dictionary = enchant.Dict("en_US")
    parsedurl = tldextract.extract(str)
    dom = parsedurl.domain
    res2 = dictionary.check(dom)
    res3 = dom.isalpha()

    check = 2
    if res3 == True and res2 == True:
        # if res == "n" or res == "v" or res == "a" or res == "r":
        check = 1
    else:
        check = 0

    if check == 1:
        # print("Pronounceable")
        return 1
    else:
        # print("Not pronounceable")
        return 0


# Function to check whether the domain name is random Feature44

def IsDomainRandom(str):
    dictionary = enchant.Dict("en_US")
    parsedurl = tldextract.extract(str)
    dom = parsedurl.domain
    # print(dom)

    # syn = wordnet.synsets(dom)[0]
    # res = syn.pos()
    # print(res)

    res2 = dictionary.check(dom)
    res3 = dom.isalpha()

    check = 2
    if res3 == True and res2 == True:
        # if res == "n" or res == "v" or res == "a" or res == "r":
        check = 1
    else:
        check = 0

    if check == 1:
        # print("Not Random")
        return 0
    else:
        # print("Random")
        return 1


# Function to calculate Unigram probability of the URL Feature45

def Unigram(str):
    # print("Hello World")

    concat_total_url = ''
    val_without_tld = (str.rsplit('.', 1))[0]
    # print(val_without_tld)

    concat_total_url = concat_total_url + val_without_tld
    # print(concat_total_url)

    # for calculate distribuation alphabet for Unigram calculation
    len_concat_total_url = len(concat_total_url)
    res = Counter(concat_total_url[idx: idx + 1] for idx in range(len_concat_total_url - 1))
    dict_res = dict(res)
    for c in dict_res:
        if len(c) == 1:
            dict_res[c] = dict_res[c] / len_concat_total_url

    # calculate Unigram probability
    concat_url = val_without_tld
    p_uni_gram = 1
    concat_url = val_without_tld
    # print(dict_res)

    # print(type(dict_res))
    res = 1
    for val in dict_res.values():
        res = res * val

    p_uni_gram = res / len(dict_res)
    return p_uni_gram


# Function to calculate Bigram probability of the URL Feature46

def Bigram(str):
    concat_total_url = ''
    val_without_tld = (str.rsplit('.', 1))[0]
    # print(val_without_tld)

    concat_total_url = concat_total_url + val_without_tld
    # print(concat_total_url)

    # for calculate distribuation alphabet for Bigram calculation
    len_concat_total_url = len(concat_total_url)
    res1 = Counter(concat_total_url[idx: idx + 2] for idx in range(len_concat_total_url - 1))
    dict_res1 = dict(res1)
    for c1 in dict_res1:
        if len(c1) == 2:
            dict_res1[c1] = dict_res1[c1] / len_concat_total_url

    # calculate Bigram probability
    concat_url = val_without_tld
    len_concat_total_url_bigram = len(concat_url)
    res_bigram = Counter(concat_url[idx1: idx1 + 2] for idx1 in range(len_concat_total_url_bigram - 1))
    p_bi_gram = 1
    for u1 in res_bigram:
        if len(u1) == 2:
            p_bi_gram = p_bi_gram * dict_res1[u1]
    p_bi_gram = p_bi_gram * (len(concat_url) / len_concat_total_url * 100)
    decimal.getcontext().prec = 25  # Change 25 to the precision you want.
    p_bi_gram = decimal.Decimal(p_bi_gram) / decimal.Decimal(10)

    return p_bi_gram


# Function to calculate Trigram probability of the URL Feature47

def Trigram(str):
    concat_total_url = ''
    val_without_tld = (str.rsplit('.', 1))[0]
    # print(val_without_tld)

    concat_total_url = concat_total_url + val_without_tld
    # print(concat_total_url)

    # for calculate distribuation alphabet for Trigram calculation
    len_concat_total_url = len(concat_total_url)
    res2 = Counter(concat_total_url[idx: idx + 3] for idx in range(len_concat_total_url - 1))
    dict_res2 = dict(res2)
    for c2 in dict_res2:
        if len(c2) == 3:
            dict_res2[c2] = dict_res2[c2] / len_concat_total_url

    # calculate Trigram probability
    concat_url = val_without_tld
    len_concat_total_url_trigram = len(concat_url)
    res_trigram = Counter(concat_url[idx2: idx2 + 3] for idx2 in range(len_concat_total_url_trigram - 1))
    p_tri_gram = 1
    for u2 in res_trigram:
        if len(u2) == 3:
            p_tri_gram = p_tri_gram * dict_res2[u2]
    p_tri_gram = p_tri_gram * (len(concat_url) / len_concat_total_url * 100)
    decimal.getcontext().prec = 25  # Change 25 to the precision you want.
    p_tri_gram = decimal.Decimal(p_tri_gram) / decimal.Decimal(10)

    return p_tri_gram


# Function to count number of sensitive words in a webpage Feature48

def SensitiveWordCount(str):
    url = str
    fr = []
    count = 0
    wanted = ['bank', 'Bank', 'banking', 'architect', 'chemist', 'pharma', 'account', 'credit', 'transfer', 'allow',
              'assure', 'government', 'organisation', 'fund', 'secure', 'confirm', 'Secure', 'Confirm', 'webscr',
              'login', 'Login', 'Log in', 'Log In', 'ebayisapi', 'sign in', 'Sign in', 'Sign In', 'sign up', 'Sign up',
              'Sign Up', 'trust', 'authority', 'offer', 'accept', 'Accept', 'admit', 'allow', 'cookies', 'Cookies',
              'safe', 'browse', 'fix', 'get', 'cash', 'credit', 'buy', 'purchase', 'coin', 'money', 'obtain', 'help',
              'connect', 'drug']
    a = requests.get(url).text
    soup = BeautifulSoup(a, 'html.parser')
    for word in wanted:
        freq = soup.get_text().lower().count(word)
        dic = {'phrase': word, 'frequency': freq}
        fr.append(dic)
        count = count + freq
        # print('Frequency of', word, 'is:', freq)
    return count


"""
# Function to check if the domain name is present in suspicious list Feature49

def InSuspiciousList(str):
    dom = str
    ispresent = 0
    with open('Suspicious_file_name.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')  # good point by @paco
        for row in reader:
            for field in row:
                if field == dom:
                    #print("Present")
                    ispresent =1
    return ispresent

"""


# check Deep Feature Homoglyph and called in Containment()

def switch_all_letters(url):
    domains = []
    # url = get_tld(url, as_object=True, fix_protocol=True)

    domain = url
    a = []
    j = 0
    glyphs = homo_dictionary
    result1 = set()
    for ws in range(1, len(domain)):
        for i in range(0, (len(domain) - ws) + 1):
            win = domain[i:i + ws]
            j = 0
            while j < ws:
                c = win[j]
                if c in glyphs:
                    win_copy = win
                    for g in glyphs[c]:
                        win = win.replace(c, g)
                        result1.add(domain[:i] + win + domain[i + ws:])
                        win = win_copy
                j += 1

    result2 = set()
    for domain in result1:
        for ws in range(1, len(domain)):
            for i in range(0, (len(domain) - ws) + 1):
                win = domain[i:i + ws]
                j = 0
                while j < ws:
                    c = win[j]
                    if c in glyphs:
                        win_copy = win
                        for g in glyphs[c]:
                            win = win.replace(c, g)
                            result2.add(domain[:i] + win + domain[i + ws:])
                            win = win_copy
                    j += 1
    return list(result1 | result2)


# check Deep Feature Vowel_swap and called in Containment()

def vowel_swap(domain):
    vowels = 'aeiou'
    result = []

    for i in range(0, len(domain)):
        for vowel in vowels:
            if domain[i] in vowels:
                result.append(domain[:i] + vowel + domain[i + 1:])

    return list(set(result))


# check Deep Feature bitsquatting and called in Containment()

def bitsquatting(domain):
    result = []
    masks = [1, 2, 4, 8, 16, 32, 64, 128]

    for i in range(0, len(domain)):
        c = domain[i]
        for j in range(0, len(masks)):
            b = chr(ord(c) ^ masks[j])
            o = ord(b)
            if (o >= 48 and o <= 57) or (o >= 97 and o <= 122) or o == 45:
                result.append(domain[:i] + b + domain[i + 1:])

    return result


# check Deep Feature insertion and called in Containment()

def insertion(domain):
    result = []

    for i in range(1, len(domain) - 1):
        for keys in keyboards:
            if domain[i] in keys:
                for c in keys[domain[i]]:
                    result.append(domain[:i] + c + domain[i] + domain[i + 1:])
                    result.append(domain[:i] + domain[i] + c + domain[i + 1:])

    return list(set(result))


# check Deep Feature omission and called in Containment()

def omission(domain):
    result = []

    for i in range(0, len(domain)):
        result.append(domain[:i] + domain[i + 1:])

    return list(set(result))


# check Deep Feature repetition and called in Containment()

def repetition(domain):
    result = []

    for i in range(0, len(domain)):
        if domain[i].isalnum():
            result.append(domain[:i] + domain[i] + domain[i] + domain[i + 1:])

    return list(set(result))


# check Deep Feature replacement and called in Containment()

def replacement(domain):
    result = []

    for i in range(0, len(domain)):
        for keys in keyboards:
            if domain[i] in keys:
                for c in keys[domain[i]]:
                    result.append(domain[:i] + c + domain[i + 1:])

    return list(set(result))


# check Deep Feature subdomain and called in Containment()

def subdomain(domain):
    result = []

    for i in range(1, len(domain) - 1):
        if domain[i] not in ['-', '.'] and domain[i - 1] not in ['-', '.']:
            result.append(domain[:i] + '.' + domain[i:])

    return result


# check Deep Feature transpose and called in Containment()

def transposition(domain):
    result = []

    for i in range(0, len(domain) - 1):
        if domain[i + 1] != domain[i]:
            result.append(domain[:i] + domain[i + 1] + domain[i] + domain[i + 2:])

    return result


# check Deep Feature addition and called in Containment()

def addition(domain):
    result = []

    for i in range(97, 123):
        result.append(domain + chr(i))

    return result


# Function for the following features : Hyphenstring, Homoglyph, Vowel, Bitsquatting, Insertion, Omission, Repeatition,
# Replacement, Subdomain, Transposition, Addition String : Feature52, Feature53, Feature54, Feature55,
#  Feature56, Feature57, Feature58, Feature59, Feature60, Feature61, Feature62

def Containment(str):
    val_without_tld = (str.rsplit('.', 1))[0]
    tld = (str.split('.'))[-1]
    # print(val_without_tld)

    hyphen_str = hyphenate_word(val_without_tld)

    if len(hyphen_str) == 0:
        hyphen_str = "No_hyphen"
    else:
        # print(hyphen_str)
        for domain in hyphen_str:
            # print(domain)
            if not is_registered(domain + '.' + tld):
                hyphen_str.remove(domain)
                if len(hyphen_str) != 0:
                    continue
                hyphen_str = "No_hyphen"

    # print(hyphen_str)

    homo_str = switch_all_letters(str)

    if len(homo_str) == 0:
        homo_str = "No_homo_str"
    else:
        for domain in homo_str:
            if not is_registered(domain + '.' + tld):
                homo_str.remove(domain)
                if len(homo_str) == 0:
                    homo_str = "No_homo_str"

    # print(homo_str)

    vowel_result = vowel_swap(val_without_tld)

    if len(vowel_result) == 0:
        vowel_result = "No_vowel_result"
    else:
        for domain in vowel_result:
            if not is_registered(domain + '.' + tld):
                vowel_result.remove(domain)
                if len(vowel_result) == 0:
                    vowel_result = "No_vowel_result"

    # print(vowel_result)

    bitsquatting_result = bitsquatting(val_without_tld)

    if len(bitsquatting_result) == 0:
        bitsquatting_result = "bitsquatting_result"
    else:
        for domain in bitsquatting_result:
            if not is_registered(domain + '.' + tld):
                bitsquatting_result.remove(domain)
                if len(bitsquatting_result) == 0:
                    bitsquatting_result = "bitsquatting_result"

    # print(bitsquatting_result)

    insertion_str = insertion(val_without_tld)

    if len(insertion_str) == 0:
        insertion_str = "No_insertion_str"
    else:
        for domain in insertion_str:
            if not is_registered(domain + '.' + tld):
                insertion_str.remove(domain)
                if len(insertion_str) == 0:
                    insertion_str = "No_insertion_str"

    # print(insertion_str)

    omission_str = omission(val_without_tld)

    if len(omission_str) == 0:
        omission_str = "No_omission_str"
    else:
        for domain in omission_str:
            if not is_registered(domain + '.' + tld):
                omission_str.remove(domain)
                if len(omission_str) == 0:
                    omission_str = "No_omission_str"

    # print(omission_str)

    repetition_str = repetition(val_without_tld)

    if len(repetition_str) == 0:
        repetition_str = "No_repetition_str"
    else:
        for domain in repetition_str:
            if not is_registered(domain + '.' + tld):
                repetition_str.remove(domain)
                if len(repetition_str) == 0:
                    repetition_str = "No_repetition_str"

    # print(repetition_str)

    replacement_str = replacement(val_without_tld)

    if len(replacement_str) == 0:
        replacement_str = "No_replacement_str"
    else:
        for domain in replacement_str:
            if not is_registered(domain + '.' + tld):
                replacement_str.remove(domain)
                if len(replacement_str) == 0:
                    replacement_str = "No_replacement_str"

    # print(replacement_str)

    subdomain_str = subdomain(val_without_tld)

    if len(subdomain_str) == 0:
        subdomain_str = "No_subdomain_str"
    else:
        for domain in subdomain_str:
            if not is_registered(domain + '.' + tld):
                subdomain_str.remove(domain)
                if len(subdomain_str) == 0:
                    subdomain_str = "No_subdomain_str"

    # print(subdomain_str)

    transposition_str = transposition(val_without_tld)

    if len(transposition_str) == 0:
        transposition_str = "No_transposition_str"
    else:
        for domain in transposition_str:
            if not is_registered(domain + '.' + tld):
                transposition_str.remove(domain)
                if len(transposition_str) == 0:
                    transposition_str = "No_transposition_str"

    # print(transposition_str)

    addition_str = addition(val_without_tld)

    if len(addition_str) == 0:
        addition_str = "No_addition_str"
    else:
        for domain in addition_str:
            if not is_registered(domain + '.' + tld):
                addition_str.remove(domain)
                if len(addition_str) == 0:
                    addition_str = "No_addition_str"

    # print(addition_str)
    arr = [hyphen_str, homo_str, vowel_result, bitsquatting_result, insertion_str, omission_str, repetition_str,
           replacement_str, subdomain_str, transposition_str, addition_str]
    return arr


# Calculate Levenshtein Distance

def LevenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1 - 1] == token2[t2 - 1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]


# Calculate entropy and called in CounterBlock()

def Entropy(s):
    p, lns = Counter(s), float(len(s))

    return -sum(count / lns * math.log(count / lns, 2) for count in p.values())


# Function to check if www is used in url Feature04

def URLWithoutwww(self):
    self = self.lower()
    # In string, what is the count that // occurs
    count = self.count("www.")
    if count == 0:
        flag = 0
        # print("No www used")
    else:
        flag = 1
        # print("www used")
    return flag


# Function to check if ftp:// is used in url Feature05

def FTPUsed(self):
    self = self.lower()
    # In string, what is the count that // occurs
    count = self.count("ftp://")
    if count == 0:
        flag = 0
        # print("No ftp:// used")
    else:
        flag = 1
        # print("ftp:// used")
    return flag


# Function to check if files is used in url Feature07

def FilesInURL(self):
    self = self.lower()
    # In string, what is the count that // occurs
    count = self.count("files")
    if count == 0:
        flag = 0
        # print("No files used")
    else:
        flag = 1
        # print("files used")
    return flag


# Function to check if .js is used in url Feature06

def JSUsed(self):
    self = self.lower()
    # In string, what is the count that // occurs
    count = self.count(".js")
    if count == 0:
        flag = 0
        # print("No .js used")
    else:
        flag = 1
        # print(".js used")
    return flag


# Function to check if .css is used in url Feature08

def CSSUsed(self):
    self = self.lower()
    # In string, what is the count that // occurs
    count = self.count("css")
    if count == 0:
        flag = 0
        # print("No css used")
    else:
        flag = 1
        # print("css used")
    return flag


# Function to find IPAddress Feature64

def IPAddress(str):
    parsed_url = urllib.parse.urlparse(str)
    dom = parsed_url.netloc
    # print(str)
    # print(dom)
    # print("Hello World!")
    stri = dom
    # print(stri)
    # input data like www.pythonguides.com
    IP_addres = socket.gethostbyname(stri)

    # obj = IPWhois(IP_addres)
    # res = obj.lookup()
    # print(res)
    # asn_num = res['asn']
    # print(res['asn_country_code'])
    # asn_country = res["nets"][0]['country']
    # print(res["nets"][0]['address'])
    # print(res["nets"][0]['name'])
    # asn_cidr = res["nets"][0]['cidr']
    # print(res["nets"][0]['state'])
    # asn_postal_code = res["nets"][0]['postal_code']
    # created_date = res["nets"][0]['created']
    # updated_date = res["nets"][0]['updated']

    if IP_addres == None:
        return 0
    else:
        return IP_addres

    # print(asn_num)
    # print(asn_country)
    # print(asn_cidr)
    # print(asn_postal_code)
    # print(created_date)
    # print(updated_date)


# Function to find ASN Number Feature65

def ASNNumber(str):
    parsed_url = urllib.parse.urlparse(str)
    dom = parsed_url.netloc
    # print(str)
    # print(dom)
    # print("Hello World!")
    stri = dom
    # print(stri)
    # input data like www.pythonguides.com
    IP_addres = socket.gethostbyname(stri)

    obj = IPWhois(IP_addres)
    res = obj.lookup_whois()
    # print(res)
    asn_num = res['asn']
    # print(res['asn_country_code'])

    if IP_addres == None:
        return 0
    else:
        return asn_num


# Function to find ASN Country Code Feature66

def ASNCountryCode(str):
    parsed_url = urllib.parse.urlparse(str)
    dom = parsed_url.netloc
    stri = dom
    IP_addres = socket.gethostbyname(stri)
    obj = IPWhois(IP_addres)
    res = obj.lookup_whois()
    # print(res)
    asn_country = res["nets"][0]['country']

    if IP_addres == None:
        return 0
    else:
        return asn_country


# Function to find ASN CIDR Feature67

def ASNCIDR(str):
    parsed_url = urllib.parse.urlparse(str)
    dom = parsed_url.netloc
    # print(str)
    # print(dom)
    # print("Hello World!")
    stri = dom
    # print(stri)
    # input data like www.pythonguides.com
    IP_addres = socket.gethostbyname(stri)

    obj = IPWhois(IP_addres)
    res = obj.lookup_whois()
    # print(res)
    asn_cidr = res["nets"][0]['cidr']

    if IP_addres == None:
        return 0
    else:
        return asn_cidr


# Function to find ASN Postal Code Feature68

def ASNPostalCode(str):
    parsed_url = urllib.parse.urlparse(str)
    dom = parsed_url.netloc
    # print(str)
    # print(dom)
    # print("Hello World!")
    stri = dom
    # print(stri)
    # input data like www.pythonguides.com
    IP_addres = socket.gethostbyname(stri)

    obj = IPWhois(IP_addres)
    res = obj.lookup_whois()
    # print(res)
    asn_postal_code = res["nets"][0]['postal_code']

    if IP_addres == None:
        return 0
    else:
        return asn_postal_code


# Function to find Creation Date Feature69

def ASNCreationDate(str):
    parsed_url = urllib.parse.urlparse(str)
    dom = parsed_url.netloc
    # print(str)
    # print(dom)
    # print("Hello World!")
    stri = dom
    # print(stri)
    # input data like www.pythonguides.com
    IP_addres = socket.gethostbyname(stri)

    obj = IPWhois(IP_addres)
    res = obj.lookup_whois()
    # print(res)
    created_date = res["nets"][0]['created']

    if IP_addres == None:
        return 0
    else:
        return created_date


# Function to find Updation Date Feature70

def ASNUpdationDate(str):
    parsed_url = urllib.parse.urlparse(str)
    dom = parsed_url.netloc
    # print(str)
    # print(dom)
    # print("Hello World!")
    stri = dom
    # print(stri)
    # input data like www.pythonguides.com
    IP_addres = socket.gethostbyname(stri)

    obj = IPWhois(IP_addres)
    res = obj.lookup_whois()
    # print(res)

    updated_date = res["nets"][0]['updated']

    if IP_addres == None:
        return 0
    else:
        return updated_date


# Function to check if any .exe file is contained in the URL Feature03

def CheckEXE(str):
    res = distutils.spawn.find_executable(str)
    if res == None:
        return 0
    else:
        return 1


# Function to count number of images in the webpage Feature71

def ImgCount(str):
    response = requests.get(str)
    soup = BeautifulSoup(response.content)

    a = len(soup.find_all('img'))
    # b = (get_img_cnt(str))
    return a
    # print(b)


# Function to count the number of links used in the webpage Feature72

def TotalLinks(str):
    # working with url having https or full address
    reqs = requests.get(str)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    count = 0
    urls = []
    for link in soup.find_all('a'):
        if link.get('href'):
            count = count + 1
    return count


# Source code
# def sourcecode(self):
#   response = request.urlopen(self)
#  # set the correct charset below
# print(page_source)


# Function to check if title tag is empty or not in HTML source code Feature83

def TitleCheck(self):
    # input data is url with protocol
    br = mechanize.Browser()
    br.set_handle_robots(False)
    # br.set_handle_refresh(0)
    # br.addheaders = [('User-agent',
    #                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36')]
    br.open(self)
    res = br.title()
    # print(res)
    if res == None:
        # print("Title is empty")
        return 1
    else:
        # print("Title not empty")
        return 0


# Function to check if HTML source code contains “mailto” Feature81

def CheckMailto(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # set the correct charset below

    # print(page_source)

    page_source = page_source.lower()
    # In string, what is the count that // occurs
    count = 0
    count = page_source.count(b'mailto')
    if count == 0:
        # print("No mailto ")
        return 0
    else:
        # print("Mailto used")
        return 1


# Function to check if iframe or frame is used in HTML source code Feature82

def CheckFrameTag(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    page_source = page_source.lower()
    # In string, what is the count that // occurs
    count1 = page_source.count(b'frame')
    count2 = page_source.count(b'iframe')
    count = count1 + count2
    # print(count2)
    # print(count1)
    if count == 0:
        # print("No frame tag used ")
        return 0
    else:
        # print("Frame tag used")
        return 1


# Function to check number of function eval() in HTML source code Feature84

def SourceEvalCount(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    page_source = page_source.lower()
    # In string, what is the count that // occurs
    count = 0
    count = page_source.count(b'eval(')
    return count


# Function to check number of function escape() in HTML source code Feature85

def SourceEscapeCount(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    page_source = page_source.lower()
    # In string, what is the count that // occurs
    count = page_source.count(b'escape(')

    return count


# Function to check number of function exec() in HTML source code Feature86

def SourceExecCount(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    page_source = page_source.lower()
    # In string, what is the count that // occurs
    count = page_source.count(b'exec(')

    return count


# Function to check number of function search() in HTML source code Feature87

def SourceSearchCount(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    page_source = page_source.lower()
    count = page_source.count(b'search(')

    return count


# Function to check if actions in the form of HTML source code does not contain text, but only images Feature88

def ImageOnlyInForm(self):
    response = requests.get(self)
    soup = BeautifulSoup(response.content)

    numimg = len(soup.find_all('img'))
    # print(numimg)

    # input data is url with protocol
    br = mechanize.Browser()
    br.set_handle_robots(False)
    # br.set_handle_refresh(False)
    # br.addheaders = [('User-agent',
    #                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36')]
    br.open(self)
    res = br.title()
    # print(res)

    if numimg != None and res == None:
        # print("Only Images")
        return 1
    else:
        # print("Text with Images")
        return 0


# Function to find the age of domain since it is registered Feature89

def DomainAgeInDays(self):
    parsed_url = urllib.parse.urlparse(self)
    dom = parsed_url.netloc
    # print(dom)
    IP_addres = socket.gethostbyname(dom)
    obj = IPWhois(IP_addres)
    res = obj.lookup_whois()
    # date_format = "%m/%d/%Y"
    created_date = res["nets"][0]['created']
    if created_date == None:
        return 0

    # print(created_date)
    created_year = int(created_date[0:4])
    created_month = int(created_date[5:7])
    created_day = int(created_date[8:10])
    today = date.today()
    # print(created_year)

    d0 = date(created_year, created_month, created_day)
    d1 = date(today.year, today.month, today.day)
    delta = d1 - d0
    # print(delta.days)

    return delta.days


# Function to check if HTML source code contains a JavaScript command to start a popup Window Feature80

def PopUpWindow(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    page_source = page_source.lower()
    # In string, what is the count that // occurs
    count1 = page_source.count(b'popup(')
    count2 = page_source.count(b'popupform(')
    count = count1 + count2
    if count == 0:
        # print("No popup command used")
        return 0
    else:
        # print("Popup command used")
        return 1


# Function to check if HTML source code contains a JavaScript command to turn off the right click of the mouse Feature79

def RightClickDisabled(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    page_source = page_source.lower()
    # In string, what is the count that // occurs
    count1 = page_source.count(b"document.addEventListener('contextmenu',")
    count2 = page_source.count(b"$(\"body\").on(\"contextmenu\".function(e)")
    count3 = page_source.count(b"$(\"img\").bind(\"contextmenu\".function(e)")
    count = count1 + count2 + count3
    if count == 0:
        # print("No command to disable right key")
        return 0
    else:
        # print("Disable right key command used")
        return 1


# Function to check if HTML source code contains a JavaScript command on MouseOver to display a fake URL in the
# status bar Feature78

def FakeLinkInStatusBar(self):
    # input data is url with protocol
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    page_source = page_source.lower()
    # In string, what is the count that // occurs
    count1 = page_source.count(b"onMouseOver=\"window.status=")
    count2 = page_source.count(b"onMouseOut=\"window.status=")
    count3 = page_source.count(b"onmouseover=\"window.status=")
    count4 = page_source.count(b"onmouseout=\"window.status=")
    count = count1 + count2 + count3 + count4
    if count == 0:
        # print("No fake URL in status bar")
        return 0
    else:
        # print("Fake URL in status bar")
        return 1


# Function to find total number of query parameters in the URL Feature73

def NumParameters(self):
    params = self.split('&')
    a = len(params) - 1
    return a


# Function to find total number of fragments in the URL Feature74

def NumFragments(self):
    fragments = self.split('#')
    a = len(fragments) - 1
    return a


# Function to count number of Body tag in a web page Feature75

def BodyTagCount(self):
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    count = page_source.count(b"</body>")
    return count


# Function to count number of Meta tag in a web page Feature76

def MetaTagCount(self):
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    count = page_source.count(b"<meta")
    return count


# Function to count number of Div tag in a web page Feature77

def DivTagCount(self):
    req = Request(self, headers={'User-Agent': 'Mozilla/5.0'})
    page_source = urlopen(req).read()
    # print(page_source)

    count = page_source.count(b"</div>")
    return count


# Function to check distribution of word based feature Feature40

def DistWordBased(self):
    count1 = self.count("admin")
    count2 = self.count("personal")
    count3 = self.count(".bin")
    count4 = self.count("update")
    count5 = self.count("verification")
    count6 = self.count("abuse")
    count7 = self.count(".php")

    count = count1 + count2 + count3 + count4 + count5 + count6 + count7
    if count == 0:
        # print("Doubtful words used")
        return 1
    else:
        # print("No such word used")
        return 0


# Function to check presence of file extention Feature33

def FileExtension(self):
    count1 = self.count(".zip")
    count2 = self.count(".jpg")
    count3 = self.count(".gif")
    count4 = self.count(".rar")
    count5 = self.count("download.php")
    count6 = self.count("mail.php")
    count7 = self.count(".jar")
    count8 = self.count(".swf")
    count9 = self.count(".cgi")

    count = count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9
    if count == 0:
        # print("No such word used")
        return 0
    else:
        # print("Such file extension present")
        return 1


# Function for google search feature of top 10 results Feature63

def GoogleSearchFeature(selfwp):
    parsed_url = urllib.parse.urlparse(selfwp)
    hostname = parsed_url.netloc
    count = 0
    num = 0
    ld = 0
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    # to search
    query = hostname
    print(hostname)
    for j in search(query, tld="com", num=10, stop=10, pause=3):
        # print(j)
        j = j.lower()
        if hostname in j:
            # count = j.count("geeks")
            count = count + 1
        if num == 0:
            # print("yes zero counted")
            ld = (enchant.utils.levenshtein(j, hostname))
        num = num + 1
    arr = [ld, count]
    return arr


def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


# Main Function() starts

def Main(url):
    val = url
    selfwp = val
    print(selfwp)
    # Function Call
    R_01 = URLLength(selfwp)
    R_09 = DigitAlphabetRatio(selfwp)
    R_10 = SpecialcharAlphabetRatio(selfwp)
    R_11 = UppercaseLowercaseRatio(selfwp)
    R_12 = DomainURLRatio(selfwp)
    R_13 = NumericCharCount(selfwp)
    R_14 = EnglishLetterCount(selfwp)
    R_15 = SpecialCharCount(selfwp)
    R_16 = DotCount(selfwp)
    R_17 = SemiColCount(selfwp)
    R_18 = UnderscoreCount(selfwp)
    R_19 = QuesMarkCount(selfwp)
    R_20 = HashCharCount(selfwp)
    R_21 = EqualCount(selfwp)
    R_22 = PercentCharCount(selfwp)
    R_23 = AmpersandCount(selfwp)
    R_24 = DashCharCount(selfwp)
    R_25 = DelimiterCount(selfwp)
    R_26 = AtCharCount(selfwp)
    R_27 = TildeCharCount(selfwp)
    R_28 = DoubleSlashCount(selfwp)
    R_51 = Entropy(selfwp)
    R_37 = HostNameLength(selfwp)
    R_38 = PathLength(selfwp)
    R_39 = QueryLength(selfwp)
    R_36 = HttpsInHostName(selfwp)
    R_29 = IsHashed(selfwp)
    R_32 = HttpsInUrl(selfwp)
    R_31 = DistDigitAlphabet(selfwp)
    R_41 = IsDomainEnglishWord(selfwp)
    R_43 = IsDomainPronounceable(selfwp)
    R_44 = IsDomainRandom(selfwp)
    R_45 = Unigram(selfwp)
    R_46 = Bigram(selfwp)
    R_47 = Trigram(selfwp)
    R_40 = DistWordBased(selfwp)
    R_33 = FileExtension(selfwp)
    R_04 = URLWithoutwww(val)
    R_05 = FTPUsed(selfwp)
    R_06 = JSUsed(selfwp)
    R_07 = FilesInURL(selfwp)
    R_08 = CSSUsed(selfwp)
    # add record to pandas data frame for saving in future
    X = {
        'URL_Length': R_01,
        'Is_www_present': R_04,
        'FTP_used': R_05,
        'js_used': R_06,
        'Files_in_URL': R_07,
        'css_used': R_08,
        'Digit_to_alphabet_ratio': R_09,
        'Special_Char_to_Alphabet_Ratio': R_10,
        'Uppercase_to_LowercaseRatio': R_11,
        'Domain_to_URL_Ratio': R_12,
        'Numeric_Character': R_13,
        'English_Letters': R_14,
        'Special_Characters': R_15,
        'Dots': R_16,
        'Semicolon': R_17,
        'Underscore': R_18,
        'Question_Mark': R_19,
        'Hash_Character': R_20,
        'Equals': R_21,
        'Percentage_Character': R_22,
        'Ampersand': R_23,
        'Dash': R_24,
        'Delimiters': R_25,
        'At_Character': R_26,
        'Tilde': R_27,
        'Double_Slash': R_28,
        'Is_Hashed': R_29,
        'Digit_to_alphabet_distance': R_31,
        'Https_in_URL': R_32,
        'File_Extention': R_33,
        'https_in_hostname': R_36,
        'Host_name_length': R_37,
        'Path_length': R_38,
        'Query_length': R_39,
        'Word_based_distribution': R_40,
        'Is_English_word': R_41,
        'Is_Pronounceable': R_43,
        'Is_random': R_44,
        'Unigram': R_45,
        'Bigram': R_46,
        'Trigram': R_47,
        # 'Levenshtein_Distance': R_50,
        'Entropy': R_51
    }
    return X
# End of the Program
