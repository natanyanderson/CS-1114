"""
Author: [Natanya Anderson]
Assignment / Part: HW7 - Q2, Q3 (depending on the file name)
Date due: 2022-11-11, 12:00pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def is_haiku(input_string):
    lines = input_string.split("/")
    if len(lines)!=3:
        return "WARNING: The first line is not 5 syllables long.\nFalse"
    if len(lines[0].split(",")) != 5:
        return "WARNING: Th first line is not 5 syllables long.\nFalse"
    if len(lines[1].split(",")) != 7:
        return "WARNING: The second line is not 7 syllables long.\nFalse"
    if len(lines[2].split(",")) != 5:
        return "WARNING: The third line is not 5 syllables long.\nFalse"
    return True

print(is_haiku("clouds ,mur,mur ,dark,ly /it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon "))

def haiku_string_parser(input_string):
    return_answer = ""
    if is_haiku(input_string) == True:
        lines = input_string.split("/")
        for line in lines:
            line_split = line.split(",")
            join_line = "".join(line_split)
            return_answer += join_line + "\n"
    return return_answer.strip("\n")


def main():
 haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
 formatted_haiku = haiku_string_parser(haiku_string)
 print(formatted_haiku)
main()