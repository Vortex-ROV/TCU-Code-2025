def adjustPwm(pwm, gain):
    adjustedPwm = 1500
    
    if pwm == 1500:
        return adjustedPwm
    
    if pwm > 1500:
        adjustedPwm = min(pwm, 1500 + int(400*gain/100))
    elif pwm < 1500:
        adjustedPwm = max(pwm, 1500 - int(400*gain/100))

    return adjustedPwm
