import re

filename = "1/input.txt"
separator = re.compile(r"(\d)")


def main():
  calibration = 0
  
  with open(filename) as file:
    for i, line in enumerate(file):
      # Get a list of digits, including written out ones
      digit_list = separator.findall(line)
      
      # Edge case for no digits
      if len(digit_list) == 0:
        continue
      
      # Get the digits
      digit_one = digit_list[0]
      digit_two = digit_list[-1]
      
      # Calculate the additions
      accumulator = 10 * int(digit_one) + int(digit_two)
      calibration += accumulator
      print(f"{i}: Adding {accumulator}  |  Total: {calibration}")
      
  print(f"Final Sum: {calibration}")

if __name__ == "__main__":
  main()