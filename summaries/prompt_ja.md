# プロンプト一覧

> このファイルには `prompts/` ディレクトリ内のプロンプトと一行の日本語要約を記載しています。

| プロンプト名                                              | 概要                                                                                                                         |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| apple-appstore-reviewer                                   | iOS アプリを審査し、App Store リジェクトのリスクを評価して優先順位付きの修正案とレビューノートを提供します。                 |
| arch-linux-triage                                         | pacman、systemd、Arch 固有のベストプラクティスを使って Arch Linux の問題を診断・解決します。                                 |
| ai-prompt-engineering-safety-review                       | プロンプトの安全性、バイアス、セキュリティ、有効性を総合的にレビューし改善案を提示します。                                   |
| add-educational-comments                                  | コードに教育的コメントを追加して教材化します。行数制約と厳格なルールに従います。                                             |
| az-cost-optimize                                          | Azure の IaC / リソースを分析してコスト最適化案を提示、想定節約額を算出し、作業を追跡する GitHub Issue / EPIC を作成します。 |
| aspnet-minimal-api-openapi                                | 型安全な ASP.NET Minimal API エンドポイントと完全な OpenAPI/Swagger ドキュメントを作成する支援を行います。                   |
| architecture-blueprint-generator                          | プロジェクトのアーキテクチャを自動検出して包括的な設計ブループリント（図表・パターン含む）を生成します。                     |
| boost-prompt                                              | 明確化質問を行い、反復的に改善されたプロンプトを生成する対話型ワークフロー（コード生成は行わない）。                         |
| azure-resource-health-diagnose                            | ログやテレメトリを用いて Azure リソースのヘルスを解析し、原因を診断して修復計画を作成します。                                |
| centos-linux-triage                                       | RHEL 互換コマンドと SELinux を考慮した手順で CentOS の問題をトリアージ・解決します。                                         |
| breakdown-test                                            | 機能アーティファクトに基づいた包括的なテスト計画、QA 戦略、テスト項目分解を生成します。                                      |
| breakdown-plan                                            | GitHub プロジェクト用の計画（エピック→機能→ストーリー）を生成し、Issue 自動化、依存関係、優先度を組み込みます。              |
| breakdown-feature-prd                                     | 機能の PRD（受け入れ基準、スコープ含む）を詳細に作成します。                                                                 |
| breakdown-feature-implementation                          | 機能を実装タスクと技術的ステップに分解し、計画と実行に適した形式で提供します。                                               |
| containerize-aspnetcore                                   | ASP.NET Core アプリをコンテナ化するためのベストプラクティスを提供します。                                                    |
| containerize-aspnet-framework                             | レガシー ASP.NET Framework アプリの安全かつ効果的なコンテナ化ガイダンスを提供します。                                        |
| comment-code-generate-a-tutorial                          | コメント付きコードを抽出・構造化してチュートリアル形式の教育資料を生成します。                                               |
| code-exemplars-blueprint-generator                        | プロジェクト慣習と優れたパターンを示すコード例のブループリントを生成します。                                                 |
| breakdown-epic-pm                                         | PM 観点でエピックを分解し、機能、ストーリー、タスクに優先順位を付けます。                                                    |
| breakdown-epic-arch                                       | エピックのアーキテクチャ分解を作成し、コンポーネント、インターフェース、設計制約を文書化します。                             |
| cosmosdb-datamodeling                                     | Azure Cosmos DB の NoSQL モデリング（要件収集、パーティション設計、データモデル生成）を支援します。                          |
| copilot-instructions-blueprint-generator                  | `copilot-instructions.md` を生成し、Copilot がプロジェクト規約やバージョンに沿ってコードを生成できるよう導きます。           |
| create-agentsmd                                           | リポジトリ向けのエージェントセットアップ、ワークフロー、ガイダンスを記述した `AGENTS.md` を生成します。                      |
| convert-plaintext-to-md                                   | プレーンテキストを指定テンプレートに従って適切な Markdown に変換します。                                                     |
| create-architectural-decision-record                      | 技術的決定、代替案、理由を記録するアーキテクチャ決定記録（ADR）を生成します。                                                |
| create-github-issue-feature-from-specification            | 仕様ファイルから機能用の GitHub Issue を作成し、受け入れ基準とコンテキストを含めます。                                       |
| create-github-action-workflow-specification               | 高レベル要件から GitHub Actions ワークフロー仕様を生成します。                                                               |
| documentation-writer                                      | ガイド、ハウツー、リファレンスなどの整った技術文書を生成します。                                                             |
| dotnet-design-pattern-review                              | .NET コードのデザインパターン使用をレビューし、改善やリファクタリングを提案します。                                          |
| dotnet-best-practices                                     | アーキテクチャ、性能、保守性に関する .NET のベストプラクティスを助言します。                                                 |
| devops-rollout-plan                                       | プレフライトチェック、検証シグナル、ロールバック手順、コミュニケーション計画を含むロールアウト計画を作成します。             |
| ef-core                                                   | Entity Framework Core のモデリング、性能、マイグレーション、テストに関するベストプラクティスを提供します。                   |
| editorconfig                                              | プロジェクトの言語と好みに基づいた包括的な `.editorconfig` を生成します。                                                    |
| dotnet-upgrade                                            | .NET フレームワーク/ライブラリのアップグレード計画、依存互換性、CI/CD 調整を支援します。                                     |
| first-ask                                                 | Joyride を用いた明確化質問型の対話ワークフローで、実行前にタスクの範囲を精査します。                                         |
| finalize-agent-prompt                                     | プロンプトファイルを洗練し、明確さと構造を改善します（フロントマターは保持）。                                               |
| fedora-linux-triage                                       | dnf、systemd、SELinux を考慮した Fedora のトリアージと解決方法を提供します。                                                 |
| folder-structure-blueprint-generator                      | プロジェクトのフォルダ構成を解析・可視化し、推奨慣習を提示します。                                                           |
| gen-specs-as-issues                                       | 欠けている機能を特定し、優先度付きの仕様と GitHub Issue に変換します。                                                       |
| declarative-agents                                        | 宣言型エージェント定義とワークフローの作成を支援します（エージェントマニフェスト生成）。                                     |
| debian-linux-triage                                       | apt、systemd、AppArmor を考慮して Debian の問題をトリアージ・解決します。                                                    |
| dataverse-python-usecase-builder                          | Dataverse を使った Python ソリューションの要件、データモデル、実装テンプレートを設計します。                                 |
| dataverse-python-quickstart                               | CRUD 等の簡潔な Dataverse Python SDK のクイックスタートコードを提供します。                                                  |
| generate-custom-instructions-from-codebase                | 差分を解析して Copilot のマイグレーション/コード進化用の指示を生成します。                                                   |
| dataverse-python-production-code                          | 冗長性対策やログ等を含むプロダクション向けの Dataverse Python コードを生成します。                                           |
| dataverse-python-advanced-patterns                        | バッチ処理、OData 最適化、ファイルアップロード、キャッシュ等の高度なパターンを提案します。                                   |
| csharp-xunit                                              | XUnit のベストプラクティス（テスト構造、データ駆動、モック手法）を提供します。                                               |
| csharp-tunit                                              | TUnit のベストプラクティス（ライフサイクルフック、データ駆動）を提供します。                                                 |
| csharp-nunit                                              | NUnit のベストプラクティス（フィクスチャ、データ駆動、アサーション）を提供します。                                           |
| csharp-mstest                                             | MSTest のモダンベストプラクティス（セットアップ、アサーション、ライフサイクル）を提供します。                                |
| csharp-mcp-server-generator                               | ロギング、DI パターンを備えた本番利用可能な C# MCP サーバーを生成します。                                                    |
| csharp-docs                                               | C# 型の XML コメントとドキュメントベストプラクティスを保証します。                                                           |
| csharp-async                                              | 非同期プログラミングの命名、戻り値、例外処理、性能に関するベストプラクティスを提供します。                                   |
| create-tldr-page                                          | 公式ドキュメントやコマンド例から簡潔な tldr ページを生成します。                                                             |
| create-technical-spike                                    | 成功基準とプロトタイプを含むタイムボックス化された技術スパイクドキュメントを生成します。                                     |
| go-mcp-server-generator                                   | サンプルツール、トランスポート、ドキュメントを含む Go MCP サーバーのスキャフォールドを生成します。                           |
| create-spring-boot-kotlin-project                         | 推奨依存関係と設定を備えた Spring Boot Kotlin プロジェクトのスケルトンを生成します。                                         |
| create-spring-boot-java-project                           | Spring Boot Java プロジェクトのスケルトンを生成します。                                                                      |
| create-specification                                      | AI に適した構造化された要件、インターフェース、テストを含む仕様を作成します。                                                |
| create-readme                                             | プロジェクトに合わせた簡潔で体系的な `README.md` を生成します。                                                              |
| create-oo-component-documentation                         | C4/arc42/IEEE に準拠した OO コンポーネントの包括的ドキュメントを生成します。                                                 |
| create-llms                                               | LLM 消費用のリポジトリ構造を記述する `llms.txt` を生成します。                                                               |
| create-implementation-plan                                | 段階的タスクとバリデーションを含む機械可読な実装計画を生成します。                                                           |
| create-github-pull-request-from-specification             | 仕様から PR を作成し、テンプレートに沿って内容を埋めます。                                                                   |
| create-github-issues-for-unmet-specification-requirements | 未実装の仕様要件に対してコンテキストと受け入れ基準を含む Issue を作成します。                                                |
| create-github-issues-feature-from-implementation-plan     | 実装計画各フェーズに基づく GitHub Issue をテンプレートで生成します。                                                         |

---

_生成済み：最初のプロンプト群を要約しました。_

_Next step:_ 残りのプロンプト（合計 138 件まで）を翻訳してこのファイルに追記することもできます。続けますか？
