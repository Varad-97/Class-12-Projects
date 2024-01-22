# Input player names
player1_name = input("Enter your name: ")
player2_name = input("Enter Her/His name: ")
# Combine the names and convert to lowercase for case-insensitive comparison
combined_names = (player1_name + player2_name).lower()
# Count the total number of unique characters in the combined names
unique_characters = len(set(combined_names))
# Determine the relationship type using the "FLAMES" method
relationship_type = "FLAMES"[(unique_characters - 1) % len("FLAMES")]
# Display the result based on the relationship type
if relationship_type == "F":
 print("F - Friends: In the vast algorithm of life, friendship is the constant that provides stability.")
elif relationship_type == "L":
 print("L - Lovers: Love is the quantum entanglement of two souls, intertwined across spacetime.")
elif relationship_type == "A":
 print("A - Affectionate: Affection, like a well-designed algorithm, operates seamlessly, bringing joy to the heart.")
elif relationship_type == "M":
 print("M - Marriage: Marriage is the optimal solution to life's equation, where two variables find equilibrium.")
elif relationship_type == "E":
 print("E - Enemies: Enemies, much like software bugs, require understanding and resolution, not deletion.")
else:
 print("S - Siblings: Siblings: the earliest version of peer-to-peer networking, filled with shared memories and occasional conflicts.")