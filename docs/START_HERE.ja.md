# まずここから

このページは、初めて来た人が最初の3分で Codex Maintainer Kit の役割をつかむための入口です。

## これは何か

Codex Maintainer Kit は、OSSリポジトリを Codex に手伝わせる前に、状況を整理するローカルCLIです。メンテナンス監査、メンテナー向け説明、作業タスク、変更レビュー用レポートをMarkdownで作ります。

## 最初の3分

1. まず [やさしい解説](BEGINNER_GUIDE.ja.md) を読みます。
2. 次に [ユースケース](USE_CASES.ja.md) から、使うコマンドを選びます。
3. `python3 -m pip install -e .` でローカルに入れます。
4. テスト用リポジトリで `codex-maintainer-kit audit . --output OSS_MAINTENANCE_AUDIT.md` を実行します。

## 読む順番

| やりたいこと | コマンド | 次に読むもの |
| --- | --- | --- |
| リポジトリの健康診断 | `audit` | [ユースケース](USE_CASES.ja.md) |
| Codexに渡す前提情報作り | `brief` | [出力例](../examples/MAINTAINER_BRIEF.example.md) |
| 作業タスク化 | `tasks` | [タスクスキーマ](../schema/codex-tasks.schema.json) |
| 変更内容の人間レビュー | `review` | [レビュー例](../examples/CODEX_REVIEW.example.md) |

## 安全面

このキットは人間が確認するための資料を作ります。コードを自動マージしたり、PRを勝手に作ったり、Codexに書き込み権限を渡したりしません。
