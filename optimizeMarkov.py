import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Load the Excel file
file_path = 'optimization .xlsx' #your file here
data = pd.read_excel(file_path, sheet_name='0000')

# Extract the required columns for transition rates (h) and corresponding states
n_values = pd.to_numeric(data['n'], errors='coerce').fillna(0).values
h_values = pd.to_numeric(data['h'], errors='coerce').fillna(0).values
cost_values = pd.to_numeric(data['Cost'], errors='coerce').fillna(0).values

# Define the specific lambda sums for each transition
lambda_sums = {
    3: 0.002933,
    9: 0.002769,
    13: 0.002583,
    14: 0.002366,
    15: 0.001967
}

# Define the cost function
def cost_function(x):
    T1, T2 = x
    adjusted_h = h_values.copy()
    # Update based on T1 and T2 for respective indices
    adjusted_h[3] = np.log(T2) / lambda_sums[3]
    adjusted_h[9] = np.log(T2) / lambda_sums[9]
    adjusted_h[15] = np.log(T1) / lambda_sums[15]
    adjusted_h[13] = np.log(T1) / lambda_sums[13]
    adjusted_h[14] = np.log(T1) / lambda_sums[14]
    
    nh_values = adjusted_h * n_values
    sum_nh = np.sum(nh_values)
    π_values = nh_values / sum_nh
    cost = np.sum(π_values * cost_values)
    return cost

# Define the availability function
def availability_function(x):
    T1, T2 = x
    adjusted_h = h_values.copy()
    # Update based on T1 and T2 for respective indices
    adjusted_h[3] = np.log(T2) / lambda_sums[3]
    adjusted_h[9] = np.log(T2) / lambda_sums[9]
    adjusted_h[15] = np.log(T1) / lambda_sums[15]
    adjusted_h[13] = np.log(T1) / lambda_sums[13]
    adjusted_h[14] = np.log(T1) / lambda_sums[14]
    
    nh_values = adjusted_h * n_values
    sum_nh = np.sum(nh_values)
    π_values = nh_values / sum_nh
    availability_indices = [1, 2, 3, 7, 8, 9, 13, 14, 15]
    availability = np.sum(π_values[availability_indices])
    return availability

# Constraint: Availability must be at least 0.99
def availability_constraint(x):
    return availability_function(x) - 0.99

# Initial guess for T1 and T2
initial_guess = [3000, 3000]

# Define the bounds for T1 and T2
bounds = [(1, 10000), (1, 10000)]

# Define the constraints
constraints = {
    'type': 'ineq',
    'fun': availability_constraint
}

# Perform the optimization using the COBYLA method
result_cobyla = minimize(cost_function, initial_guess, method='COBYLA', constraints=constraints)

# Extract the optimal values
optimal_T1_cobyla, optimal_T2_cobyla = result_cobyla.x
optimal_cost_cobyla = result_cobyla.fun
optimal_availability_cobyla = availability_function([optimal_T1_cobyla, optimal_T2_cobyla])

optimal_T1_cobyla, optimal_T2_cobyla, optimal_cost_cobyla, optimal_availability_cobyla

import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Load the Excel file
file_path = '/mnt/data/Μεταβάσεις_v8 with cost optimization - f.xlsx'
data = pd.read_excel(file_path, sheet_name='0000')

# Extract the required columns for transition rates (h) and corresponding states
n_values = pd.to_numeric(data['n'], errors='coerce').fillna(0).values
h_values = pd.to_numeric(data['h'], errors='coerce').fillna(0).values
cost_values = pd.to_numeric(data['Cost'], errors='coerce').fillna(0).values

# Define the specific lambda sums for each transition
lambda_sums = {
    3: 0.002933,
    9: 0.002769,
    13: 0.002583,
    14: 0.002366,
    15: 0.001967
}

# Define the cost function
def cost_function(x):
    T1, T2 = x
    adjusted_h = h_values.copy()
    # Update based on T1 and T2 for respective indices
    adjusted_h[3] = np.log(T2) / lambda_sums[3]
    adjusted_h[9] = np.log(T2) / lambda_sums[9]
    adjusted_h[15] = np.log(T1) / lambda_sums[15]
    adjusted_h[13] = np.log(T1) / lambda_sums[13]
    adjusted_h[14] = np.log(T1) / lambda_sums[14]
    
    nh_values = adjusted_h * n_values
    sum_nh = np.sum(nh_values)
    π_values = nh_values / sum_nh
    cost = np.sum(π_values * cost_values)
    return cost

# Define the availability function
def availability_function(x):
    T1, T2 = x
    adjusted_h = h_values.copy()
    # Update based on T1 and T2 for respective indices
    adjusted_h[3] = np.log(T2) / lambda_sums[3]
    adjusted_h[9] = np.log(T2) / lambda_sums[9]
    adjusted_h[15] = np.log(T1) / lambda_sums[15]
    adjusted_h[13] = np.log(T1) / lambda_sums[13]
    adjusted_h[14] = np.log(T1) / lambda_sums[14]
    
    nh_values = adjusted_h * n_values
    sum_nh = np.sum(nh_values)
    π_values = nh_values / sum_nh
    availability_indices = [1, 2, 3, 7, 8, 9, 13, 14, 15]
    availability = np.sum(π_values[availability_indices])
    return availability

# Constraint: Availability must be at least 0.99
def availability_constraint(x):
    return availability_function(x) - 0.99

# Initial guess for T1 and T2
initial_guess = [850, 2500]

# Define the bounds for T1 and T2
bounds = [(800, 900), (2200, 2600)]

# Define the constraints
constraints = {
    'type': 'ineq',
    'fun': availability_constraint
}

# Perform the optimization
result = minimize(cost_function, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

# Extract the optimal values
optimal_T1, optimal_T2 = result.x
optimal_cost = result.fun
optimal_availability = availability_function([optimal_T1, optimal_T2])

optimal_T1, optimal_T2, optimal_cost, optimal_availability
