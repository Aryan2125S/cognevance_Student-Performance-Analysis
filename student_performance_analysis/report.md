# STUDENT PERFORMANCE & ATTENDANCE TRENDS REPORT
**Internship Project Report (Level 1)**  
**Author:** 2nd-Year Computer Science (AI) Student  
**Target Subject:** Secondary Education Mathematics Performance  

---

## 1. Executive Summary
This report analyzes a cohort of 395 secondary school students to determine the factors influencing their academic outcomes. The primary focus is investigating the relationship between class attendance and final grades ($G3$). 

By separating academic dropouts/absences from active participants, we identified that attendance has a **statistically significant positive impact** on grades. Combined with weekly study habits and household educational support, these indicators can help administrators predict academic risk early in the school year.

---

## 2. Dataset Overview & Variables
The analysis utilizes the **UCI Student Performance Dataset**, which captures student records across two Portuguese schools.
*   **Sample Size:** 395 students
*   **Target Grade ($G3$):** Final course grade (measured on a 0-20 scale)
*   **Key Inputs Evaluated:** Absences (attendance rate), weekly study time, extra educational support, and parental education levels.

---

## 3. Data Preprocessing & Cleaning Steps
A major portion of this project was setting up a data cleaning pipeline to ensure statistical accuracy:
1.  **Attendance Conversion:** Absences were converted to an Attendance Rate (%) using:
    $$\text{Attendance Rate} = \frac{180 - \text{absences}}{180} \times 100$$
2.  **Attendance Grouping:** Students were categorized into Good ($\ge 90\%$), Average ($75\% - 89\%$), and Poor ($< 75\%$) attendance groups.
3.  **Absence/Dropout Isolation:** We identified **38 students** who scored exactly 0 on the final exam ($G3 = 0$) despite scoring well in earlier periods ($G1, G2 > 8$) and having very low absences. These records were flagged as **Absent/Dropout** in a new `status` field to prevent skewing academic correlations, while preserving their demographical values.

---

## 4. Key Findings & Statistics

### A. Attendance vs. Final Grades ($G3$)
*   **Overall Sample Correlation:** $r = -0.034$ (skewed by dropout zeros)
*   **Cleaned Active Sample Correlation:** $r = 0.213$ (weak-to-moderate positive linear relationship)
*   **Group Averages:**
    *   **Good Attendance ($\ge 90\%$):** 11.23 / 20 average grade (279 students)
    *   **Average Attendance ($75\% - 89\%$):** 8.87 / 20 average grade (76 students)
    *   **Poor Attendance ($< 75\%$):** 7.78 / 20 average grade (40 students)

*Conclusion: Students with chronic absences ($< 75\%$) face an average performance drop of 30.7% compared to those attending regularly.*

### B. Weekly Study Time vs. Final Grades ($G3$)
Academic grades increase steadily with study time investment:
*   **$< 2$ hours/week:** 9.25 / 20 average final score
*   **$2 - 5$ hours/week:** 10.17 / 20 average final score
*   **$5 - 10$ hours/week:** 11.41 / 20 average final score
*   **$> 10$ hours/week:** 11.26 / 20 average final score

*Conclusion: Moving students from studying $< 2$ hours to $2 - 5$ hours yields the highest immediate return on grade improvement (+0.92 grade points).*

### C. Parental Education Baseline Impact
Mother's educational level significantly influences student performance baseline:
*   **Higher Education:** 11.76 / 20 average grade
*   **None/Primary Education:** 9.60 / 20 average grade

---

## 5. Actionable Recommendations

1.  **Deploy an Early Warning System (EWS):** School systems should flag any student whose attendance drops below **90%** during the first grading period ($G1$) rather than waiting for semester failures.
2.  **Transition to Proactive Support:** Currently, extra school support (`schoolsup`) is reactive (assigned to already-failing students). Support programs should proactively invite students who exhibit attendance issues or study time shortages early.
3.  **Encourage "Study Smart" Workshops:** Implement weekly active study sessions to help students transition from the low-study bracket ($< 2$ hours) to the average bracket ($2 - 5$ hours).
4.  **Engage Parents:** Provide home learning resources and guidelines to parents, particularly those without higher education backgrounds, to help align home study environments with school academic goals.
