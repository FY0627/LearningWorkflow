# Approval Panel Template

Loaded by `human-approval` at Workflow step 7 when a gate has triggered.

## Output layout

Render a review subject above a table. Translate the subject, headers, options, and
consequences into the operator's language. Keep commands and paths literal.

```text
Stopped: [actual objects and actions awaiting a decision]

| Option | Consequence | Undo |
|---|---|---|
| A. [direct action] | [outcomes, irreversible part, accepted risk] | [concrete undo or —] |
| B. [create recovery first, then act, when feasible] | [outcomes and recovery conditions] | [concrete undo] |
| C. [do not proceed] | [what remains unchanged] | [applicable undo or —] |
```

The cells above are slots, not wording to copy. One row represents one option, not a separate
approval for its consequences. Selecting its identifier is sufficient for its disclosed scope.
Determine each cell from the option's actual effects. Neither "no undo" nor a backup command
is a default answer to copy from a template or example.

## Content rules

- The subject names what will actually be touched. If it differs from the request, disclose
  the wider, narrower, or changed target. Do not silently substitute a different object.
- Every option covers its entire action list, including supporting actions and lower-tier
  changes bundled with the action that opened the gate. Undisclosed actions are not authorized.
  Name the full scope in the subject, and account for each action in every option's consequence
  and undo cells. Mentioning a supporting action only in the subject is insufficient. An option
  that omits an action must explicitly leave it unchanged, not silently hide its effects.
- Use separate option, consequence, and undo columns. Only options receive identifiers.
  Do not repeat an identifier in separate consequence and undo paragraphs.
- Use an em dash in the undo cell when nothing can or needs to be undone. Consequences must
  distinguish permanent loss from no change; the dash alone does not explain that difference.
- For mixed actions, identify the irreversible part and provide commands for the recoverable
  part. Never replace a partly available undo with a dash for the whole option.
- Include a do-not-proceed option. Offer direct action and, when feasible, recovery preparation
  followed by action. Choose a concrete backup destination and check it will not overwrite
  existing content. Do not omit recovery just because the agent thinks copying is not worthwhile.
  Do not promise a backup despite known space, permission, or consistency obstacles. If recovery
  cannot be prepared, state the limitation briefly. A copy of a message does not undo sending it.
- Consequences state facts and risks, not advocacy. Do not add a paragraph repeating the request.
- Keep implementation details outside the panel except the concrete recovery choice and undo
  commands needed for an informed decision. Do not print internal tier numbers.
- Within one requested object, summarize scale when checked. Independently chosen extra work
  remains separately visible; do not hide it inside a broader action's description.
  The distinction is dependency, not size: necessary work to achieve the named change may be
  summarized with it; a separate change chosen by the agent is a separate decision, however
  small. For example, a rename spanning many files can be one decision, while an unrelated
  configuration edit beside it cannot inherit that consent.

Derive the options from actual recovery possibilities: direct action, preparation of recovery
when feasible, and no action. Do not select an option count for visual consistency. Omitting
recovery asserts that no applicable recovery can be prepared; disclose the checked obstacle.
A large copy is not automatically infeasible, but an existing permission, capacity, or
consistency obstacle must not be concealed. Several independent choices should be split
upstream rather than folded into one identifier.

## Undo validation

An undo command starts from the state that its option would leave behind. Verify that its
sources would exist, destinations match the original state, and unrelated work is preserved.
Use a command appropriate to the actual shell, with concrete paths and necessary conditions.
Do not print placeholders or descriptions such as "restore the backup" in a live undo cell.

The paste test is a completeness check, not an instruction to execute recovery before approval.
Do not run a destructive undo merely to demonstrate it. If later edits would make the printed
command unsafe, disclose that material condition. Never call a backup command an undo command.

## Size and overflow

Aim for one screen: at most 150 Chinese characters or 100 English words, excluding literal
commands and paths. These are ceilings, not quotas; do not hide long prose inside code spans.
Keep at most three decisions in one panel; decisions are not the same as alternative options.
Split independent decisions upstream when necessary, using unambiguous option identifiers.

If the complete disclosure cannot fit, shorten nonessential explanation first. Preserve action
scope, irreversible consequences, recovery conditions, and meaningful options. Exceed the
ceiling explicitly rather than dropping those facts. Do not render the panel repeatedly in
one turn. Additional explanation belongs outside the decision summary when needed for clarity.

## Designed examples — not execution evidence

The first two cases keep the layout and operation constant while varying language and paths.
Assume a POSIX shell, the named source exists, the backup destination does not, and the original
is absent after deletion. Real panels must check their own facts and use the actual shell.

```text
Stopped: delete data/samples; no backup exists.

| Option | Consequence | Undo |
|---|---|---|
| A. Delete | Original permanently lost | — |
| B. Copy to data/samples.bak, then delete | Original recoverable from backup | mv -- data/samples.bak data/samples |
| C. Keep | Original unchanged | — |
```

```text
待确认：删除 exports/report；当前无备份。

| 选项 | 后果 | 撤销 |
|---|---|---|
| A. 直接删除 | 原内容永久丢失 | — |
| B. 复制到 exports/report.bak 后删除 | 原内容可从备份恢复 | mv -- exports/report.bak exports/report |
| C. 保留 | 原内容不变 | — |
```

An external effect has the same columns but no fictitious recovery option:

```text
待确认：向客户发送对账邮件；发送后无法撤回。

| 选项 | 后果 | 撤销 |
|---|---|---|
| A. 发送 | 收件人收到邮件，无法撤回 | — |
| B. 不发送 | 邮件保持未发送 | — |
```

For a mixed task, assume `notes.md` matches HEAD in both index and worktree before acting,
only the stated note will be added, no later edits exist, and a POSIX shell is in use:

```text
Stopped: delete output/ and record it in notes.md; output/ has no backup.

| Option | Consequence | Undo |
|---|---|---|
| A. Delete and record | output/ permanently lost; notes.md gains the note | git restore -- notes.md |
| B. Copy to output.bak, delete and record | output/ recoverable; notes.md gains the note | mv -- output.bak output && git restore -- notes.md |
| C. Do neither | Both unchanged | — |
```

The undo in A restores only the note; the deleted output remains unrecoverable.
The mixed example illustrates why an irreversible option can still contain a useful undo.
Across these examples the disclosure structure stays fixed. Language, paths, option count,
and the number of actions vary with the actual task. The email has no recovery option because
keeping a copy cannot reverse delivery; the mixed case retains the note's undo because
irreversibility of one action does not erase recovery available for another.

## Acceptance criteria

- Subject and actual action scope match, or the difference is explicit.
- Each option has separate consequences and undo; irreversible loss is explicit.
- An identifier authorizes exactly the disclosed option, without a second acknowledgment.
- Available recovery is concrete, applicable, and preserves unrelated work.
- The panel remains concise without dropping a decision-relevant fact.
