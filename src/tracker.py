import time

class PerformanceTracker:
    def __init__(self):    #stores dictionaries of every attempt
        self.history = []

    def log_attempt(self, difficulty, time_taken, is_correct): #logs performance on a single puzzle.
        record = {
            "difficulty": difficulty,
            "time_taken": time_taken,
            "correct": is_correct,
            "timestamp": time.time()
        }
        self.history.append(record)

    def get_recent_performance(self, n=3): #Returns the last 'n' attempts. Used by the engine to make decisions.
        
        return self.history[-n:]

    def get_summary(self): #Calculates total accuracy and average time.
    
        if not self.history:
            return "Empty"
            
        total_q = len(self.history)
        correct_count = sum(1 for p in self.history if p['correct'])
        avg_time = sum(p['time_taken'] for p in self.history) / total_q
        accuracy = (correct_count / total_q) * 100
        
        return {
            "total_questions": total_q,
            "accuracy": round(accuracy, 2),
            "average_time_sec": round(avg_time, 2)
        }