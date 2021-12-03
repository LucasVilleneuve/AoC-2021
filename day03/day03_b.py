from aocd import lines


# Split diagnostics reports in two arrays based on their content at the idx position
def filter_diagnostics(reports, idx):
    ones, zeros = [], []
    for x in reports :
        if x[idx] == "1":
            ones.append(x)
        else :
            zeros.append(x)

    return ones, zeros


# Returns the correct oxygen report if oxygen == True, else returns the CO2 rating
def single_out_diagnostic(oxygen, diagnostics):
    for i in range(0, len(diagnostics[0])):
        ones, zeros = filter_diagnostics(diagnostics, i)

        if len(ones) >= (len(diagnostics) / 2) :
            diagnostics = ones if oxygen == True else zeros
        else :
            diagnostics = zeros if oxygen == True else ones

        if len(diagnostics) <= 1:
            break;
        

    if len(diagnostics) == 0:
        print("Error, couldn't single out a diagnostic report.")
        return 0

    return diagnostics[0]
    

oxygen_report = int(single_out_diagnostic(True, lines), 2)
CO2_rating = int(single_out_diagnostic(False, lines), 2)
life_support_rating = oxygen_report * CO2_rating

print(life_support_rating)