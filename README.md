#### **Screen Time Analysis Project**  
This project analyzes mobile screen time data to identify patterns and trends in app usage. The focus is on categorizing apps into "distracting" and "productive" and visualizing the most and least predictive hours of the day.

#### **Features**  
1. **Data Simulation**:  
   - Generated synthetic data for 30 days (~3,000 rows), including app usage by hour and category.  

2. **Analysis**:  
   - Calculated total and normalized screen time for distracting apps by the hour.  
   - Identified most and least predictive hours for distracting app usage.  

3. **Visualization**:  
   - Bar plot highlighting normalized distracting app usage across 24 hours.  

#### **Technologies Used**  
- **Python Libraries**:  
  - **Pandas**: Data processing and aggregation.  
  - **Matplotlib**: Data visualization.  
  - **Seaborn**: Enhanced visual aesthetics.  
  - **NumPy**: Statistical calculations (mean, standard deviation).  

#### **How to Run**  
1. Install the required libraries:  
   ```
   pip install pandas matplotlib seaborn numpy
   ```
2. Place the `screen_time_data.csv` file in the same directory as the script.  
3. Run the script:  
   ```
   python analysis.py
   ```
4. View the results in the console and the generated visualizations.

---
