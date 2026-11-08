# Codex 6.x compatibility review — 2026-11-09

Scope: seven Open Steps skills, routing block, safety constraints and documentation.

Routing precedence:
1. Independent verification of work from elsewhere: os-check-work.
2. A concrete user-side step: os-step-by-step.
3. A necessary technical decision: os-ask-simple.
4. What is left / next: os-whats-next.
5. Wrap-up of substantial work: os-done-or-not.
6. Rewrite existing text: os-say-simple.
7. Hard-to-reverse decision: os-what-could-go-wrong as an additional safety gate.

The routing boundaries are targeted at reducing false triggers on stronger models. They are **not** evidence of a measured improvement. The existing eval corpus measures Claude, not current Codex 6.x model activation. Run new headless activation evaluations when a suitably authenticated Codex CLI is available.

Safety is unchanged: never merge, deploy, delete production resources, pay, rotate credentials or perform irreversible migrations without explicit user approval. Never put secrets in chat. Prior agent reports do not establish passed tests. Preserve original Claude Code hooks and routing behavior where possible.

Compatibility checklist:
- Codex CLI >= 0.153.0 for GPT-6 Astra in the companion orchestrator repository.
- Confirm each requested model is accessible to the signed-in account; plan availability is not inferred from model naming.
- Place skill folders in `~/.agents/skills/`, and append the routing block to `~/.codex/AGENTS.md` only after reviewing existing instructions.
- Do not overwrite `~/.codex/config.toml` or MCP configuration.
- Run `bash hooks/test.sh` for hook integration, `python3 -m py_compile evals/score.py` for scorer syntax and Codex activation tests separately.
- CI failures for DCO Signed-off-by must be resolved by an authorized human contributor rather than fabricating their signature.
