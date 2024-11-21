filename = "2/input.txt"

minimum_bag = {
  "red": 0,
  "green": 0,
  "blue": 0
}

def main():
  sum = 0
  
  with open(filename) as file:
    for id, game in enumerate(file):
      # Reset bag contents for each game
      minimum_bag["red"] = 0
      minimum_bag["green"] = 0
      minimum_bag["blue"] = 0
      
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
        
        # Check each color occurrence, find the largest one
        for color_cube in color_split_draw:
          # Get the number of cubes and the color
          number, color = color_cube.split()
          
          # Save an occurrence if it is larger than previous largest
          if int(number) > minimum_bag[color]:
            minimum_bag[color] = int(number)
      
      
      # Calculate the power a game
      power = 1
      for color in ["red", "green", "blue"]:
        power *= minimum_bag[color]
      
      sum += power
  
  print(f"Final Sum: {sum}")


if __name__ == "__main__":
  main()