filename = "3/input.txt"


# Read the first number from a line, given index
def read_number(line, index):
  number_buffer = ""
  i = index
  
  # Go to the start of the number
  while line[i-1].isdigit():
    i -= 1
  
  # Read until the end
  while line[i].isdigit():
    number_buffer += line[i]
    i += 1
  
  return int(number_buffer)


# Does a 3x3 convolution to check for gear numbers
def convolution(x, y, schematic):
  
  numbers = []
  
  for i in [-1, 0, 1]:
    number_start = False
    
    for j in [-1, 0, 1]:
      # Parse numbers
      if schematic[x+i][y+j].isdigit():
        # Rising edge detection
        if not number_start:
          number_start = True
          
          # Check for backward and forward number:
          number = read_number(schematic[x+i], y+j)
          numbers.append(number)
      
      else:
        # Falling edge detection
        if number_start:
          number_start = False

  # Only a gear if it has two numbers around
  if len(numbers) == 2:
    return numbers[0] * numbers[1]
  else:
    return 0


# Construct a padded 2d list, padding allows trivial edge calculations
def construct_matrix_from_input():
  lines = []
  line_length = None
  
  with open(filename) as file:
    
    for line in file:
      # Count the number of lines
      
      # Padding by one for convolution
      # Also removes line ending
      line = "." + line[0:-1] + "."
      
      if line_length is None:
        # First line padding
        line_length = len(line)
        lines.append("."*line_length)
      
      # Add line to the matrix
      lines.append(line)
    
    # Last line padding
    lines.append("."*line_length)
  
  return lines


def main():
  schematic = construct_matrix_from_input()
  
  # Height and width of schematic plus padding
  h = len(schematic)
  w = len(schematic[0])
  
  # Visit every character of the schematic
  gear_ratios = []
  
  # Doesn't visit the padded section
  for i in range(1, h-1):
    for j in range(1, w-1):
            
      if schematic[i][j] == "*":
        gear_ratio = convolution(i, j, schematic)
        
        if gear_ratio > 0:
          gear_ratios.append(gear_ratio)
  
  
  print(f"Final Sum: {sum(gear_ratios)}")


if __name__ == "__main__":
  main()