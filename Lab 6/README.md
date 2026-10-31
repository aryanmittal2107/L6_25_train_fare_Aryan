
# Lab 6 – Code Coverage and Branch Coverage

## Student Details

- **Name:** Aryan Mittal
- **SRN:** PES2UG24CS089
- **Course:** Software Engineering Lab
- **Experiment:** Code Coverage and Branch Coverage using Python

## Objective

To understand and measure code coverage and branch coverage by writing Python test cases using `pytest` and measuring coverage using the `coverage` package.

## Project Structure

```text
Lab 6/
├── README.md
├── train_fare.py
├── test_train_fare.py
├── CodeCoverageTest_PES2UG24CS089_application.py
└── BranchCoverageTest_PES2UG24CS089_application.py
```

## Application Description

The train-fare application contains three functions:

- `base_fare()` – Calculates the base fare based on travel class and distance.
- `concession()` – Calculates passenger concessions based on age, gender, and Tatkal booking status.
- `tatkal_charge()` – Calculates Tatkal charges based on travel class and fare.

## Technologies Used

- Python 3
- pytest
- coverage.py

## Setup

Install the required packages:

```bash
python -m pip install pytest coverage
```

Run the existing test cases:

```bash
python -m pytest test_train_fare.py -v
```

## Code Coverage Testing

Run the code coverage test file:

```bash
python -m pytest CodeCoverageTest_PES2UG24CS089_application.py -v
```

Generate the coverage report:

```bash
python -m coverage erase
python -m coverage run --branch --source=train_fare -m pytest CodeCoverageTest_PES2UG24CS089_application.py
python -m coverage report -m
```

## Branch Coverage Testing

Run the branch coverage test file:

```bash
python -m pytest BranchCoverageTest_PES2UG24CS089_application.py -v
```

Generate the branch coverage report:

```bash
python -m coverage erase
python -m coverage run --branch --source=train_fare -m pytest BranchCoverageTest_PES2UG24CS089_application.py
python -m coverage report -m
```

## Combined Test Execution

Run both test files together:

```bash
python -m pytest CodeCoverageTest_PES2UG24CS089_application.py BranchCoverageTest_PES2UG24CS089_application.py -v
```

## Results

The combined test execution completed with **20 tests passed**.

The coverage report obtained during testing showed:

- **Statements:** 31
- **Missed statements:** 0
- **Branches:** 22
- **Partial branches:** 0
- **Reported coverage:** 100%

These results correspond to the coverage run shown during the lab work.

## Deliverables

- Code coverage test file
- Branch coverage test file
- Code coverage results screenshot
- Branch coverage results screenshot

The screenshots are submitted separately as required.

## Conclusion

The train-fare application was tested using `pytest`, and coverage was measured using `coverage.py`. Test cases were written to exercise the application's conditions and decision paths. The recorded coverage report showed 100% coverage for the measured application code.
