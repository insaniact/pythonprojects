def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

adjective1 = get_input("adjective")
noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} all day long.

One day, the {noun1} walked into the room and caught the {noun2} trying to {verb1}.

{noun2}: "What are you doing?"
{noun1}: "I'm just {verb1}ing. What's the big deal?"
{noun2}: "Well, it's not everyday that I see a {noun2} {verb1}ing in the middle of the day."
{noun1}: "I guess you're right. I'll stop {verb1}ing now."
{verb2}: "Good idea. Let's go {verb2}ing instead."
{noun1}: "Sounds like a plan!"

And so, the two friends went off {verb2}ing together. 

"""

print(story)