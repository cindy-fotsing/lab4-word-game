### **New Interaction**
- **Date**: 03-12-2026 11:46
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: Update the journal with the recent interactions
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Reconciled the recent conversation against `JOURNAL.md` and prepended the missing in-scope Ask interactions, then logged this current journal-update request.
- **Context and Reasons for Changes**: User explicitly requested a journal update. Reconciliation was performed inline against the top 250 lines of `JOURNAL.md`; missing recent prompts were backfilled in order before prepending this current interaction.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 11:46
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: What are possible bugs in Word Guess / Hangman implementations
- **CoPilot Mode**: Ask
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Provided a concise bug catalog covering input validation, repeated guesses, case handling, win/loss transitions, state-reset issues, and display/loop edge cases.
- **Context and Reasons for Changes**: Answered a conceptual design/debugging question for Hangman behavior; no code files were modified in that turn. Entry backfilled during reconciliation.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 11:46
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: What are the rules and invariants?
- **CoPilot Mode**: Ask
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Defined gameplay rules (input handling, guess outcomes, transitions to win/loss) and core invariants (bounded lives, valid state set, consistency constraints).
- **Context and Reasons for Changes**: Clarified the difference between rules and invariants for the user's Hangman notes; no code changes were required. Entry backfilled during reconciliation.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 11:46
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: What variables should I keep track of ?
- **CoPilot Mode**: Ask
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Recommended a minimal variable set (`secret_word`, `guessed_letters`, `lives_remaining`, `game_state`) and distinguished derived values from stored state.
- **Context and Reasons for Changes**: Responded to a data-model question for a Hangman app state design; no file edits were made in that turn. Entry backfilled during reconciliation.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 11:46
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: What states does a Word Game like Hangman game need?
- **CoPilot Mode**: Ask
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Suggested the core game states (`start/idle`, `playing`, `won`, `lost`) and clarified that invalid input is typically an event handled during `playing`, not a separate state.
- **Context and Reasons for Changes**: Answered a conceptual modeling question to help structure `MY_NOTES.md`; no code changes were made in that turn. Entry backfilled during reconciliation.
- **My Observations**:

### **New Interaction**
- **Date**: 03-09-2026 11:54
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: Implement a recursive fibonacci function in main.py
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Added a recursive `fibonacci(n)` implementation to `lab4-word-game/main.py` with base cases and non-negative input validation, plus a small `main()` example call.
- **Context and Reasons for Changes**: Implemented directly to satisfy the user request. Reconciliation was performed against the top 250 lines of `lab4-word-game/JOURNAL.md`; no in-scope missing interactions were detected before prepending this current entry.
- **My Observations**:

### **New Interaction**
- **Date**: 03-09-2026 11:50
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: In this lab4-word-game folder, read the copilot-instructions.md file and follow its directives. Activate the journal agent in journal-logger.agent.md
- **CoPilot Mode**: Agent
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Read lab4 custom instructions and journal agent directives; attempted to invoke `journal-logger` agent directly; direct activation was unavailable in the registered agent list, so applied the same reconciliation and logging workflow inline and updated this journal entry.
- **Context and Reasons for Changes**: Required to follow `lab4-word-game/.github/copilot-instructions.md` and activate journaling. Reconciliation was performed against the top 250 lines of `lab4-word-game/JOURNAL.md`; no prior interaction entries were found in scope to backfill, so this current interaction was prepended as newest.
- **My Observations**:

# This JOURNAL.md file gets automatically updated by the journal-logger agent after every interaction with CoPilot. It serves as a comprehensive log of all prompts, responses, changes made, and reflections during the development process. Each entry is formatted consistently for easy reading and is listed in reverse chronological order, with the most recent interactions at the top.

