import random
from flask import Flask, render_template_string

app = Flask(__name__)

# Define the lists
rigs = ["Stun", "Blind", "Heal", "X-Ray", "Barricade"]
tools = ["Slippers", "Cacophony", "Noise Reduction", "Battery Charger", "Lock Breaker", "Recycle", "Keymaster", "Backpack"]
skills = ["Hide and Breathe", "Hide and Heal", "Hide and Restore", "Quick Escape", "Invisible", "Door Trap Breaker", "Smash", "Strong Arm"]
medicines = ["Double Doses", "Antitoxin", "Surplus", "Last Chance", "Incognito", "Good Job", "Boosted", "Self Revive"]

@app.route('/')
def index():
    return render_template_string('''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Randomizer</title>
      </head>
      <body>
        <div style="text-align:center; margin-top:50px;">
          <h1>New Outlast Loadout</h1>
          <button onclick="fetchLoadout()">New Loadout</button>
          <p id="loadout"></p>
        </div>
        <script>
          function fetchLoadout() {
            fetch('/randomize')
              .then(response => response.json())
              .then(data => {
                document.getElementById('loadout').innerText =
                  `Rig: ${data.rig}\n` +
                  `Tool: ${data.tool}\n` +
                  `Skill: ${data.skill}\n` +
                  `Medicine: ${data.medicine}`;
              });
          }
        </script>
      </body>
    </html>
    ''')

@app.route('/randomize')
def randomize():
    selected_rig = random.choice(rigs)
    selected_tool = random.choice(tools)
    selected_skill = random.choice(skills)
    selected_medicine = random.choice(medicines)
    
    return {
        "rig": selected_rig,
        "tool": selected_tool,
        "skill": selected_skill,
        "medicine": selected_medicine
    }

if __name__ == '__main__':
    app.run(debug=True)
