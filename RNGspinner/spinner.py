import random 

reward_probs = { 
        'Chord Mojo 2': 0.00001,
        'nothing': 0.5,
        '30 minutes of video games': 0.05, 
        '30  mins of phone time': 0.1, 
        'SS13 with friends on weekend': 0.05, 
        'eat takeout': 0.05, 
        '20 mins of anything': 0.05, 
        '20 mins of model building': 0.05, 
        'Trip to Newbury Comics': 0.05, 
        'Trip to Games Workshop': 0.05, 
        'read an news article': 0.1, 
        'two spins': 0.04999, 
}
def spin(): 
    return random.choices(list (reward_probs. keys ()), list (reward_probs. values () )) [0]
def main(): 

    spin_result = spin() 
    print('Your Random Reward is...')
    print(spin_result) 
    if (spin_result != 'nothing'): 
        with open('rewards.txt', 'a') as f: 
            f.write(spin_result +'\n') 
if __name__ == '__main__': main()


