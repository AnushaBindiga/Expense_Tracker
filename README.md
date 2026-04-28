#  Expense Tracker with Budget Alerts & Visual Reporting

A Python command-line application that helps users track their daily expenses, set budgets, monitor spending habits, and generate automated Excel and Power BI reports with visual insights.

---

##  Why I Built This

Most people have no clear visibility into where their money goes each month. This tool solves that by combining expense tracking, budget alerts, and automated visual reporting — turning raw spending data into actionable insights.

---

##  Features

-  **Add expenses** with date, category and description
-  **View all expenses** in a clean formatted table
-  **Set budgets** — total monthly and per category limits
-  **Budget validation** — warns if category budgets exceed total
-  **Color coded alerts** — green, amber and red spending status
-  **Auto Excel report** — formatted table and bar chart generated automatically
-  **Power BI dashboard** — 4 interactive visuals connected to live data

---

##  Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core application logic |
| CSV | Expense data storage |
| JSON | Budget configuration storage |
| Colorama | Terminal color alerts |
| OpenPyXL | Excel report generation |
| Power BI Desktop | Interactive dashboard |
| Git and GitHub | Version control |

---

##  How to Run

**1. Clone the repository**

```bash
git clone https://github.com/AnushaBindiga/Expense_Tracker.git
cd Expense_Tracker
```

**2. Install dependencies**

```bash
python -m pip install colorama openpyxl
```

**3. Run the application**

```bash
python expense_tracker.py
```

**4. Follow the menu**
==== Expense Tracker ====

1.Add expense
2.View all expenses
3.Set budget
4.Show summary
5.Generate Excel report
6.Exit

---

##  Sample Output

### Terminal — Budget Summary
-  Green = under 75% of budget
-  Amber = between 75% and 100% of budget
-  Red = budget exceeded

### Excel Report
Auto generated expense_report.xlsx with:
- Formatted expense table with blue headers
- Color coded budget summary sheet
- Bar chart comparing spent vs budget per category

### Power BI Dashboard
Interactive expense_dashboard.pbix with:
- Total spent card
- Spending by category bar chart
- Budget vs spent donut chart
- Budget vs spent clustered column chart

---

##  Project Structure
Expense_Tracker/
├── expense_tracker.py     # Main application
├── expenses.csv           # Expense data
├── budget.json            # Budget configuration
├── expense_report.xlsx    # Auto generated Excel report
├── expense_dashboard.pbix # Power BI dashboard
└── README.md              # Project documentation
---

##  Future Improvements

- Web or mobile interface
- Voice input for adding expenses
- Multi-user support
- Monthly email reports
- Integration with bank APIs

---

##  Author

**Anusha Bindiga**
Aspiring Business and Data Analyst
[GitHub](https://github.com/AnushaBindiga)