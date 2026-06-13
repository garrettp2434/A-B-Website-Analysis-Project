## DAX Measures

AVG Purchase Amount = AVERAGE('AB Testing Data'[purchase_amount])

Control Rate = CALCULATE(AVERAGE('AB Testing Data'[converted]),
    'AB Testing Data'[group] = "control")

Conversion Rate = 
DIVIDE(
    SUM('AB Testing Data'[converted]),
    COUNT('AB Testing Data'[converted])
)

Relative Lift = 
DIVIDE(
    [Treatment Rate] - [Control Rate],
    [Control Rate]
)

Treatment Rate = CALCULATE(
    AVERAGE('AB Testing Data'[converted]),
    'AB Testing Data'[group] = "treatment"
)