import random 

reward_probs = { 
        'Fiio M17': 0.0001,
        'Asus Flashstor 6 NAS': 0.0001,
        'Nothing': 0.5,
        '1 hour of video games': 0.05, 
        '1 hour of phone time': 0.1, 
        'Gaming with friends on weekend': 0.05, 
        'Get takeout': 0.05, 
        '30 mins of anything': 0.05, 
        'Model building on weekend': 0.05, 
        'Trip to Newbury Comics': 0.03, 
        'Trip to Games Workshop': 0.03, 
        'Read an news article': 0.1, 
        'Two spins': 0.04999, 
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


