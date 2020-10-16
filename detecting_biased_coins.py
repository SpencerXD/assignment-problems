
coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']

import matplotlib.pyplot as plt

def detecting_biased_coins(input_list):
    prob_list = [0, 0, 0, 0]
    for string in input_list:
        count = 0
        for char in string:
            if char == 'H':
                count += 1
        prob_list[count] += 1
    for index in range(len(prob_list)):
        prob_list[index] = prob_list[index]/len(input_list)
    return prob_list


plt.style.use('bmh')
plt.plot([0, 1, 2, 3],detecting_biased_coins(coin_1))
plt.plot([0, 1, 2, 3],detecting_biased_coins(coin_2),linewidth=0.75)
plt.plot([0, 1, 2, 3],detecting_biased_coins(coin_3),linewidth=0.75)
plt.legend(['coin 1','coin 2','coin 3'])
plt.xlabel('Number of Heads')
plt.ylabel('Experimental Probability')
plt.title('Number of Heads vs experimental probability ')
plt.savefig('biased_coins.png')

#coin 1 is baised towards tails as shown on the graph
#coin 2 is fair because it has an equal number of 1 and 2 Heads
#coin 3 is biased towards heads because two heads is much higher than one head. 
