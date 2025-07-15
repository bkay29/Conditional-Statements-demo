adj1 = input("Enter an adjective to describe the day (e.g., sunny, gloomy): ")
adj2 = input("Enter an adjective to describe the monkey (e.g., silly, wiered): ")
adj3 = input("Enter an adjective to describe the snake (e.g., majestic, lazy): ")
adj4 = input("Enter an adjective to describe the whole experience: ")
noun = input("Enter a noun (e.g., Karura forest): ")

if adj1.lower() == "boring":
    extra_line = "Honestly, I almost fell asleep!"
elif adj1.lower() == "scary":
    extra_line = "I was nervours the whole time!"
else:
    extra_line = "I couldn't stop smiling the entire trip!"

story = ( 
    f"On a beautiful {adj1} day, I went to {noun}. "
    f"I saw a funny {adj2} monkey swinging from the trees. "
    f"Then, I spotted {adj3} a snake lounging in the sun. "
    f"What a wild and {adj4} experience! {extra_line}"
)

print("\n Here's your mad libs story:\n")
print(story)