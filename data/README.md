# Data Directory

This directory should contain the CSV files for case data.

## Required Files

1. **claimants.csv** - Data for cases where Chinese investors are claimants
2. **respondents.csv** - Data for cases where China is the respondent

## CSV File Structure

The CSV files should contain the following columns (case-insensitive):

- No
- Case Name
- Case Number
- Year of Initiation
- Claimant
- Claimant-mainland/HK/Macau
- Representatives for Claimant
- Arbitrator appointed by Claimant
- Respondent
- Representatives for Respondent
- Arbitrator appointed by Respondent
- President of Tribunal
- Instrument(s) Invoked
- Arbitration Rule
- Administrative Institution
- Subject of Dispute
- Status
- duration of the arbitral proceedings (Years)
- Disputing Issues
- Detail Summary
- Official Link
- Media Link 1
- Media Link 2
- Media Link 3

## Notes

- The CSV files should have headers in the first row
- Empty cells are allowed
- Links (Official Link, Media Link 1-3) will be automatically converted to clickable links
- Charts will automatically update when CSV files are modified and reloaded

