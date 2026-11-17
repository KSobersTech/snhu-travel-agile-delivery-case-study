# SNHU Travel Agile Artifact Examples

## Purpose

These examples show how I would turn the SNHU Travel scenario into delivery-ready Agile artifacts. They are illustrative working documents for portfolio review, not records from a deployed commercial product.

## Example Product Goal

Help travelers narrow a broad set of vacation options into relevant choices using preferences they understand and can revise.

## Example Refined User Story

**Story**

> As a budget-conscious traveler, I want to filter trips by a minimum and maximum price so that I can focus on options within my planned spending range.

**Customer value**

The traveler can remove irrelevant results and compare options they can realistically consider.

**Acceptance criteria**

```gherkin
Scenario: Filter trips within a valid price range
  Given available trips have different prices
  And the traveler enters a minimum price of 1000
  And the traveler enters a maximum price of 2500
  When the traveler applies the price filter
  Then only trips priced from 1000 through 2500 are displayed
  And the active price range remains visible

Scenario: Reject a reversed price range
  Given the traveler enters a minimum price greater than the maximum price
  When the traveler applies the price filter
  Then the results are not updated
  And the traveler is told how to correct the range

Scenario: Explain an empty result
  Given no available trips match the valid price range
  When the traveler applies the price filter
  Then an empty-state message is displayed
  And the traveler can revise or clear the filter
```

**Questions to resolve before implementation**

- Are price boundaries inclusive?
- Which currency is displayed and stored?
- Can either boundary be left blank?
- How are taxes and fees represented?
- Should changing another filter preserve the price range?

These questions show why a story statement alone is not enough to begin implementation.

## Example Test Case

| Field | Example |
|---|---|
| Test case | Valid price range filters results |
| Related story | Filter trips by minimum and maximum price |
| Preconditions | Trips exist below, inside, and above the requested range |
| Test data | Minimum 1000; maximum 2500 |
| Action | Apply the price filter |
| Expected result | Only trips priced from 1000 through 2500 appear; the active range remains visible |
| Boundary follow-up | Verify that results priced exactly 1000 and 2500 follow the agreed rule |

## Definition of Ready

A story is ready for sprint planning when:

- The user and value are clear.
- Acceptance criteria describe observable behavior.
- Important business rules and error states are defined.
- Dependencies and open questions are visible.
- The story is small enough to complete and demonstrate within a sprint.
- The team understands how the behavior will be tested.

Readiness is a shared-understanding checkpoint, not a guarantee that the story will never change.

## Definition of Done

A story is done when:

- Acceptance criteria are satisfied.
- Relevant unit, integration, and manual checks are complete.
- Validation, empty states, and important boundaries are handled.
- Code or deliverables have been reviewed.
- Accessibility and usability have been considered for the changed journey.
- Documentation is updated when behavior or maintenance expectations change.
- No unresolved critical defect blocks release.
- The increment can be demonstrated.
- Follow-up work is recorded explicitly rather than hidden inside the completed story.

## Example Change Decision

Suppose feedback shows that cruise travelers need cabin preferences in addition to destination filters.

| Decision question | Response approach |
|---|---|
| Is this required to satisfy an active story? | Compare the request with current acceptance criteria |
| Does it threaten the sprint goal? | Assess the added behavior, data, design, and testing work |
| Who decides priority? | Product Owner, using customer value and current commitments |
| How is the decision recorded? | Refine an active story only if it is clarification; otherwise create and prioritize a new backlog item |
| How is the team informed? | Update the backlog and communicate the scope decision before implementation continues |

## Retrospective Action Plan

| Direction | Action | Owner | Evidence in the next sprint |
|---|---|---|---|
| Keep | Test against acceptance criteria during development | Developer and Tester | Test evidence is linked before the story is demonstrated |
| Start | Hold a brief review for stories with unresolved behavior | Product Owner, Developer, and Tester | Open questions are answered or explicitly tracked before work starts |
| Stop | Waiting until the Sprint Review to disclose blockers | Person who discovers the blocker | Blockers are raised when discovered and reflected on the task board |

The goal is not more ceremony. It is to resolve uncertainty while the team still has options.

## Sprint Review Checklist

- The behavior can be demonstrated from the customer's perspective.
- Each acceptance criterion has evidence.
- Known limitations and incomplete work are visible.
- Feedback can be captured as a clear backlog decision.
- The demonstration supports the sprint goal instead of listing unrelated activity.

Read the [full case study](agile-delivery-case-study.md) or return to the [repository overview](../README.md).


