def remplace_fillna(df, column, value):
    df.loc[:, column].fillna(value, inplace=True)
    
def monthly_debt(df):
    df.loc[:,'MonthlyDebt']=df['DebtRatio']*df['MonthlyIncome']
    df.loc[df['MonthlyIncome'] == 0,'MonthlyDebt']=df.loc[df['MonthlyIncome'] == 0,'DebtRatio']
    df.loc[df['MonthlyIncome'] == 0,'DebtRatio']=None


def disposable_income(df):
    df.loc[:,'DisposableIncome']=df['MonthlyIncome']-df['MonthlyDebt']
    df.loc[df['MonthlyIncome'] == 0,'DisposableIncome']=0

    
def balanced_income(df):    
    df.loc[:,'BalancedIncome']= df['MonthlyIncome'] / (df['NumberOfDependents']+1)

def balanced_income_per_dependent(df):
    df.loc[:,'BalancedIncomePerDependent']= df['DisposableIncome'] / (df['NumberOfDependents']+1)

def weighted_of_late_payment(df):
    df['WeightedOfLatePayment']=   (df['NumberOfTime30-59DaysPastDueNotWorse']*1) + (df['NumberOfTime60-89DaysPastDueNotWorse']*2) + (df['NumberOfTimes90DaysLate']*3)

def debt_ratio_ok(df, debt_value):
    df.loc[df['MonthlyIncome'] == 0,'DebtRatio']=debt_value


def drop_columns(df, columns):
    for column in columns:
        df.drop(column, axis=1, inplace=True)