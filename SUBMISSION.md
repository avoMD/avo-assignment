# Avo Engineering Assignment — Submission Guide

---

## 1. Problem Definition → `PROBLEM.md`

Before writing any code, fill in `PROBLEM.md`:

- What is the actual problem you're solving?
- What are you explicitly **not** solving, and why?
- What assumptions did you make?

---

## 2. Working Implementation

Your task is to design and build a solution to the problem described in the README.

At minimum, build an API that lets someone manage prompts without changing code. What else is needed is up to you — define and justify your scope in `PROBLEM.md`.

- **Tech stack**: Python + Django (preferred). If you're not comfortable with Python, TypeScript + NestJS/Express is fine.
- Create a new project from scratch
- `docker compose up --build` as the single entry point
- **`docker compose up --build` must run without errors, and all tests must pass**

We'll provide an OpenAI API key for the GPT calls.

---

## 3. Decision Log → `DECISIONS.md`

- Key design decisions and why you made them
- What you considered but decided against

---

## 4. AI Usage Log → `AI_USAGE.md`

- You are expected to use AI tools (Cursor, Claude, etc.)
- What tasks you used AI for
- Where you made the call yourself and why

---

## 5. How to Submit

1. **Create a private repository on your own GitHub account.**
   - On this template repo page, click **"Use this template" → "Create a new repository"**.
   - Set the owner to **your own account** and the visibility to **Private**.
2. **Complete the assignment** in your new repository (all items above).
3. **Push your work to the `main` branch.**
4. **Invite our reviewer as a collaborator.**
   - In your repo: **Settings → Collaborators → Add people** → invite **`yunho-ju`**.
5. **Email us** once you're fully done so we can begin the review.

> Please keep the repository **private**. Make sure `.env` is in `.gitignore` and your OpenAI API key is never committed.

---

## Notes

- No right answer. We're interested in how you think.
- We'll walk through your submission together in a 30-40 min follow-up call.
