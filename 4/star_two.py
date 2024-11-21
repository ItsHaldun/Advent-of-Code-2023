filename = "4/input.txt"


def main():
  match_counts = []
  
  # Construct a list of appearing and winning numbers
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
      
      match_counts.append(len(matches)) 
      
  # Initial counts of 1
  card_counts = [1] * len(match_counts)
  
  # Go throught the list and cound the copies
  for i in range(len(match_counts)):
    # Either up until how many matches the card has or the end of the card list
    # Prevents out of bound errors
    upper_lim = min(i+match_counts[i]+1, len(match_counts))
    
    # Calculate the copies generated
    for j in range(i+1, upper_lim):
      card_counts[j] += card_counts[i]

  print(f"Final Sum: {sum(card_counts)}")


if __name__ == "__main__":
  main()