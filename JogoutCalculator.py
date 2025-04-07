import math

def calculate_jogout_parameters(length_a,length_b,num_jogouts):
    # Calculate total length to add
    total_length_to_add = length_a - length_b

    # For Right-angle isosceles triangle jogouts:
    # Each jogout adds legnth = (2*s)-s*sqrt(2) = .5858*s
    side_length = total_length_to_add / (num_jogouts * (2 - math.sqrt(2)))

    added_length_per_jogout = (2 * side_length) - (side_length * math.sqrt(2))
    total_added_length = added_length_per_jogout * num_jogouts

    return {
        'trace_to_match' : length_a,
        'trace_to_change' : length_b,
        'total_length_to_add' : total_length_to_add,
        'side_length' : side_length,
        'added_length_per_jogout' : added_length_per_jogout,
        'total_added_length' : total_added_length,
        'num_jogouts' : num_jogouts
    }

def get_user_input():
    """get input paramters from user"""
    print("PCB Diff Pair Length Matching Calculator")

    length_a = float(input("Enter length of trace to match (longer trace, mm): "))
    length_b = float(input("Enter length of trace to change (shorter trace, mm): "))
    num_jogouts = int(input("Enter number of jogouts to add: "))

    return length_a, length_b, num_jogouts

def display_results(params):
    """Display the calculation results"""
    print("\nResults:")
    print("--------")
    print(f"Trace to match (longer trace): {params['trace_to_match']} mm")
    print(f"Trace to change (shorter trace): {params['trace_to_change']} mm")
    print(f"Number of jogouts: {params['num_jogouts']}")
    print(f"\nTotal length to add: {params['total_length_to_add']:.4f} mm")
    print(f"\nSide length for each jogout: {params['side_length']:.4f} mm")
    print(f"\nLength added per jogout: {params['added_length_per_jogout']:.4f} mm")
    print(f"\nTotal added length: {params['total_added_length']:.4f} mm")

    #Verify
    if abs(params['total_added_length'] - params['total_length_to_add']) > 0.001:
        print("\nWarning: There may be a small rouding error of some kind")

def main():
    """Main program function"""
    length_a, length_b, num_jogouts = get_user_input()

    if length_b > length_a:
        length_a, length_b = length_b, length_a

    params = calculate_jogout_parameters(length_a, length_b, num_jogouts)
    display_results(params)

if __name__ == "__main__":
    main()
