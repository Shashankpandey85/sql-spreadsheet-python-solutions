# Spreadsheet Analytics Solutions

## 1. Populate ticket_created_at in Feedbacks Table

### Problem
Fill the `ticket_created_at` column in feedbacks table by matching with `created_at` from tickets table.

### Solution: Using VLOOKUP
```excel
=VLOOKUP(A2, ticket!A:B, 2, FALSE)
```

**Steps:**
1. Go to feedbacks worksheet
2. Click on cell D2 (first data row of ticket_created_at)
3. Enter the formula above
4. Press Enter
5. Copy formula down to all data rows (Ctrl+C then select range and Ctrl+V)

### Alternative: Using INDEX/MATCH (More Robust)
```excel
=INDEX(ticket!B:B, MATCH(A2, ticket!A:A, 0))
```

**Advantages:**
- Works even if columns are inserted/deleted
- Better performance with large datasets
- Cleaner formula structure

### Example Result
```
cms_id          | feedback_at         | feedback_rating | ticket_created_at
vew-iuvd-12     | 2021-08-21 13:26:48 | 3               | 2021-08-19 16:45:43
```

---

## 2. Outlet-wise Tickets: Same Day Creation and Closure

### Problem
Count tickets created and closed on the same day for each outlet.

### Solution Approach

**Step 1: Create Helper Worksheet**
- Create a new worksheet named "Analytics"
- Column A: List unique outlet_ids from ticket sheet
- Column B: Same-day count formula

**Step 2: Main Formula**
```excel
=SUMPRODUCT((ticket!outlet_id=A2)*(INT(ticket!created_at)=INT(ticket!closed_at))*1)
```

**Explanation:**
- `ticket!outlet_id=A2`: Matches outlet ID
- `INT(ticket!created_at)=INT(ticket!closed_at)`: Converts timestamps to dates and compares
- `*1`: Converts TRUE/FALSE to 1/0
- `SUMPRODUCT`: Sums all matches

### Alternative: Using COUNTIFS

```excel
=COUNTIFS(ticket!outlet_id, A2, ticket!created_at, ">="&DATE(2021,8,19), ticket!closed_at, "<"&DATE(2021,8,20))
```

### Result Table
```
| outlet_id      | same_day_count |
|----------------|----------------|
| wrqy-juv-978   | 0              |
| 8woh-k3u-23b   | 1              |
```

---

## 3. Outlet-wise Tickets: Same Hour Creation and Closure

### Problem
Count tickets created and closed in the same hour of the same day.

### Solution Approach

**Step 1: Create Helper Columns in Ticket Sheet**

Column F (Hour of created_at):
```excel
=HOUR(A2)
```

Column G (Hour of closed_at):
```excel
=HOUR(B2)
```

Column H (Same Hour Flag):
```excel
=IF(AND(INT(A2)=INT(B2), HOUR(A2)=HOUR(B2)), 1, 0)
```

**Step 2: Analytics Sheet Formula**
```excel
=SUMPRODUCT((ticket!outlet_id=A2)*(ticket!H:H=1)*1)
```

### Direct Formula (No Helper Columns)
```excel
=SUMPRODUCT((ticket!outlet_id=A2)*(INT(ticket!created_at)=INT(ticket!closed_at))*(HOUR(ticket!created_at)=HOUR(ticket!closed_at))*(1))
```

### Performance Considerations
- Helper column approach: Faster for large datasets (1000+ rows)
- Direct formula: Better for small datasets and easier to manage
- For very large datasets, consider using pivot tables

### Result Table
```
| outlet_id      | same_hour_count |
|----------------|-----------------|
| wrqy-juv-978   | 0               |
| 8woh-k3u-23b   | 1               |
```

### Troubleshooting
- **#VALUE! error**: Check if date columns have proper date format
- **Count too high**: Verify date comparison logic
- **Slow performance**: Consider using helper columns or pivot tables

---

## Summary of Formulas

| Task | Formula | Use Case |
|------|---------|----------|
| Lookup value | `=VLOOKUP(A2, range, 2, 0)` | Simple lookup |
| Lookup value (robust) | `=INDEX(range, MATCH(A2, lookup, 0))` | Complex scenarios |
| Conditional count | `=SUMPRODUCT((condition1)*(condition2))` | Multiple conditions |
| Date comparison | `=INT(date1)=INT(date2)` | Same day check |
| Hour comparison | `=HOUR(date1)=HOUR(date2)` | Same hour check |

---

## Excel Version Compatibility
- VLOOKUP: All versions ✓
- INDEX/MATCH: Excel 97+ ✓
- SUMPRODUCT: Excel 97+ ✓
- HOUR function: All versions ✓

## Tips & Best Practices
1. Always use absolute references for lookup tables ($A$1:$B$100)
2. Test formulas on small dataset first
3. Use named ranges for cleaner formulas
4. Document complex formulas with comments
5. Consider using Data Validation for data integrity
