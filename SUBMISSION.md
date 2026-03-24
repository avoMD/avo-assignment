# Submission Guide

Please include the following in your submission:

---

## 1. Problem Definition (½ page max)

- What is the actual problem you're solving?
- What are you explicitly **not** solving, and why?
- What assumptions did you make?

---

## 2. Working Implementation

- `docker compose up --build` must run without errors
- Core flow must work end-to-end
- Tests pass: `docker compose exec web python manage.py test`

---

## 3. Decision Log (bullet points)

- Key design decisions and why you made them
- What you considered but decided against

---

## 4. AI Usage Log

- What tasks you used AI for
- Where you made the call yourself and why

---

## How to Submit

1. Create a **public** GitHub repository
2. Reply to this email with the repository link

Make sure `.env` is in `.gitignore` and your OpenAI API key is not committed.
