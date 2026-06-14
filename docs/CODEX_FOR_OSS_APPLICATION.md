# Codex for Open Source Application Notes

This document prepares the exact application text for the Codex for Open Source form.

Application form:

https://openai.com/ja-JP/form/codex-for-oss/

## Required Personal Fields

- Last name: enter manually
- First name: enter manually
- ChatGPT account email: enter manually
- GitHub username: enter manually
- GitHub repository URL: use the public `codex-maintainer-kit` repository URL after publishing
- Role: Main maintainer

## Why This Repository Qualifies

500 Japanese characters or fewer:

`codex-maintainer-kit` は、OSSメンテナーがCodexを実際の保守作業に使いやすくするためのCLIです。リポジトリをスキャンし、README、LICENSE、CI、テスト、AGENTS.md、Issueテンプレートなどの保守状態を確認したうえで、Codexに渡せる `MAINTAINER_BRIEF.md`、`CODEX_TASKS.md`、GitHub issue下書きを生成します。作ったばかりのプロジェクトですが、OSSのIssueトリアージ、PRレビュー、リリース準備、人間レビュー前提のAI活用という本プログラムの目的に直接対応しています。

## Interested Benefits

Select both:

- Codex Security
- API credits for the project

## Planned API Credit Usage

500 Japanese characters or fewer:

APIクレジットは、`codex-maintainer-kit` の保守ワークフロー改善に使います。具体的には、生成された `MAINTAINER_BRIEF.md` と `CODEX_TASKS.md` をもとに、CodexでIssueの分解、テスト追加、テンプレート改善、README更新、リリース準備、PRレビュー補助を行います。また、将来的には複数OSSリポジトリに対して保守タスクを自動生成し、人間メンテナーが確認してからマージする運用を検証します。自動マージはせず、最終判断は人間が行います。

## Additional Message

500 Japanese characters or fewer:

このプロジェクトは、Codexを単なるコード生成ではなく、OSSメンテナンスの継続作業に組み込むための実験でもあります。既存のScorecardのようなセキュリティ採点ツールではなく、診断結果をCodex用タスク、完了条件、GitHub issue下書き、人間レビュー観点に変換する点に絞っています。採択された場合は、実際のメンテナンス履歴、Issue、PR、リリースを公開し、他のOSSメンテナーが再利用できる形に改善していきます。

## Submission Notes

- Do not claim broad adoption yet.
- Emphasize early active maintenance, clear public utility, and direct fit with Codex-assisted OSS workflows.
- Submit only after the GitHub repository is public and has a visible first release tag.
