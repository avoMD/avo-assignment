# Avo Engineering Assignment

## Glossary

**Prompt** — The instruction text sent to an AI model (e.g., OpenAI GPT-4).
The model's output quality depends directly on how this text is written and structured.

Example: `"Summarize the following patient information in 3 bullet points: {patient_info}"`

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

See [SUBMISSION.md](SUBMISSION.md) for requirements and how to submit.
