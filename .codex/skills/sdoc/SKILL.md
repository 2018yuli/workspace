---
name: sdoc
description: Generate a Chinese architecture-reading Markdown document for a source file or module using the local sdoc tool. Use this when the user asks with `/sdoc`, asks to explain a code file as structured documentation, or wants a generated source walkthrough saved next to the code.
---

# sdoc

Use this skill when the user wants a structured source-documentation pass for an existing file.

## What to do

1. Treat the user argument as a repository-relative source path.
2. Verify the target file exists and infer the project root from the current workspace unless the user provides one.
3. Prefer the local CLI:

```bash
sdoc generate <relative-path> --project-root <repo-root>
```

4. If the user wants config details, run:

```bash
sdoc print-config <relative-path>
```

5. Report the generated Markdown path and summarize the important findings.

## Notes

- The skill is offline-first and reads nearby source, README files, and project manifests.
- Default config lives in `.codex/skills/sdoc/sdoc.toml` for this workspace.
- For behavior and capabilities, consult `.codex/skills/sdoc/README.md` only when needed.
