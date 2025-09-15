#Hard
#String Dynamic Programming Recursion

#FAILED

"""
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).



    Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    Example 2:

    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    Example 3:

    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".


    Constraints:

    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""

from functools import lru_cache

#ChatGpt Solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dp(index_s: int, index_p: int) -> bool:
            # caso base: se ho finito il pattern,
            # devo aver finito anche la stringa
            if index_p == len(p):
                return index_s == len(s)

            # controlla se il carattere corrente di s e p combaciano
            has_current_match = (
                    index_s < len(s)
                    and (p[index_p] == s[index_s] or p[index_p] == ".")
            )

            # se il prossimo simbolo in p è '*'
            if index_p + 1 < len(p) and p[index_p + 1] == "*":
                # due opzioni:
                # 1) salto il blocco x*  → dp(index_s, index_p+2)
                # 2) consumo un carattere da s se matcha → dp(index_s+1, index_p)
                return dp(index_s, index_p + 2) or (
                        has_current_match and dp(index_s + 1, index_p)
                )
            else:
                # se non c’è '*', devo avanzare entrambi
                return has_current_match and dp(index_s + 1, index_p + 1)

        return dp(0, 0)


"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def charDomain(char):
            return 'a' <= char <= 'z' or char == '.'

        patterns = list(p)
        string = list(s)

        lp = len(patterns) 
        ip = 0
        lw = len(string)
        iw = 0

        while ip < lp and iw < lw:

            zeroOrMore = False
            isLast = False

            if charDomain(patterns[ip]): # se il corrente è un carattere
                if ip+1 < lp: 

                    if charDomain(patterns[ip+1]): #se il successivo è un carattere
                        zeroOrMore = False
                    elif patterns[ip+1] == '*': #se il successivo è un *
                        zeroOrMore = True
                        #ip += 1

                else: #last character in pattern
                    #if charDomain(patterns[ip]):
                    #zeroOrMore = False
                    isLast = True
                    if patterns[ip] == '*':
                        zeroOrMore = True

            elif patterns[ip] == '*':
                zeroOrMore = True

            if zeroOrMore: # se asterisco
                if string[iw] == patterns[ip] or patterns[ip] == '.':
                    ip -= 1
                    iw += 1
            else: # se singola ripetizione
                if string[iw] == patterns[ip] or patterns[ip] == '.':
                    iw += 1 
                else:
                    return False

            ip += 1

        if zeroOrMore:
            ip += 2


        if iw >= lw and ip >= lp:
            return True
        elif iw >= lw and ip < lp:
            n_star = 0
            for i in range(ip, lp):
                n_star += 1 * int(patterns[i] == '*')

            if ((lp - ip) // 2) + 1*int((lp - ip) % 2 != 0) >= n_star:
                return False
            else:
                return True 
        elif iw < lw and ip >= lp:
            return False
        elif iw < lw and ip < lp:
            return False

"""

"""

    class Pattern:
        def __init__(self, character, repetition=None):
            self.char = character
            self.repetition = 1 if repetition == None else repetition

        def satisfy(self, word):
            pass

        @staticmethod
        def charDomain(char):
            return 'a' <= char <= 'z' or char == '.'


    class Solution:
        def isMatch(self, s: str, p: str) -> bool:

            prev_is_letter = False

            patterns = list()

            char = p[0]

            for pattern in p:
                if prev_is_letter is True and not(Pattern.charDomain(pattern)):
                    patterns.append(
                        Pattern(
                            character = char,
                            repetition = pattern
                        )
                    )
                    prev_is_letter = False
                elif prev_is_letter is True and Pattern.charDomain(pattern):
                    patterns.append(
                        Pattern(
                            character = char,
                            #repetition = pattern
                        )
                    )
                    char = pattern
                    prev_is_letter = True
                elif prev_is_letter is False and Pattern.charDomain(pattern):
                    char = pattern
                    prev_is_letter = True
                elif not(Pattern.charDomain(char)) and pattern != '*':
                    return False

            if prev_is_letter is True:
                patterns.append(
                    Pattern(
                        character = char
                    )
                )

            wl = len(s)
            iw=wl-1
            pl = len(patterns)
            ip=pl-1

            lastUpdatePattern = False
            string = list(s)

            while(iw>=0):
                pattern = patterns[ip]
                char2check, repetition2check = pattern.char, pattern.repetition

                currChar = string[iw]
                isCharMatch = currChar == char2check or char2check == '.'

                #end = iw+repetition2check if repetition2Check != None else wl-1

                if repetition2check == '*' and isCharMatch:
                    iw -= 1
                    lastUpdatePattern = False
                elif repetition2check == '*' and not(isCharMatch):
                    ip -= 1
                    lastUpdatePattern = True
                elif repetition2check != '*' and isCharMatch:
                    iw -= 1
                    ip -= 1
                    lastUpdatePattern = True
                else:
                    return False

                if (ip < 0 and iw >= 0):
                    return False

            cnt = 0

            for i in range(ip-1 + 1*(int(lastUpdatePattern)), -1, -1):
                if patterns[i].repetition == '*':
                    continue
                else:
                    cnt += patterns[i].repetition

            for i in range(ip-1 + 1*(int(lastUpdatePattern)), -1, -1):
                if patterns[i].repetition == 1 and patterns[i].char != string[0]:
                    return False
                elif patterns[i].repetition == 1 and patterns[i].char == string[0]:
                    return True
                elif patterns[i].repetition == '*':
                    continue


            return True

"""
