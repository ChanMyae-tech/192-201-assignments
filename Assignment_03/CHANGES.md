# Assignment 03 — CHANGES

**Name:** Chan Myae Thaw Tar  **Student ID:** 6705140048

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
| 1 |Products were stored as bare tuples|I created a Product class with name, price, and category| Classes / Encapsulation| Ran python Assignment_03.py → PASS |
| 2 | Order items used product indexes and quantities together | Created an OrderItem class containing a product and quantity | Composition / Encapsulation | Ran the behavior self-test → PASS |
| 3 | Repeated if/elif conditions were used for membership discounts and points | Created Customer subclasses: SilverCustomer, GoldCustomer, and PlatinumCustomer | Inheritance / Polymorphism  | Ran the behavior self-test → PASS |
| 4 | Calculations and printing were mixed together in the original program | Created separate methods such as subtotal(), tax(), discount(), total(), and points(). The receipt() method builds the receipt text | Encapsulation / Separation of responsibilities | Compared the output with the legacy program → PASS |
| 5 | Magic numbers and invalid data were not clearly managed | Created named constants and added validation in constructors | Encapsulation / Validation | Ran python Assignment_03.py → PASS |

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original                                                  | What I changed it to                                                                                                                            | OOP concept applied                            | How I verified behaviour was unchanged             |

| 1 | Products were stored as bare tuples                                         | I created a `Product` class with `name`, `price`, and `category`                                                                                | Classes / Encapsulation                        | Ran `python Assignment_03.py` → PASS               |
| 2 | Order items used product indexes and quantities together                    | Created an `OrderItem` class containing a product and quantity                                                                                  | Composition / Encapsulation                    | Ran the behavior self-test → PASS                  |
| 3 | Repeated `if/elif` conditions were used for membership discounts and points | Created `Customer` subclasses: `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer`                                                         | Inheritance / Polymorphism                     | Ran the behavior self-test → PASS                  |
| 4 | Calculations and printing were mixed together in the original program       | Created separate methods such as `subtotal()`, `tax()`, `discount()`, `total()`, and `points()`. The `receipt()` method builds the receipt text | Encapsulation / Separation of responsibilities | Compared the output with the legacy program → PASS |
| 5 | Magic numbers and invalid data were not clearly managed                     | Created named constants and added validation in constructors                                                                                    | Encapsulation / Validation                     | Ran `python Assignment_03.py` → PASS               |


## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?
"My reflection"
The best change to improve the code was the customer subclasses for the different membership tiers. They all have different rules for discounts and points. This allows for polymorphism, so you don’t have to reiterate the same conditions for each tier in the program. In addition, the new classes Product and OrderItem make the data much clearer and easier to handle. As mentioned before, I was careful to keep the behavior identical, i.e. the same receipt format, same calculation order, and rounding as before. I tested the code by running python Assignment_03.py and the behavior test displayed PASS.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
| 1 | Help me understand the assignment requirements and how to start the refactoring | Explained the requirements and suggested creating classes step by step | Accepted and edited while coding | Read the assignment instructions and checked each step |
| 2 | Explain how to create an OrderItem class and validate the product and quantity | Suggested composition using a Product object and quantity validation | Accepted | Read every line and ran the behavior test |
| 3 | Explain inheritance and polymorphism for customer membership tiers | Suggested a base Customer class and Silver, Gold, and Platinum subclasses | Edited and accepted |  Checked the discount and points behavior |
| 4 | Explain how to create the Order class and its calculation methods | Suggested methods for subtotal, tax, discount, total, and points | Accepted and edited | Read every method and ran the behavior self-test |
| 5 | Explain how to create the receipt method and preserve the original output format | Suggested building receipt text using a list and returning a string | Edited | Compared the receipt format with the legacy output |
**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [ yes ] `python Assignment_03.py` prints **PASS**.
- [ yes ] No tuples / parallel lists left — products, orders, and items are objects.
- [ yes ] No `if tier == ...` chains — tiers are a class family.
- [ yes ] Calculation methods **return** values and do not `print`; printing is separate.
- [ yes ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ yes ] The change table and reflection above are filled in.
- [ yes ] The prompt log is complete and the ownership statement is signed.
