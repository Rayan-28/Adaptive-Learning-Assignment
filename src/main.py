import time
from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def main():
    print("Welcome to Math Adventures!")
    print("Type 'exit' to finish the session.\n")
    
    generator = PuzzleGenerator()
    tracker = PerformanceTracker()
    engine = AdaptiveEngine()
    
    current_difficulty = "Easy" #tracks the current difficulty level and is kept updating
    
    while True:
        puzzle = generator.generate(current_difficulty) #generates puzzle
        print(f"[{current_difficulty}] Question: {puzzle['question']}")
        
        start_time=time.time()
        user_input=input("Answer: ") #captures input
        end_time=time.time() #measures time
        
        if user_input.lower()=='exit':
            break
        try:
            user_answer = int(user_input)
        except ValueError: #makes sure the input is a valid number
            print("Please enter a valid number.")
            continue
            
        time_taken = end_time - start_time
        
        is_correct = (user_answer == puzzle['answer']) #checks answer 
        if is_correct:
            print(f"Correct! ({time_taken:.2f}s)\n")
        else:
            print(f"Wrong. The answer was {puzzle['answer']}.\n")
            
        tracker.log_attempt(current_difficulty, time_taken, is_correct) # logs performance
        
        recent_history = tracker.get_recent_performance()
        new_difficulty = engine.determine_next_level(current_difficulty, recent_history) #determines difficulty 
        
        if new_difficulty != current_difficulty:
            print(f"*** Adapting Difficulty: {current_difficulty} -> {new_difficulty} ***\n")
            current_difficulty = new_difficulty

   
    print("SESSION SUMMARY")
    print("-"*30)
    
    stats = tracker.get_summary()
    
    if isinstance(stats, dict):
        print(f"Total Questions:       {stats['total_questions']}")
        print(f"Accuracy:              {stats['accuracy']}%")
        print(f"Average Speed:         {stats['average_time_sec']}s")
        print("-" * 30)
        # This satisfies the requirement to show "Next Recommended Level"
        print(f"Next Recommended Level: {current_difficulty}")
    else:
        print(stats) # Handles the "No questions answered" case

if __name__ == "__main__":
    main()