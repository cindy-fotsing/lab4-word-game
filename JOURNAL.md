### **New Interaction**
- **Date**: 03-12-2026 14:38
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: Update the journal with the latest testing interactions
- **CoPilot Mode**: Edit
- **CoPilot Model**: Claude Sonnet 4.6
- **Changes Made**: Reconciled recent conversation turns against `JOURNAL.md`; backfilled the missing README interaction and prepended this current journal-update entry.
- **Context and Reasons for Changes**: User requested journal update. Two missing entries identified: README authoring and this current prompt.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 14:38
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: The file should explain how to run the game and the tests.
- **CoPilot Mode**: Edit
- **CoPilot Model**: Claude Sonnet 4.6
- **Changes Made**: Populated the empty `README.md` with setup instructions (virtual environment + pytest install including execution-policy fix), commands to run the game and the tests (verbose and quiet modes), and a project structure overview.
- **Context and Reasons for Changes**: User wanted `README.md` to document how to run the game and the test suite. No prior content existed in the file. Entry backfilled during reconciliation.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 14:08
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: using powershell, help me to install the pytest. step by step
- **CoPilot Mode**: Ask
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Provided step-by-step PowerShell commands to install `pytest` in a virtual environment, including activation and verification commands with a common execution-policy fallback.
- **Context and Reasons for Changes**: User asked for guided installation using PowerShell. Reconciliation was performed against the top section of `JOURNAL.md`; no additional in-scope missing prompts were detected before prepending this entry.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 14:00
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: yes sure
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Created `tests/test_main.py` with nine focused pytest test cases covering correct/wrong guesses, invalid input, duplicate guesses, lives boundaries, already-won behavior, normalization, and non-alphabetic secret-word handling.
- **Context and Reasons for Changes**: User confirmed they wanted the proposed tests implemented. Added executable tests for `update_game_state` and verified there were no analysis errors in both `main.py` and `tests/test_main.py`.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 14:00
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: Can you suggest tests for this function?
- **CoPilot Mode**: Ask
- **CoPilot Model**: GPT-5.3-Codex
- **Changes Made**: Proposed a concise, high-value test matrix covering normal flow, invalid input, repeated guesses, boundary conditions, normalization, and non-alphabetic word edge cases.
- **Context and Reasons for Changes**: User asked for suggested tests before implementation. No files were modified in that interaction; entry was backfilled during reconciliation.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 13:49
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: update the journal with the latest interactions
- **CoPilot Mode**: Edit
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Reconciled recent code-review and documentation interactions against `JOURNAL.md` and prepended four missing Edit/Ask entries from this session before prepending this current journal-update request.
- **Context and Reasons for Changes**: User requested journal update. Backfilled missing interactions: function review iterations with input validation, normalization, win-state checks, lives clamping; return signature expansion to include feedback messages; and module/function documentation with docstrings.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 13:49
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: Can you review and document main.py? Do not be too verbose and skip the trivial
- **CoPilot Mode**: Edit
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Added module docstring and comprehensive function docstring to `update_game_state()` covering normalization behavior, win-condition logic (alphabetic-only filtering), and state-update guarantees.
- **Context and Reasons for Changes**: User requested lightweight documentation. Added docstring with focus on non-obvious behavior: that guessed_letters updates only on correct guesses, and that win-detection filters to alphabetic characters only.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 13:49
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: i changed it, can you tell me if it is okay ?
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Reviewed updated `update_game_state()` function with win-state detection (`required_letters <= set(guessed_letters)`), input validation, and normalization. Confirmed correctness; flagged minor edge case for non-alphabetic-only words.
- **Context and Reasons for Changes**: Function passed to solid state (no syntax errors, all major bugs fixed); flagged non-alphabetic characters in secret_word as an edge case (minor, acceptable for typical use cases).
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 13:49
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: I have made some changes, review my code and tell me
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Reviewed third version with `required_letters` set comprehension for win detection, `strip()` reintroduced, and `guessed_letters` normalization on every call.
- **Context and Reasons for Changes**: User added alphabetic-only filtering for win conditions and restored whitespace handling. Identified residual risk: repeated guesses with normalized incoming duplicates (e.g., ["A"] and guess "a"), though not currently breaking.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 13:49
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: I have made some changes, review my code and tell me
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Reviewed second version with `lives <= 0` early guard, return-signature expansion to `tuple[list[str], int, str]` for feedback messages, and message text on each exit path.
- **Context and Reasons for Changes**: User added feedback messages and output status strings. Identified remaining issues: mixed-case normalization inconsistency and missing win-state check. No code modified in this turn.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 13:49
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: I have made some changes, review my code and tell me
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Reviewed first refactored version with early guards, extended return type, and input validation. Flagged medium issues: incomplete normalization of incoming `guessed_letters` and lacking whitespace handling from `guess`/`secret_word`.
- **Context and Reasons for Changes**: Initial review of improved implementation; provided feedback for next iteration targeting normalization consistency and win-state detection.
- **My Observations**:

### **New Interaction**
- **Date**: 03-12-2026 11:46
- **User**: cindy.gangne-fotsing@epita.fr
- **Prompt**: I've started implementing a guess the word game (hangman). Can you review my `update_game_state` function?
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Initial code review of `update_game_state()` function. Identified high-priority bug (substring matching instead of single-letter validation), medium issues (lives underflow, case/whitespace normalization), and low-priority gap (no game_state tracking for finished rounds).
- **Context and Reasons for Changes**: User presented first implementation; provided comprehensive review with four categories of findings and suggested test cases. No code was modified in this turn.
- **My Observations**:

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

