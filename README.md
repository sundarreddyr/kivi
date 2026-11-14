# Kivi

A household memory and chore assistant, starting in Bengaluru kitchens. Kivi is the working name. In Kannada, *kivi* means “ear” — a fitting name for a home that can listen when someone has a free moment and remember when it is time to act.

Imagine opening the door for the cook at 8 am. One partner is half asleep, yesterday’s dal is still in the fridge, and breakfast depends on whether anyone bought batter. The household has most of the answers, but they belong to different people and arrive at different times. Kivi’s goal is to give the cook a workable plan and give the family their morning back.

## First project

Turn everyday kitchen updates into attributable, correctable records in MySQL. Start with a voice note and carry it through to a stored record. Use typed transcripts as a control to isolate interpretation errors. Extend coverage to native scripts, transliterated words and mixed languages through the same application boundary. WhatsApp is the intended everyday channel for the cook. Before an action involving money, fetch the latest applicable state and reconcile it with the merchant cart.

Today this repository contains a Maven skeleton and engineering documents. The first project is a design brief. Database models, extraction, speech, messaging and ordering are future work.

## Problems worth exploring

| Household problem | What success would look like |
| --- | --- |
| Breakfast and lunch are decided while the cook waits | The cook arrives knowing what to prepare, for whom and in what portions. |
| Both partners say “anything”, then reject yesterday’s dosa | Meal suggestions account for recent meals, mood, dietary preferences, balance and what the cook can prepare. |
| People remember groceries at odd times | “Get eggs tomorrow” survives until the chosen ordering time. A question about eggs does not create a purchase. |
| Stock is approximate or stale | “Batter enough for tomorrow” remains an observation with a reporter and time. Ask about it when freshness changes a decision. |
| Leftovers are forgotten, duplicates bought, food wasted | Meals use reported portions and account for goods someone already picked up. |
| Guests arrive, children’s plans change, someone eats out | Revise the affected meal and pending purchases. Preserve which earlier decision changed. |
| The cook takes leave or misses a message | The household learns which plan was acknowledged and can arrange an alternative in time. |
| Cooks work in multiple homes and households speak different languages | The right household receives the update with minimal typing, including from WhatsApp voice notes. |
| Parents, children, cook and maid make overlapping requests | Tell suggestions, observations, approvals, corrections and fulfilment apart. Ask a short question when a conflict affects the outcome. |
| Last-minute changes arrive near checkout | Recheck the latest state, respect household spending limits, preserve unrelated cart items and capture the merchant’s actual outcome. |
| The family needs help beyond the kitchen | Explore cleaning, household supplies, reminders and later a shared voice controller. Timers or kitchen entertainment can use the same interface. |

## How we judge the idea

Compare one-pass chat, Kivi and direct app use on the same household day. Measure wrong purchases, missed corrections, questions, human time and actual token usage. Attribute transcription, intent extraction, household rules and merchant failures separately. A reliable result with more household effort is a poor trade.

## Start here

- [Voice-to-record design](docs/specs/002-voice-to-record.md) follows a cook’s note through capture, correction and read-back.
- [Architecture](ARCHITECTURE.md) describes the module boundaries.
- [Agent guide](AGENTS.md) explains how to work in this repository.
- [Project memory](docs/STATUS.md) records the current handoff and open decisions.
- [First project brief](docs/specs/001-kitchen-capture.md) defines the scenario and future acceptance criteria.
- [Harness and project map](docs/README.md) explains where decisions and plans live.

## Local development

Use JDK 21 and Maven 3.9+. Run `python3 scripts/check.py` for the repository checks and `mvn verify` from the root for the Java build. Neither command needs a configured database or model key. Maven needs dependency access or a populated cache.
