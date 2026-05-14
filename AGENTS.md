# Workspace Skills

## Skills
A skill is a set of local instructions stored in a `SKILL.md` file.

### Available skills
- `sdoc`: Generate a Chinese architecture-reading Markdown document for a source file or module using the local `sdoc` tool. Use when the user asks with `/sdoc`, asks for structured code documentation, or wants a generated walkthrough saved next to the source. (file: `/config/workspace/.codex/skills/sdoc/SKILL.md`)

### How to use skills
- If the user names a skill, including `/sdoc` or `sdoc`, open that skill's `SKILL.md` and follow it.
- Resolve relative paths from the workspace root unless the skill says otherwise.
- Load extra files only when needed.
