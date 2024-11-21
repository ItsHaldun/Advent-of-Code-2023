import re

conversion_table = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

edge_cases = {
  "oneight": "18",
  "twone": "21",
  "threeight": "38",
  "fiveight": "58",
  "sevenine": "79",
  "eightwo": "82",
  "eighthree": "83",
  "nineight": "98"
}

separator = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|\d)")
filename = "1/input.txt"


def main():
  calibration = 0

  with open(filename) as file:
    for i, line in enumerate(file):
      accumulator = 0
      
      # Edge cases (Overlaps)
      for case in edge_cases.keys():
        line = re.sub(case, edge_cases[case], line)
      
      # Get a list of digits, including written out ones
      digit_list = separator.findall(line)
      
      # Edge case for no digits
      if len(digit_list) == 0:
        continue
      
      # Get the digits
      digit_one = digit_list[0]
      digit_two = digit_list[-1]
      
      # Convert them if they're written down versions
      if digit_one in conversion_table.keys():
        digit_one = conversion_table[digit_one]
        
      if digit_two in conversion_table.keys():
        digit_two = conversion_table[digit_two]
      
      # Calculate the additions
      accumulator = 10 * int(digit_one) + int(digit_two)
      calibration += accumulator
      print(f"{i}: Adding {accumulator}  |  Total: {calibration}")
      
  print(f"Final Sum: {calibration}")


if __name__ == "__main__":
  main()