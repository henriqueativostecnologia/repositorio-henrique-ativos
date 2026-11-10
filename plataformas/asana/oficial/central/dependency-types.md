---
fonte: https://help.asana.com/s/article/dependency-types?language=en_US
baixado: 2026-11-10
---

# Dependency types

Dependencies show the relationships between tasks and the sequence in which they should be performed. Task dependencies allow you to mark a task as blocking another or being blocked by another task. In this way, we designate one task as the precedent and the other as a dependent; the precedent task is performed before the dependent task.

Previously, Asana offered one type of dependency, called finish to start, or FS. This meant that the dependent task should not be started until the precedent task was completed. We've now added three more dependency types, outlined in this article.

In the examples below, it's helpful to consider two example tasks, Task A and Task B. Task A is the precedent task, and task B is the dependent task.

#### Related articles

- [Task dependencies](https://help.asana.com/s/article/task-dependencies?language=en_US)
- [Auto-shifting dates for dependent tasks](https://help.asana.com/s/article/auto-shifting-dates-for-dependent-tasks?language=en_US)

## Finish to start - FS

Task B cannot start until Task A is complete. This is the most common type of dependency.

For example, a writer cannot begin editing a draft until the first draft is complete.

## Finish to finish - FF

Task B cannot finish until Task A is complete. This type of finish dependency is useful for tasks which contain subtasks; if the subtasks are not complete, the parent task cannot be completed.

For example, before declaring that the design phase of a project is complete, all user experience research interviews must also be finished.

## Start to start - SS

Task B cannot start before Task A starts. This type of dependency is ideal for tasks that are required to run parallel to each other.

For example, drafting a social media announcement should not start until the related web page creation has begun, although neither task needs to be complete before the other may begin.

## Start to finish - SF

Task B must start before Task A can be completed. This is important for situations that require overlap.

For example, in shift work, one operator's shift should not end before their replacement has begun their shift to provide uninterrupted coverage.

Jamie's shift does not end until Chris' shift begins.

## Dependency types and auto-shifting dates

Dependency types are compatible with Asana's [auto-shifting date](https://help.asana.com/s/article/auto-shifting-dates-for-dependent-tasks?language=en_US) functionality. Asana uses the relevant dates for any dependency relationship to determine how to shift dates. Relevant dates are defined as the critical or key dates for a specific dependency type that directly influence scheduling adjustments.

## Relevant dates for each dependency type

The following relevant dates are used to determine how tasks auto-shift.

### Finish to start - FS

- The precedent task's due date
- The dependent task's start date

### Finish to finish - FF

- The precedent task's due date
- The dependent task's due date

### Start to start - SS

- The precedent task's start date
- The dependent task's start date

### Start to finish - SF

- The precedent task's start date
- The dependent task's due date

## Default dependency type

Finish to start (FS) is the default dependency type at creation, but the dependency type can be modified afterward.

[](https://forum.asana.com/c/forum-en/tips/6)
