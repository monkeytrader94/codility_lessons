def solution(A):

    ave = (A[0] + A[1]) / 2
    index = 0

    for i in range(len(A) - 1):
        if i == len(A) - 2:
            trial_ave = (A[i] + A[i+1]) / 2            
            if trial_ave < ave or ave == None:
                ave = trial_ave
                index = i
        else:
            first_trial_ave = (A[i] + A[i+1]) / 2
            second_trial_ave = (A[i] + A[i+1] + A[i+2]) / 3
            if first_trial_ave <= second_trial_ave:
                trial_ave = first_trial_ave
            else:
                trial_ave = second_trial_ave
            if trial_ave < ave:
                ave = trial_ave
                index = i

    return index