import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import calendar

def generate_toyota_sales_data():
    # Car models with their base prices and seasonality factors
    car_models = {
        'Camry': {'base_price': 25000, 'seasonal_factor': 1.2},
        'Corolla': {'base_price': 20000, 'seasonal_factor': 1.1},
        'RAV4': {'base_price': 27000, 'seasonal_factor': 1.3},
        'Highlander': {'base_price': 35000, 'seasonal_factor': 1.4},
        'Tacoma': {'base_price': 27000, 'seasonal_factor': 1.2},
        'Tundra': {'base_price': 35000, 'seasonal_factor': 1.1},
        'Prius': {'base_price': 25000, 'seasonal_factor': 1.0},
        'Sienna': {'base_price': 32000, 'seasonal_factor': 1.2}
    }

    # Generate sales rep data (assuming 20 sales reps)
    sales_reps = pd.DataFrame({
        'rep_id': range(1, 21),
        'experience_years': np.random.randint(1, 20, 20),
        'performance_rating': np.random.uniform(0.8, 1.2, 20)
    })

    # Date range
    start_date = datetime(2014, 1, 1)
    end_date = datetime(2025, 3, 31)
    current_date = start_date
    
    # Initialize global sale_id counter
    global_sale_id = 1

    while current_date <= end_date:
        # Calculate seasonality factors
        month = current_date.month
        year = current_date.year
        
        # Seasonal adjustments
        season_factor = {
            12: 1.3,  # December (holiday season)
            1: 0.8,   # January (post-holiday slump)
            2: 0.9,   # February
            3: 1.1,   # March (tax refunds)
            4: 1.2,   # April (spring buying)
            5: 1.2,   # May
            6: 1.1,   # June
            7: 1.0,   # July
            8: 1.1,   # August (model year clearance)
            9: 1.0,   # September
            10: 0.9,  # October
            11: 1.1   # November
        }[month]

        # Economic cycle factor (assuming 7-year cycles)
        economic_cycle = np.sin(2 * np.pi * ((year - 2014) % 7) / 7) * 0.1 + 1

        # Generate random number of sales (5000-8000)
        num_sales = np.random.randint(5000, 8000)
        
        # Create sales data
        sales_data = []
        for _ in range(num_sales):
            # Random sale date within the month
            sale_date = datetime(year, month, 
                               np.random.randint(1, calendar.monthrange(year, month)[1] + 1))
            
            # Select random car model and sales rep
            car_model = np.random.choice(list(car_models.keys()))
            rep_id = np.random.randint(1, 21)  # Changed to 20 reps
            rep_experience = sales_reps.loc[sales_reps['rep_id'] == rep_id, 'experience_years'].iloc[0]
            rep_rating = sales_reps.loc[sales_reps['rep_id'] == rep_id, 'performance_rating'].iloc[0]

            # Calculate sale amount with various factors
            base_price = car_models[car_model]['base_price']
            model_seasonality = car_models[car_model]['seasonal_factor']
            experience_factor = 1 + (rep_experience * 0.01)
            
            # Final sale amount with randomness
            sale_amount = base_price * \
                         season_factor * \
                         economic_cycle * \
                         model_seasonality * \
                         experience_factor * \
                         rep_rating * \
                         np.random.uniform(0.9, 1.1)

            # Commission percentage (varies by experience and performance)
            commission_pct = min(8.0, 2.0 + (rep_experience * 0.1) + (rep_rating * 2))

            sales_data.append({
                'sale_id': global_sale_id,  # Use global counter instead of len(sales_data) + 1
                'sale_rep_id': rep_id,
                'sale_date': sale_date.strftime('%Y-%m-%d'),
                'car_model': car_model,
                'sale_amount': round(sale_amount, 2),
                'commission_pct': round(commission_pct, 2),
                'sale_status': np.random.choice(['Completed', 'Pending', 'Cancelled'], 
                                              p=[0.95, 0.03, 0.02])
            })
            global_sale_id += 1  # Increment the global counter

        # Create DataFrame and save to CSV
        df = pd.DataFrame(sales_data)
        filename = f"toyota_sales_{year}_{month:02d}.csv"
        df.to_csv(filename, index=False)

        # Move to next month
        if month == 12:
            current_date = datetime(year + 1, 1, 1)
        else:
            current_date = datetime(year, month + 1, 1)

if __name__ == "__main__":
    generate_toyota_sales_data()