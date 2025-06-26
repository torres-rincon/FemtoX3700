# Define tolerance for approximate matching
TOLERANCE = 0.001

# Read DpDm file into memory as list of tuples (value, column2)
dpdm_data = []
with open('DpDm_corr_R4fm.dat', 'r') as f:
    for line in f:
        parts = line.split()
        if len(parts) >= 2:
            x = float(parts[0])
            y = float(parts[1])
            dpdm_data.append((x, y))

# Sort dpdm_data by x for efficient searching
dpdm_data.sort()

# Read cf file and perform approximate matching and summing
results = []
with open('cfD0D0Bar-r4fm-alpha0DOT67a180amuM1DOT0.dat', 'r') as f:
    for line in f:
        parts = line.split()
        if len(parts) >= 3:
            cf_x = float(parts[0])
            cf_y = float(parts[2])
            
            # Find closest match in dpdm_data
            closest_diff = float('inf')
            closest_y = None
            for dpdm_x, dpdm_y in dpdm_data:
                diff = abs(cf_x - dpdm_x)
                if diff < closest_diff and diff <= TOLERANCE:
                    closest_diff = diff
                    closest_y = dpdm_y
            
            # If a match found within tolerance, sum and save result
            if closest_y is not None:
                sum_y = cf_y + closest_y
                results.append((cf_x, sum_y-1))

# Save results to output file
with open('C_DpDm_v180_amu1_R4.dat', 'w') as f:
    for x, y_sum in results:
        f.write(f'{x:.8f} {y_sum:.8f}\n')

print(f"Saved {len(results)} combined results")

