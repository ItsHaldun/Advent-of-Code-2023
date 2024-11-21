filename = "3/input.txt"


# Does a 3x3 convolution to check for characters
def convolution(x, y, schematic):
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      # Is a part number if its not a digit and "."
      if not schematic[x+i][y+j].isdigit() and schematic[x+i][y+j] != ".":
        return True
  
  return False


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
  part_numbers = []
  
  for i in range(1, h-1):
    number_string = ""
    is_included = False
    
    for j in range(1, w-1):
            
      if schematic[i][j].isdigit():
        number_string += schematic[i][j]
        
        # Check for symbols
        # Only check if didn't found any up until now
        if is_included == False:
          is_included = convolution(i, j, schematic)
        
        # Check if this is the end of the number
        if not schematic[i][j+1].isdigit():
          if is_included:
            part_numbers.append(int(number_string))
          
          # Restart the number buffer
          is_included = False
          number_string = ""

  print(f"Final Sum: {sum(part_numbers)}")


if __name__ == "__main__":
  main()