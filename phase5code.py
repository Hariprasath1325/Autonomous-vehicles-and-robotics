import random
import time

def simulate_distance():
    """Simulate a sensor reading for distance in cm."""
    return round(random.uniform(20.0, 100.0), 2)

def simulate_object_detection():
    """Simulate object detection using random choice."""
    return random.choice(["person", "wall", None])

def robot_decision(distance, detected_object):
    """Print decision based on sensor inputs."""
    detected_object_str = detected_object if detected_object is not None else 'None'
    print(f"Distance: {distance:.2f} cm | Detected: {detected_object_str}")

    if distance < 30.0 or detected_object == "wall":
        print("→ Obstacle detected. Stopping.\n")
    else:
        print("→ Moving forward...\n")

def main():
    for cycle in range(1, 6):  # Run 5 simulation cycles
        print(f"--- Simulation Cycle {cycle} ---")
        distance = simulate_distance()
        detected_object = simulate_object_detection()
        robot_decision(distance, detected_object)
        time.sleep(1)

if __name__ == "__main__":
    main()