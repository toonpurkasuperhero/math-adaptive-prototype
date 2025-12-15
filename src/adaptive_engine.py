class AdaptiveEngine:
    def __init__(self, p_l0=0.3, p_t=0.2, p_s=0.1, p_g=0.2):
        self.p_l = p_l0
        self.p_t = p_t
        self.p_s = p_s
        self.p_g = p_g

    def update_mastery(self, correct):
        p_l = self.p_l

        if correct:
            num = p_l * (1 - self.p_s)
            den = num + (1 - p_l) * self.p_g
        else:
            num = p_l * self.p_s
            den = num + (1 - p_l) * (1 - self.p_g)

        p_l_given_obs = num / den
        self.p_l = p_l_given_obs + (1 - p_l_given_obs) * self.p_t

        return self.p_l

    def choose_difficulty(self, history):
        mastery = self.p_l

        # rule-based smoothing
        if len(history) >= 2:
            if history[-1] and history[-2]:
                mastery += 0.05
            if not history[-1] and not history[-2]:
                mastery -= 0.05

        if mastery < 0.4:
            return "Easy"
        elif mastery < 0.7:
            return "Medium"
        else:
            return "Hard"
