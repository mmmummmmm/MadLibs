# MadLibs
A game written in Python as part of the TumoLabs program.

Welcome to the **MadLibs**! This Python program allows you to create fun and whimsical stories by filling in the blanks in predefined templates. Whether you're reminiscing about a hospital visit, planning a camping trip, or writing a letter from an enchanted castle, this program will help you craft a unique tale based on your input.

## How It Works

1. **Select a Story Template**:
   - When you run the program, you'll be presented with a welcome message and instructions.
   - You'll have the option to choose from a list of story templates or let the program randomly select one for you.
   - The available templates include:
     1. A hospital visit
     2. A camping trip
     3. A letter to a friend

2. **Provide Your Inputs**:
   - Once a template is selected, the program will extract placeholders from the template, such as `(a number)`, `(a noun)`, or `(a verb)`.
   - You'll be prompted to provide words or phrases to fill in these placeholders.
   - The program includes validation for numerical inputs, ensuring you provide a valid number when required.

3. **Generate Your Story**:
   - After you've provided all the necessary inputs, the program will insert them into the selected template.
   - The final story will be displayed, featuring your personalized details.

## Features

- **Random Template Selection**: If you can't decide which story to create, let the program choose a random template for you!
- **Input Validation**: The program ensures that numerical inputs are correctly provided, enhancing the user experience.


## Logic of the Program
- The idea is to automate the code by extracting words in paranthesis and going through the list of keywords to obtaining input from the user and using the same list to generate the final story.
- Inspritions:
  1. https://stackoverflow.com/questions/58111954/python-extract-substring-from-between-parenthesis
  -(Replacing ')' with '(' simplifies the process of extracting placeholders from the template.)
  2. #https://stackoverflow.com/questions/1442782/how-to-split-an-iterable-into-two-lists-with-alternating-elements
  -(To split the list into alternating keywords.)

  


## Example

Here's an example of how the program works:

1. **Choose a Template**:
   - Suppose you select "A camping trip."

2. **Provide Inputs**:
   - You might be asked to provide a name, an animal, an adjective, etc.

3. **Generated Story**:
   - The program will generate a story like:
     ```
     This weekend I am going camping with Alice. I packed my lantern, sleeping bag, and a book. I am so excited to sleep in a tent. I am nervous we might see a bear; I hear they’re kind of dangerous...
     ```

## How to Run

1. Ensure you have Python installed on your system.
2. Copy the code from this repository and save it as `story_generator.py`.
3. Run the script using your terminal or command prompt:

