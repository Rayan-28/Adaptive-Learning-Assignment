class AdaptiveEngine:
    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]

    def determine_next_level(self, current_level, recent_history):
        # using at least 3 questions to detect if have to level up and 2 questions to detect if sruggling
        if len(recent_history) < 2:
            return current_level


        #logic for leveling downwhen we determine the user is struggling if 2 ques wrong then level down
        last_two = recent_history[-2:]
        correct_count_last_2 = sum(1 for r in last_two if r['correct'])
        
        if correct_count_last_2 == 0:  # 0 out of 2 correct
            return self._change_level(current_level, step=-1)

        #logic for levelin up when we determine the user is doing good but we need atleast 3 questions to determine
    
        if len(recent_history) < 3:
            return current_level
            
        last_three = recent_history[-3:]
        all_correct = all(r['correct'] for r in last_three)
        
        # calculates average speed of last 3 attempts
        avg_time = sum(r['time_taken'] for r in last_three) / 3
        
        if all_correct and avg_time < 8.0: #if the avg time is 8 or less then we can determine to level up
            return self._change_level(current_level, step=1)

    
        return current_level # if average time is not achieved then we have to keep it on current level

    def _change_level(self, current_level, step): #calculates where to step next without fear for going out of bounds
        try:
            current_index = self.levels.index(current_level)
            new_index = current_index + step

            if 0 <= new_index < len(self.levels):
                return self.levels[new_index]
            else:
                return current_level 
        except ValueError:
            return "Easy" 