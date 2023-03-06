from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/workouts')
def get_workouts():
    off = ['Off Day']
    metabolic = ['Jump Rope', 'Burpees','Jumping Jacks','Mountain Climbers']
    gymnastics = ['air squat','pull up','push up', 'dip', 'sit up', 'lunge']
    weightlifting = ['deadlift','shoulder press','squat','kettlbell swing','thruster','benchpress']
    wod_type = ['Rounds For Time','As Many Rounds As Possible']

    # Generate the workout data
    meta1 = random.choice(metabolic)
    gym1 = random.choice(gymnastics)
    lift1 = random.choice(weightlifting)
    workout1 = random.choice(wod_type)

    meta2 = random.choice(metabolic)
    gym2 = random.choice(gymnastics)
    lift2 = random.choice(weightlifting)
    workout2 = random.choice(wod_type)

    # Return the workout data as a JSON object
    return jsonify({
        'workout1': {
            'meta': meta1,
            'gym': gym1,
            'lift': lift1,
            'type': workout1
        },
        'workout2': {
            'meta': meta2,
            'gym': gym2,
            'lift': lift2,
            'type': workout2
        }
    })

if __name__ == '__main__':
    app.run()
