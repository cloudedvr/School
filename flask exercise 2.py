from flask import Flask, request, render_template_string

# --- Madlibs Story Code ---
class Story:
    """Madlibs story.

    To make a story, pass a list of prompts, and the text of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing of {prompt: answer}:

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""
        text = self.template
        for key, val in answers.items():
            text = text.replace("{" + key + "}", val)
        return text

# Example story
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# --- Flask App ---
app = Flask(__name__)

# Homepage: dynamically generate a form using story.prompts
@app.route("/")
def index():
    form_template = '''
    <!doctype html>
    <html>
    <head>
      <title>Madlibs</title>
    </head>
    <body>
      <h1>Fill in the blanks</h1>
      <form action="/story" method="get">
      {% for prompt in prompts %}
        <label for="{{ prompt }}">{{ prompt|capitalize }}:</label>
        <input type="text" name="{{ prompt }}" id="{{ prompt }}">
        <br>
      {% endfor %}
      <button type="submit">Generate Story</button>
      </form>
    </body>
    </html>
    '''
    return render_template_string(form_template, prompts=story.prompts)

# Story route: generate and display the final story based on answers
@app.route("/story")
def show_story():
    # Get the answers for each prompt from the query parameters.
    answers = {prompt: request.args.get(prompt, "") for prompt in story.prompts}
    final_story = story.generate(answers)
    
    story_template = '''
    <!doctype html>
    <html>
    <head>
      <title>Your Madlib Story</title>
    </head>
    <body>
      <h1>Your Madlib Story</h1>
      <p>{{ final_story }}</p>
      <a href="/">Try Again</a>
    </body>
    </html>
    '''
    return render_template_string(story_template, final_story=final_story)

if __name__ == '__main__':
    app.run(debug=True)
