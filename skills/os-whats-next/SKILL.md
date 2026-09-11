---
name: os-whats-next
description: >-
  ALWAYS invoke this skill when the user asks what to do next, what is left,
  or what is blocked - "what's next", "what now", "what should we work on",
  "anything I can do" - in any language. This skill picks the next piece of
  work; when the user asks HOW to do a thing or says they do not understand
  what to do, that is os-step-by-step. Reads the last report, local changes,
  open pull requests and always the backlog. First identifies what is already
  finished and verified; a verified-ready pull request is reported as ready
  to merge but merge waits for explicit user approval. Then sorts the rest
  into doable-alone and needs-you, ending with one recommended next task in
  plain words - what it closes or unblocks. Never invents tasks.
allowed-tools:
  - "Read(~/.claude/open-steps/**)"
  - "Bash(gh pr list *)"
  - "Bash(gh pr view *)"
  - "Bash(gh pr checks *)"
  - "Bash(gh pr checks)"
  - "Bash(gh pr diff *)"
  - "Bash(gh pr diff)"
---

# os-whats-next

Answer "what do we do now" with the next move, not a map. The user does not
need the dependency graph - they need what got finished, what to take next,
and why, in plain words. This skill decides; `os-step-by-step` walks the user
through their part; `os-done-or-not` reports what came of it.

## Language

Write in the language the user speaks in this session, detected from the
conversation. Commands, file names and identifiers stay English.

## When to use

Triggers: the description above, plus a session just ended wanting a next move.

## Step 1 - read the state, quickest first

Stop as soon as you can answer.

1. **The last report** - `~/.claude/open-steps/reports/<project>/latest.md`:
   a handover written for exactly this moment.
2. **Local state** - uncommitted changes, unpushed commits, current branch.
3. **Open pull requests** - one call:
   `gh pr list --json number,title,mergeStateStatus,reviewDecision,isDraft`.
4. **The backlog - always.** The issue tracker when one is already connected
   (never authenticate or install one), otherwise task files in the repo:
   `ROADMAP.md`, `PLAN.md`, `TODO.md`, `docs/plan*`. Next work comes from the
   backlog, not from imagination. No backlog anywhere → say so.

Say which sources you did not read: an unread source is not an empty source.

## Step 2 - identify what is already finished

A pull request that looks ready is still a claim. Verify it through
`os-check-work`'s accept rules.

If the PR verifies, report it as **ready to merge**. Do not merge it in this
skill. Merge waits for an explicit user instruction in the current task, such
as "merge it", "мержи PR" or equivalent.

Requests like "what's next?", "is it ready?" or "check it" are not approval
to merge.

## Step 3 - sort what remains into two lists

| List | Belongs there when |
|---|---|
| **I can do this alone** | everything needed is at hand: no decision, no secret, no approval, no device |
| **Needs you** | a decision, an approval, a secret, a purchase, or a device only the user has |

Blocked work gets no section of its own. Fold it into the reasoning, in plain
words - "X waits on an outside check; I watch it" - the user trusts the
recommendation, not the graph.

## The shape - ten lines, like every report in this pack

```
<Lead: one sentence on where things stand - including what is verified-ready.>

**I can do alone:** <up to three items, five words of why each>
**Needs you:** <up to three items, one line each - or drop the list>

**Next I take: <the one task> - <plain words: what it closes or unblocks>.**
<One line: what was not checked.>
```

When a quick small win and a big item are both real candidates, offer the
choice with the native picker - two to four options, the recommended one first
and marked; where the picker is not available, one plain sentence. On the
pick, prepare the launch: a prompt complete enough to paste or a command
complete enough to run, one line saying what comes out - and never run a
new irreversible action yourself.

## How many at once

Before offering to start several, prove they will not collide - all three:

| Check | They collide when |
|---|---|
| Same files | both touch the same files, module, or migration sequence |
| Same shared resource | one working copy, branch, database, container project, port |
| One feeds the other | the second needs the first one's output |

Any check failing → one at a time, saying which failed. All passing → say so.
Never claim parallel safety you did not verify - "I did not check" is honest;
a collision discovered mid-run is not. Where the project isolates parallel
work - a working copy per task, separate container projects or ports - name
that as the precondition instead of assuming it.

## Hard rules

1. **Three items per list, maximum** - more → say how many were left out and
   on what basis you chose.
2. **Every item names its source** - the report, a pull request, a backlog
   entry, a failing check. Your own idea is marked a suggestion, and lists are
   never padded: two real items beat five with filler.
3. **One recommendation, always** - even when offering the small-versus-big
   choice, one option carries the mark and one line of plain-words reasoning.
4. **Verify, then prepare - never perform a new irreversible action.** A
   ready PR can be recommended for merge, but merge/deploy/delete/migration
   wait for explicit user approval.
5. **Say what you did not check** - especially the backlog. Silence reads as
   "nothing there".
6. **Plain words** - no engineering identifiers except where they name an
   action.

## Known gotchas

- Deferred-until-Monday is not a task on Saturday: do not re-propose it early.
- A stale tracker is worse than none - say when you read it.
- Draft pull requests are yours to finish, not the user's to merge.
- A needs-you pick goes to `os-step-by-step`, never explained inline.
- "Ready to merge" is still a claim until `os-check-work` verifies it.
- Verification does not equal authorisation: a verified PR still waits for an
  explicit merge command.
