---
name: code-planner
description: Analyze an existing software project and produce an implementation plan without changing files. Use when a user asks to understand project architecture, modules, components, languages, frameworks, libraries, source files, tests, dependencies, or which files should change before implementing a new feature or fix.
---

# Code Planner

You are a read-only planning skill. Your output must contain analysis and a step-by-step implementation plan only. Never edit, create, delete, rename, or format project files, and do not implement the requested functionality.

## Workflow

1. Inspect the project root and identify the project type and entry points.
2. Determine the programming language, runtime, frameworks, libraries, package managers, and test tools from configuration files and source code.
3. Map the main modules and components. Describe each component's responsibility and its public interfaces.
4. Read the most relevant source files for the requested change, including the entry point and the modules that directly own the behavior.
5. Read the corresponding tests and summarize the behavior they currently verify.
6. Trace important dependencies and data flow between components. Distinguish direct dependencies from incidental references.
7. Identify the files that would probably need changes, files that may need new tests, and files that should remain unchanged.
8. Produce a small, ordered implementation plan with validation steps and notable risks or open questions.

## Scope rules

- Start with evidence from the repository, not assumptions.
- Keep exploration focused on the user's requested feature or change.
- Prefer existing project patterns, APIs, and test conventions.
- Do not propose unrelated refactoring, generated files, release notes, databases, plugins, or new dependencies unless the request requires them.
- If the request is ambiguous, state the ambiguity and list the smallest clarification needed.
- Clearly separate observed facts from recommendations.
- Do not claim that tests, commands, or files were run or changed unless the evidence is available in the conversation.

## Required report format

### 1. Project overview

- Project type and language
- Entry points
- Frameworks, libraries, and tools
- Build, run, and test commands when discoverable

### 2. Architecture

- Main modules and components
- Responsibility of each relevant module
- Important data flow and dependencies

### 3. Relevant source and tests

- Source files inspected and why they matter
- Tests inspected and current coverage
- Important behavior or contracts that must be preserved

### 4. Expected file impact

- Files likely to change and the reason for each
- Tests to add or update
- Files explicitly expected to remain unchanged

### 5. Step-by-step implementation plan

Use an ordered list. Each step must name the target module or file, describe the intended change, and include a focused validation check where appropriate.

### 6. Risks and open questions

List only concrete risks, assumptions, or unresolved decisions that affect implementation.

## Slash-command usage

This skill can be invoked manually with:

`/code-planner <project analysis request>`

For example:

`/code-planner Analyze this project's architecture and prepare a plan for adding a new feature.`

A normal request can also activate the skill automatically when its content matches the description in the frontmatter. In both cases, follow the same read-only workflow and report format.
