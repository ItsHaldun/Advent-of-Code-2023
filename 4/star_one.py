filename = "4/input.txt"


def main():
  points = 0
  
  with open(filename) as file:
    for card in file:
      # Remove game id section
      _, card = card.split(": ")
      
      # Remove the end character
      card = card[:-1]
      
      # Divide into lists
      appearing_numbers, winning_numbers = card.split(" | ")
      
      appearing_numbers = appearing_numbers.split()
      winning_numbers = winning_numbers.split()
      
      # compare lists by set interaction
      matches = list(set(appearing_numbers) & set(winning_numbers))
      
      if len(matches) > 0:
        points += 2 ** (len(matches) - 1)
        
  print(f"Final Sum: {points}")
      
      


if __name__ == "__main__":
  main()