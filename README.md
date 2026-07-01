# Avo Engineering Assignment

Thank you for taking the time to work on this. We genuinely appreciate it.

This assignment is based on a real problem we've faced building our product — so as you work through it, you'll get a feel for the kind of problems we think about every day. We hope it's interesting, not just as a test, but as a small window into what it's like to work here.

There's no trick. We're looking forward to hearing how you approached it.

---

**Expected time: 3 hours.** You're encouraged to use AI tools (Cursor, Claude, etc.) — just log how in [WRITEUP.md](WRITEUP.md).

To save your time, the following are **explicitly out of scope** — please don't build them:

- **UI** — API only. No frontend, no templates.
- **Swagger / API docs** — not required.
- **Auth / RBAC** — no login, sessions, or permission enforcement.
- **OpenAI key management** — we won't provide an API key; mock the LLM call or use a placeholder response.

What we're actually evaluating is how you think: the decisions you make, what you choose not to build, and where your judgment shaped the output. A clear [WRITEUP.md](WRITEUP.md) matters.

Common time traps to avoid:

- **Scope creep** — define what you're _not_ doing in [WRITEUP.md](WRITEUP.md) early and move on
- **Written deliverables** — bullet points are enough; we're not grading prose

---

## Context

We build AI-powered clinical tools. Our backend makes OpenAI API calls in several places — document summarization, checklist generation, note writing, and more.

Here's one example of how a prompt currently lives in the codebase — this is just a subset of the full system:

```python
SUMMARIZE_PROMPT = """You are a medical documentation assistant.
Summarize the following patient information into 3 concise bullet points.
Focus on: chief complaint, key findings, and plan.

Patient information:
{patient_info}"""

def summarize(patient_info: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": SUMMARIZE_PROMPT.format(patient_info=patient_info)}],
    )
    return response.choices[0].message.content
```

We have about a dozen prompts like this across the codebase, each serving a different purpose:

- Summarizing patient information
- Generating clinical checklists
- Writing discharge notes
- Extracting key findings from lab results
- Drafting referral letters
- …and more

---

## The Problem

Our clinical content team writes and refines prompts — but they are not engineers.

Right now, every time they want to improve a prompt, test a new version, or roll back a change that made output worse, they have to ask an engineer to edit the code and deploy. This creates a bottleneck: the feedback loop is slow, experimentation is risky, and the team that best understands the clinical content has no direct control over it.

---

## What to Do

Build a solution to the problem above. At minimum, an API that lets the content team manage prompts without touching code — but scope and design decisions are yours to make and justify.

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for deliverables and how to submit.

---

_v1.3_
