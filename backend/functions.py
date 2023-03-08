import random

off = ['Off Day']
metabolic = ['Jump Rope', 'Burpees','Jumping Jacks','Mountain Climbers']
gymnastics = ['air squat','pull up','push up', 'dip', 'sit up', 'lunge']
weightlifting = ['deadlift','shoulder press','squat','kettlbell swing','thruster','benchpress']
wod_type = ['Rounds For Time','As Many Rounds As Possible']

def generate_workout(fitness_level, workout_length):
    if fitness_level == 'beginner':
        min_reps = 1
        max_reps = 5
    elif fitness_level == 'intermediate':
        min_reps = 1
        max_reps = 10
    else:
        min_reps = 1
        max_reps = 15

    workout = []
    workout.append(random.choice(metabolic) + ' ' + str(random.randint(min_reps, max_reps)) + ' reps')
    workout.append(random.choice(gymnastics) + ' ' + str(random.randint(min_reps, max_reps)) + ' reps')
    workout.append(random.choice(weightlifting) + ' ' + str(random.randint(min_reps, max_reps)) + ' reps')
    workout_type = random.choice(wod_type)

    return {'workout': workout, 'workout_type': workout_type}