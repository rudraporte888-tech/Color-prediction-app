import random

class ColorTrendAnalyzer:
    def __init__(self):
        self.history = []

    def add_result(self, result):
        """Add a new result ('Red' or 'Green') to the history log"""
        self.history.append(result)

    def simulate_history(self, count=50):
        """Simulate past rounds for testing analysis logic"""
        outcomes = ['Red', 'Green']
        self.history = [random.choice(outcomes) for _ in range(count)]
        print(f"[Info] Generated {count} historical dummy entries.")

    def analyze_trends(self):
        if not self.history:
            print("No history available to analyze.")
            return

        red_count = self.history.count('Red')
        green_count = self.history.count('Green')
        total = len(self.history)

        print(f"\n--- Statistical Summary ---")
        print(f"Total Rounds Analyzed: {total}")
        print(f"Red Count: {red_count} ({(red_count/total)*100:.2f}%)")
        print(f"Green Count: {green_count} ({(green_count/total)*100:.2f}%)")

        # Streak Analysis
        last_three = self.history[-3:]
        print(f"Last 3 Recent Draws: {last_three}")

        # Educational insight based on probability
        if last_three.count('Red') == 3:
            print("[Analysis] Streak Alert: 3 Reds in a row. Note: In independent RNG events, probability for the next draw remains 50-50.")
        elif last_three.count('Green') == 3:
            print("[Analysis] Streak Alert: 3 Greens in a row. Note: Probability for the next draw remains independent.")
        else:
            print("[Analysis] Mixed trend detected in recent sequence.")

if __name__ == "__main__":
    analyzer = ColorTrendAnalyzer()
    # Simulate data to see how the analyzer works
    analyzer.simulate_history(30)
    analyzer.analyze_trends()
