import math


def calculate_triangular_jogouts(length_a, length_b, num_jogouts):
    """Calculate parameters for triangular jogouts (45° right-angle isosceles)"""
    total_length_to_add = length_a - length_b

    # For right-angle isosceles triangle jogouts
    # Each jogout adds length = (2*s) - s*sqrt(2) ≈ 0.5858*s
    side_length = total_length_to_add / (num_jogouts * (2 - math.sqrt(2)))

    added_length_per_jogout = (2 * side_length) - (side_length * math.sqrt(2))
    total_added_length = added_length_per_jogout * num_jogouts

    return {
        'jogout_type': "45° right-angle isosceles triangle",
        'side_length': side_length,
        'added_length_per_jogout': added_length_per_jogout,
        'total_added_length': total_added_length,
        'description': f"Each jogout has two sides of {side_length:.4f} mm at 90°",
        'diagram': """
        Triangular Jogout:
           /|
          / |
         /  |
        /___|
        """
    }


def calculate_trapezoidal_jogouts(length_a, length_b, num_jogouts, angle_degrees=60):
    """Calculate parameters for proper trapezoidal jogouts"""
    total_length_to_add = length_a - length_b
    angle_radians = math.radians(angle_degrees)

    # For trapezoidal jogout: /---\
    # Where the angled sides are length 's' and top is length 's'
    # The added length is 2*s*(1 - cosθ)
    side_length = total_length_to_add / (num_jogouts * 2 * (1 - math.cos(angle_radians)))

    added_length_per_jogout = 2 * side_length * (1 - math.cos(angle_radians))
    total_added_length = added_length_per_jogout * num_jogouts

    horizontal_offset = side_length * math.sin(angle_radians)

    return {
        'jogout_type': f"Trapezoidal ({angle_degrees}° angled sides)",
        'side_length': side_length,
        'added_length_per_jogout': added_length_per_jogout,
        'total_added_length': total_added_length,
        'horizontal_offset': horizontal_offset,
        'description': f"Each jogout has two {side_length:.4f} mm sides at {angle_degrees}° and a {side_length:.4f} mm top",
        'diagram': f"""
        Trapezoidal Jogout:
          /{'-' * int(side_length * 2)}\\
         /{' ' * int(side_length * 2)}\\
        /{'_' * int(side_length * 2)}\\
        (Each side: {side_length:.2f}mm, top: {side_length:.2f}mm)
        """
    }


def get_user_input():
    """Get input parameters from user"""
    print("\nPCB Differential Pair Length Matching Calculator")
    print("----------------------------------------------")

    # Get jogout type
    print("\nSelect jogout type:")
    print("1. Triangular (45° right-angle isosceles)")
    print("2. Trapezoidal (angled sides with horizontal top)")
    choice = input("Enter choice (1 or 2): ").strip()
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter choice (1 or 2): ").strip()

    if choice == '2':
        angle = float(input("Enter angle for trapezoidal sides (degrees, typically 45-60): "))
    else:
        angle = None

    length_a = float(input("\nEnter length of trace to match (longer trace, mm): "))
    length_b = float(input("Enter length of trace to change (shorter trace, mm): "))
    num_jogouts = int(input("Enter number of jogouts to add: "))

    return length_a, length_b, num_jogouts, choice, angle


def display_results(params, length_a, length_b, num_jogouts):
    """Display the calculation results"""
    print("\nResults:")
    print("--------")
    print(f"Trace to match (longer trace): {length_a} mm")
    print(f"Trace to change (shorter trace): {length_b} mm")
    print(f"Number of jogouts: {num_jogouts}")
    print(f"Jogout type: {params['jogout_type']}")
    print(f"\nTotal length to add: {length_a - length_b:.4f} mm")

    print(f"\nParameters:")
    if params['jogout_type'].startswith("45°"):
        print(f"- Side length: {params['side_length']:.4f} mm")
    else:
        print(f"- Side length: {params['side_length']:.4f} mm")
        print(f"- Top length: {params['side_length']:.4f} mm")
        print(f"- Horizontal offset: {params['horizontal_offset']:.4f} mm")

    print(f"- Length added per jogout: {params['added_length_per_jogout']:.4f} mm")
    print(f"- Total added length: {params['total_added_length']:.4f} mm")

    print("\n" + params['diagram'])
    print(f"\nImplementation notes: {params['description']}")

    # Verification
    if abs(params['total_added_length'] - (length_a - length_b)) > 0.001:
        print("\nWarning: Small rounding error detected in calculations")


def main():
    """Main program function"""
    while True:
        length_a, length_b, num_jogouts, choice, angle = get_user_input()

        if length_b > length_a:
            print("\nWarning: The 'trace to change' is longer than the 'trace to match'!")
            print("You should be adding jogouts to the shorter trace instead.")
            if input("Swap the values and continue? (y/n): ").lower() == 'y':
                length_a, length_b = length_b, length_a
            else:
                continue

        if choice == '1':
            params = calculate_triangular_jogouts(length_a, length_b, num_jogouts)
        else:
            params = calculate_trapezoidal_jogouts(length_a, length_b, num_jogouts, angle)

        display_results(params, length_a, length_b, num_jogouts)

        if input("\nCalculate another? (y/n): ").lower() != 'y':
            print("\nHappy PCB routing!")
            break


if __name__ == "__main__":
    main()
