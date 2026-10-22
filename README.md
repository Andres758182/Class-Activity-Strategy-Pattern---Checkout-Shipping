# Strategy Pattern — Checkout Shipping (Starter)

Use this repository as the starting point for the Strategy Pattern class activity.

## Current behavior

`Checkout` currently supports:

- **Standard** — free for subtotal >= 1000; otherwise 49.
- **Express** — 99 + 12 per kilogram.
- **Pickup** — 0.

A new **Same Day** option is required:

- 149 + 18 per kilogram.

## Your task

Refactor the starter code using the **Strategy Pattern** and object-oriented Python.

1. Create an abstract `ShippingCostStrategy`.
2. Implement:
   - `StandardShipping`
   - `ExpressShipping`
   - `PickupShipping`
3. Make `Checkout` receive a `ShippingCostStrategy` object and delegate the calculation.
4. Add `SameDayShipping` with 149 + 18 per kilogram.
5. Add or update unit tests.
6. Confirm that `SameDayShipping` can be added **without modifying `Checkout`**.

### Course constraint

Use classes and objects. Do **not** implement the strategies as standalone functions, lambdas, callbacks, or other functional-programming alternatives.

## Repository setup

If working in a pair/team, **one person** creates the working repository from this starter/template. Everyone else clones that same repository.

The working repository must be **public**.

## Local setup

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

The starter repository should begin green.

## Submission

Submit the public repository URL plus a short answer identifying:

- what **varies**,
- what **stays stable**,
- one **complexity cost** introduced by Strategy.

## Evaluation — 10 credits

- Correct Strategy structure — **4**
- Correct shipping behaviors, including Same Day — **3**
- Tests — **2**
- Design explanation — **1**

A Possible Solution / Reference Implementation will be shared after submissions close.
