filename = "2/input.txt"

bag_contents = {
  "red": 12,
  "green": 13,
  "blue": 14
}

def main():
  sum = 0
  
  with open(filename) as file:
    for id, game in enumerate(file):
      is_invalid = False
      
      # Remove game id section
      _, game = game.split(": ")
      
      # Remove the end character
      game = game[:-1]
      
      # Divide into lists
      game = game.split("; ")
      
      # Check each set of the game
      for draw_set in game:
        # Divide draw_set to each color
        color_split_draw = draw_set.split(", ")
        
        # Check each color occurrence
        for color_cube in color_split_draw:
          # Get the number of cubes and the color
          number, color = color_cube.split()
          
          if int(number) > bag_contents[color]:
            is_invalid = True
      
      if not is_invalid:
        # id is zero indexed in my loop
        sum += id+1
  
  print(f"Final Sum: {sum}")


if __name__ == "__main__":
  main()