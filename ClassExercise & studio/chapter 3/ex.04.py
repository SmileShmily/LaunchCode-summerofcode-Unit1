'''Football Scores Suppose you’ve written the program below.
The given program asks the user to input the number of touchdowns and field goals scored by a (American) football team,
 and prints out the team’s score. (We assume that for each touchdown, the team always makes the extra point.)

The European Union has decided that they want to start an American football league,
and they want to use your killer program to calculate scores,
 but they like things that are multiples of 10 (e.g. the Metric System),
  and have decided that touchdowns will be worth 10 points and field goals are worth 5 points.
   Modify the program below to work on both continents, and beyond.
   It should ask the user how many points a touchdown is worth and how many points a field goal is worth.
   Then it should ask for the number of each touchdowns / field goals scored, and print the team’s total score.
'''

num_touchdowns = input("How many touchdowns were scored? ")
num_field_goals = input("How many field goals were scored? ")

total_score = 7 * int(num_touchdowns) + 3 * int(num_field_goals)

print("The team has", total_score, "points")
