"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

COLOUR_TO_CODE = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AQUAMARINE": "#7fffd4",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BISQUE": "#ffe4c4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#ffebcd",
    "BLUE": "#0000ff"
}

hexadecimal_code = input("Enter colour: ").upper()
while hexadecimal_code != "":
    try:
        print(hexadecimal_code, "is", COLOUR_TO_CODE[hexadecimal_code])
    except KeyError:
        print("Invalid colour")
    hexadecimal_code = input("Enter colour: ").upper()
