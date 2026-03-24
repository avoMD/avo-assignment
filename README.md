# Senior Engineer Take-Home Challenge

## Glossary

**Prompt** — The instruction text sent to an AI model (e.g., OpenAI GPT-4).
The model's output quality depends directly on how this text is written and structured.

Example: `"Summarize the following patient information in 3 bullet points: {patient_info}"`

---

## Context

We build AI-powered clinical tools. Our backend makes OpenAI API calls in several places — document summarization, checklist generation, note writing, and more.

Right now, every prompt lives directly in the code. Take a look at `summarize/service.py`:

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

We have about a dozen prompts like this across the codebase.

**The problem:** When a prompt produces poor output, we edit the string, open a PR, wait for review, and deploy. The feedback loop is slow. Sometimes we deploy a "fix" that makes things worse, and rolling back means another deployment.

---

## What We'd Like You to Do

We want to move prompts out of the code. That's the direction — how you get there is up to you.

**Before writing any code, define the problem.** What specifically needs to be solved? What doesn't? What assumptions are you making?

Then build a thin working slice that proves your approach.

---

## Getting Started

```bash
cp .env.example .env
# Add your OPENAI_API_KEY to .env

docker compose up --build
```

Run tests:
```bash
docker compose exec web python manage.py test
```

---

## Deliverables

See [SUBMISSION.md](SUBMISSION.md) for details.

---

## Time Box

**2 hours.** We mean it — we're evaluating judgment, not completeness.

Partial is fine if you explain what's missing and why.

---

## Notes

- No right answer. We're interested in how you think.
- You are expected to use AI tools (Cursor, Claude, etc.). Document how.
- We'll walk through your submission together in a 30–40 min follow-up call.
