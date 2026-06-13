# WEBSITE A/B TESTING ANALYSIS: BUSINESS INSIGHTS & RECOMMENDATIONS

## Executive Summary

This project evaluated the effectiveness of a redesigned website landing page (treatment group) compared to the existing landing page (control group). The goal was to determine whether the new page increased user conversions and provided a measurable business benefit.

---

## Project Objective

Determine whether the treatment landing page produces a higher conversion rate than the control landing page and assess whether the difference is statistically significant.

---

## Dataset Overview

### Dataset Size

* Total Records: 294478
* Control Group Users: 146926
* Treatment Group Users: 147552

---

# Insights

## 1. Conversion Rate Comparison

![Conversion Rate by Group](visuals/conversions_by_group.png)

### Results

| Group     | Conversion Rate |
| --------- | --------------- |
| Control   | 11.87%       |
| Treatment | 17.95%       |

### Insight

The treatment landing page achieved a higher conversion rate than the control page, indicating that the redesigned landing page was more effective at driving user conversions.

---

## 2. Statistical Significance Testing

### Method

A two-proportion Z-test was conducted to compare conversion rates between the control and treatment groups.

### Results

| Metric      | Value    |
| ----------- | -------- |
| Z-Statistic | -46.27   |
| P-Value     | 0.0      |

### Insight

The results indicate that the difference in conversion rates between the two groups is statistically significant and unlikely to have occurred by chance. The negative Z-statistic indicates that the treatment group's conversion rate was higher than the control group's conversion rate. Because the test was performed using the control group as the reference group, the difference between the two groups resulted in a large negative value. The magnitude of the Z-statistic (46.27 standard deviations from the null hypothesis) indicates an extremely large separation between the observed conversion rates.

The P-value of 0.0 does not mean the probability is exactly zero. Rather, it means the probability is so small that it was likely rounded to zero by the software. This indicates overwhelming statistical evidence that the observed difference between the control and treatment groups was not caused by random chance. Additionally, the large sample size of nearly 270,000 users in the dataset further increases the reliability of the results.

---

## 3. Relative Lift Analysis

### Result

Relative Lift: 51.18%

### Insight

The treatment landing page generated a 51.18% relative lift in conversion rate compared to the control page. This indicates that users exposed to the redesigned landing page were substantially more likely to convert, demonstrating a meaningful improvement in performance.

---

## 4. Conversion Rate by Weekday

![Weekday Conversion Rate](visuals/weekday_conversion.png)

### Insight

Conversion performance remained relatively consistent throughout the week, suggesting that the effectiveness of the treatment page was not dependent on a specific day.

---

## 5. Monthly Conversion Trends

![Monthly Conversion Trend](visuals/monthly_conversion_trend.png)

### Insight

Monthly conversion rates remained relatively stable throughout the year, with a slight decline between April and September before recovering toward the end of the year. With the highest monthly conversion rate of 15.29%, and the lowest of 14.46%, this suggests that while conversion performance experienced a modest mid-year dip, overall user engagement and conversion behavior remained consistent over time.

---

## 6. Device Performance Analysis

|Device   |   Group     | Conversions |
|---------|-------------|-------------|
|Desktop  |   control   |   10563     |
|         |   treatment |   15966     |
|Mobile   |   control   |    6010     |
|         |   treatment |   9196      |
|Tablet   |   control   |    871      |
|         |   treatment |   1322      |

### Insight

The treatment page demonstrated improved conversion performance across multiple device types, with an approximate improvement of 6% for each device. This indicates that the redesign was effective for a broad range of users.

---

## 7. Geographic Performance Analysis

| Location   | Conversions  | Conversion Rate (%)|
|------------|--------------|--------------------|
|US          | 13159        | 14.8955
|India       |  8864        | 15.0202
|UK          |  6597        | 14.9196
|Pakistan    |  4409        | 14.8953
|Canada      |  4404        | 15.0610
|Germany     |  4317        | 14.6453
|Australia   |  2178        | 14.9311

### Insight

Location-level analysis revealed major differences in total conversion behavior across regions, providing opportunities for future audience targeting and optimization efforts in places such as Canada, Germany, and Australia. The similar conversion rates regardless of total in each location further back the possibility of future expansion projects.

---

## 8. Purchase Amount Analysis

|Group     | Avg. Purchase Amount|
|----------|---------------------|
|control   |   $4.45
|treatment |   $6.76

### Insight

Users in the treatment group generated a higher average purchase amount compared to users in the control group. This suggests that the redesigned landing page not only increased conversion rates but also encouraged higher customer spending, indicating a positive impact on overall revenue potential.

---

# Business Recommendations

## Recommendation 1: Deploy the Treatment Landing Page

The treatment page consistently outperformed the control page and demonstrated statistically significant improvements in conversion rate.

### Expected Impact

* Increased conversions
* Improved user engagement
* Improved business performance

---

## Recommendation 2: Continue Monitoring Performance

Following deployment, monitor key performance indicators to ensure that conversion improvements remain stable over time.

Recommended metrics include:

* Conversion Rate
* Revenue per User
* Purchase Amount

---

## Recommendation 3: Conduct Additional A/B Tests

Future experiments could evaluate:

* Call-to-action button placement
* Checkout process improvements
* Product page layout
* Mobile user experience enhancements

---

## Recommendation 4: Focus on High-Performing Segments

Future optimization efforts should prioritize:

* High-converting locations
* High-converting device types
* High-engagement user segments

---

# Conclusion

The treatment landing page significantly outperformed the control page and produced a meaningful increase in conversion rate. Statistical testing confirmed that the improvement was highly significant, supporting the recommendation to deploy the treatment experience and continue experimentation to further improve website performance.

