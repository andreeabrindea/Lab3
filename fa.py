import Element
import re


def read_file():
    f = open("FA.in", "r")
    q = f.readline().replace("\n", "").split(" ")
    E = f.readline().replace("\n", "").split(" ")
    d = f.readline().replace("\n", "").split(";")
    q0 = f.readline().replace("\n", "").split(" ")
    F = f.readline().replace("\n", "").split(" ")
    dict = {}
    for elem in d:
        if "\n" in elem:
            elem = elem.replace("\n", "")
        if "," in elem:
            elem = elem.replace(",", " ")
        if "->" in elem:
            elem = elem.replace("->", " ")
        elem = elem.strip()
        list = elem.split(" ")
        first = list[0]
        second = list[1]
        third = list[2]
        if (first, second) in dict.keys():
            dict[(first, second)].append(third)
        else:
            dict[(first, second)] = [third]

    return Element.Element(q, E, dict, q0, F)


def check_errors(m: Element.Element):
    for elem in m.Q:
        matches = re.findall(r"[a-zA-Z][a-zA-Z0-9]*", str(elem))
        if str(matches[0]) != str(elem):
            raise ValueError("Err: States: elem " + str(elem) + " not in correct format")

    for elem in m.E:
        matches = re.findall(r"[a-zA-Z]|[0-9]|[!@#$%^&*+?=<>/]", str(elem))
        if str(matches[0]) != str(elem):
            raise ValueError("Err: Alphabet: elem " + str(elem) + " not in correct format")

    for elem in m.d.keys():
        matches = re.findall(r"[a-zA-Z][a-zA-Z0-9]*", str(elem[0]))
        if str(matches[0]) != str(elem[0]):
            raise ValueError("Err: Transitions: elem " + str(elem) + " not in correct format")
        matches = re.findall(r"[a-zA-Z]|[0-9]|[!@#$%^&*+?=<>/]", str(elem[1]))
        if str(matches[0]) != str(elem[1]):
            raise ValueError("Err: Transitions: elem " + str(elem) + " not in correct format")

    for elemList in m.d.values():
        for elem in elemList:
            matches = re.findall(r"[a-zA-Z][a-zA-Z0-9]*", str(elem))
            if str(matches[0]) != str(elem):
                raise ValueError("Err: Transitions: elem " + str(elem) + " not in correct format")

    for elem in m.q0:
        matches = re.findall(r"[a-zA-Z][a-zA-Z0-9]*", str(elem))
        if str(matches[0]) != str(elem):
            raise ValueError("Err: Initial State: elem " + str(elem) + " not in correct format")

    for elem in m.F:
        matches = re.findall(r"[a-zA-Z][a-zA-Z0-9]*", str(elem))
        if str(matches[0]) != str(elem):
            raise ValueError("Err: Final State: elem " + str(elem) + " not in correct format")


if __name__ == '__main__':
    try:
        objAutomata = read_file()
    except:
        raise IOError("Err: error parsing input file, check for delimiters ; , ->")

    check_errors(objAutomata)
    print(objAutomata)
