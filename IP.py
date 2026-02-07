import sys
import matplotlib.pyplot as plt

# =========================================================
# DAA INDIVIDUAL PROJECT
# TITLE: Counting Sort Algorithm Implementation
# =========================================================

def read_input():
    """
    Reads input from the user, validates it strictly, and returns a list of integers.
    Reprompts if validation fails.
    """
    print("\n--- INPUT PHASE ---")
    
    while True:
        try:
            print("Enter non-negative integers separated by space:")
            user_input = input().strip()
            
            # Check for empty input
            if not user_input:
                print("\n<<<<<===== ARRAY IS EMPTY. SORTING NOT POSSIBLE. TRY AGAIN. =====>>>>>")
                continue

            # Split and convert to integers
            arr = []
            valid_integers = True
            for item in user_input.split():
                try:
                    num = int(item)
                    arr.append(num)
                except ValueError:
                    # Validation: Non-integer input
                    print(f"\n<<<<<===== INVALID INPUT! '{item}' IS NOT AN INTEGER. TRY AGAIN. =====>>>>>")
                    valid_integers = False
                    break
            
            if not valid_integers:
                continue
        
            # Validation: Negative numbers
            has_negative = False
            for num in arr:
                if num < 0:
                    print(f"\n<<<<<===== COUNTING SORT DOES NOT SUPPORT NEGATIVE NUMBERS ({num}). TRY AGAIN. =====>>>>>")
                    has_negative = True
                    break
            
            if has_negative:
                continue
                
            return arr
            
        except EOFError:
            print("\n<<<<<===== UNEXPECTED END OF INPUT =====>>>>>")
            sys.exit()
        except KeyboardInterrupt:
            print("\n<<<<<===== OPERATION CANCELLED =====>>>>>")
            sys.exit()

def find_maximum(arr):
    """
    Finds the maximum element in the array.
    """
    print("\nSTEP 2: FIND MAXIMUM ELEMENT")
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]

    print(f"Maximum element found: {max_val}")
    return max_val

def build_frequency_array(arr, max_val):
    """
    Builds frequency array based on input array.
    """
    print("\nSTEP 3: FREQUENCY COUNT PHASE")
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    print("Frequency array C:")
    for i in range(len(count)):
        if count[i] > 0:
            print(f"Value {i} occurs {count[i]} times")
    
    return count

def build_cumulative_count(count):
    """
    Converts frequency array into cumulative count array.
    """
    print("\nSTEP 4: CUMULATIVE COUNT PHASE")
    print("Applying Formula: Count[i] = Count[i] + Count[i-1]")
    
    cumulative_count = list(count)
    for i in range(1, len(cumulative_count)):
        cumulative_count[i] += cumulative_count[i - 1]
        print(f"  Index {i}: Count[{i}] = {count[i]} + {cumulative_count[i-1]} = {cumulative_count[i]}")

    print("Cumulative count array:")
    print(cumulative_count)
    return cumulative_count

def build_sorted_array(arr, cumulative_count):
    """
    Builds sorted array using cumulative count.
    Final Output Phase.
    """
    print("\nSTEP 5: OUTPUT CONSTRUCTION PHASE")
    output = [0] * len(arr)
    
    count_working = list(cumulative_count)

    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        position = count_working[current] - 1
        output[position] = current
        count_working[current] -= 1

        print(
            f"==> Placing {current} at position {position}, "
            f"updated count for {current} to {count_working[current]}"
        )

    return output

def draw_array(ax, arr, title, y_pos=0.5):
    """
    Helper function to draw an array as a sequence of boxes.
    """
    n = len(arr)
    ax.set_xlim(-0.5, n + 0.5)
    ax.set_ylim(0, 2)
    ax.axis('off')
    ax.set_title(title, fontsize=12, pad=20)
    
    # Draw boxes
    for i, val in enumerate(arr):
        # Draw rectangle
        rect = plt.Rectangle((i, y_pos), 1, 1, facecolor='lightblue', edgecolor='black')
        ax.add_patch(rect)
        
        # Add value text
        ax.text(i + 0.5, y_pos + 0.5, str(val), ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Add index text
        ax.text(i + 0.5, y_pos + 1.2, str(i), ha='center', va='bottom', fontsize=10, color='red')
    
    # Add label for "Index" and "Value"
    ax.text(-0.8, y_pos + 1.2, "Index", ha='right', va='bottom', fontsize=10, color='red')
    ax.text(-0.8, y_pos + 0.5, "Value", ha='right', va='center', fontsize=12, fontweight='bold')

def visualize_all_steps(arr, frequency_arr, cumulative_arr, sorted_arr):
    """
    Visualizes all major steps of Counting Sort in one figure with subplots using array diagrams.
    """
    print("\n--- GENERATING VISUALIZATION ---")
    
    fig, axs = plt.subplots(4, 1, figsize=(10, 12))
    fig.suptitle('Counting Sort Algorithm Steps', fontsize=16)
    
    # Subplot 1: Input Array
    draw_array(axs[0], arr, 'STEP 1: Input Array')
    
    # Subplot 2: Frequency Array
    draw_array(axs[1], frequency_arr, 'STEP 3: Frequency Array (Count)')
    
    # Subplot 3: Cumulative Count Array
    draw_array(axs[2], cumulative_arr, 'STEP 4: Cumulative Count Array')
    
    # Subplot 4: Sorted Array
    draw_array(axs[3], sorted_arr, 'FINAL STEP: Sorted Output Array')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    output_filename = 'counting_sort_steps.png'
    plt.savefig(output_filename)
    print(f"Graph saved as '{output_filename}'")
    plt.show()

def main():
    # 1. Input
    arr = read_input()
    print("\nSTEP 1: INPUT RECEIVED")
    print("~~~~~> Original Array: <~~~~~")
    print(arr)
    
    # 2. Find Max
    max_val = find_maximum(arr)
    
    # 3. Frequency Array
    frequency = build_frequency_array(arr, max_val)
    
    # 4. Cumulative Count
    cumulative = build_cumulative_count(frequency)
    
    # 5. Sorted Array
    sorted_arr = build_sorted_array(arr, cumulative)
    
    print("\n--- FINAL OUTPUT ---")
    print("~~~~~> Sorted Array: <~~~~~")
    print(sorted_arr)
    
    print("\n<<<<============>>>> SORTING COMPLETED SUCCESSFULLY <<<<============>>>>")
    
    # 6. Visualization
    try:
        visualize_all_steps(arr, frequency, cumulative, sorted_arr)
    except Exception as e:
        print(f"\nWarning: Could not generate visualization. Error: {e}")

if __name__ == "__main__":
    main()
