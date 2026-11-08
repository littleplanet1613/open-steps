## These moments require a skill - not optional

Invoke the skill. Do not improvise the answer in its place.

| Moment | Skill |
|---|---|
| I ask what is next, what is left, or what is blocked | `os-whats-next` |
| A material technical decision requires a user answer or a real choice of approaches | `os-ask-simple` |
| Something hard to undo is about to be agreed, or I ask what could go wrong | `os-what-could-go-wrong` |
| A concrete user action is required - run a command, enter a value locally, approve, or test on a device | `os-step-by-step` |
| I ask about other sessions, or to accept work one of them finished | `os-check-work` |
| Work is finished, or I ask how it went | `os-done-or-not` |
| I say I did not understand, ask for simpler or shorter, or paste text asking what it means | `os-say-simple` |

Never offer me options without naming a recommendation, and never recommend
something you have not screened for future cost.

### Safety gates for this fork

Verification is not authorisation.

- Never merge a pull request unless I explicitly tell you to merge it in the current task.
- Never deploy or publish to production unless I explicitly tell you to do it.
- Never delete data/resources, run a hard-to-reverse migration, make a purchase/payment,
  rotate a production secret, or make another difficult-to-undo change without my explicit approval.
- Before a hard-to-undo action, invoke `os-what-could-go-wrong` and show the verdict first.
- A previous session's report is a claim, not current proof. Re-read the real state before relying on it.
- For important work, if the relevant checks did not run after the final change, say `not checked` rather than `done`.
- Do everything safe and reversible that you can yourself before asking me to act; use `os-step-by-step` only for the irreducible user step.

Reports live in `~/.claude/open-steps/reports/<project>/`. Read `latest.md`
before re-exploring a repository you have worked in before, but verify anything
important against current state before acting on it.

### Codex 6.x routing priority

Use one primary skill per user intent: verification → `os-check-work`; concrete user action → `os-step-by-step`; decision → `os-ask-simple`; next task → `os-whats-next`; completion → `os-done-or-not`; rewrite → `os-say-simple`. Add `os-what-could-go-wrong` before consequential irreversible changes. Avoid forcing all seven on simple messages. The existing safety gates above remain binding even when no skill activates.
