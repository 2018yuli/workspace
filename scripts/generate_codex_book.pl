#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use open ':std', ':encoding(UTF-8)';
use File::Path qw(make_path);

my $root = '/config/workspace';
my $pages_dir = "$root/docs/official-zh/pages";
my $book_dir = "$root/docs/official-zh/book";
my $nav_file = "$pages_dir/developers-openai-com-codex.md";

sub md_link {
    my ($label, $target) = @_;
    return "[$label]($target)";
}

sub slurp {
    my ($path) = @_;
    open my $fh, '<', $path or die "open $path: $!";
    local $/;
    my $content = <$fh>;
    close $fh;
    return $content;
}

sub write_file {
    my ($path, $content) = @_;
    open my $fh, '>', $path or die "write $path: $!";
    print $fh $content;
    close $fh;
}

sub slug_from_url {
    my ($url) = @_;
    $url =~ s{^https?://developers\.openai\.com/}{};
    $url =~ s{^/+|/+$}{}g;
    $url = 'codex' if $url eq '';
    $url =~ s{/}{-}g;
    return $url;
}

sub page_path_from_url {
    my ($url) = @_;
    my $slug = slug_from_url($url);
    return "$pages_dir/developers-openai-com-$slug.md";
}

sub clean_inline {
    my ($text) = @_;
    $text =~ s/!\[[^\]]*\]\([^)]+\)//g;
    $text =~ s/\[([^\]]+)\]\(([^)]+)\)/$1/g;
    $text =~ s/\s+/ /g;
    $text =~ s/^\s+|\s+$//g;
    return $text;
}

sub clean_heading {
    my ($text) = @_;
    $text = clean_inline($text);
    $text =~ s/\s+/ /g;
    $text =~ s/^\s+|\s+$//g;
    return $text;
}

sub parse_nav {
    my $raw = slurp($nav_file);
    my @lines = split /\n/, $raw;
    my @items;
    my $current_section = '';
    my $in_nav = 0;
    for my $line (@lines) {
        $in_nav = 1 if $line =~ /^### (开始使用|入门)/;
        next unless $in_nav;
        last if $line =~ /^\[API/;
        if ($line =~ /^### (.+)$/) {
            $current_section = $1;
            next;
        }
        if ($line =~ /^(\s*)- \[([^\]]+)\]\((https:\/\/developers\.openai\.com\/[^)]+)\)/) {
            my ($spaces, $title, $url) = ($1, $2, $3);
            next if $url =~ /\/blog\// || $url =~ /\/cookbook\// || $url =~ /community/ || $url =~ /platform\.openai\.com/;
            push @items, {
                level => length($spaces) / 2,
                title => $title,
                url => $url,
                section => $current_section,
            };
            next;
        }
        if ($line =~ /^(\s*)- ([^\[].+)$/) {
            my ($spaces, $title) = ($1, $2);
            push @items, {
                level => length($spaces) / 2,
                title => $title,
                url => undef,
                section => $current_section,
            };
        }
    }
    return @items;
}

sub choose_analogy {
    my ($text) = @_;
    my @rules = (
        ['自动化', '把自动化看成数列中的递推过程。你先给出初值和递推规则，之后系统会在每个时刻自动算出下一项。', '严格地说，自动化就是一个由“触发条件 + 指令 + 执行环境 + 输出汇总”组成的重复映射。'],
        ['提示', '把提示词想成做几何证明时的题目条件。条件越完整，证明路径越短；条件越含糊，辅助线就会乱加。', '严格地说，提示是对目标函数、约束条件和验证标准的联合描述。'],
        ['线程', '线程像解一道多步函数题时保留下来的草稿纸。后一步是否顺利，依赖前面保留下来的中间结果。', '严格地说，线程是一个按时间顺序累积状态的信息序列。'],
        ['子代理', '子代理像把一道大题拆成几道小问：主问题不变，但每个小问由更专门的人分别处理。', '严格地说，子代理是主代理派生出的局部求解器，拥有较小的任务域和更清晰的边界。'],
        ['沙盒', '沙盒像在平面直角坐标系里画出的一个有边界的定义域。函数只能在定义域内取值，超出范围就不允许。', '严格地说，沙盒是执行权限、文件范围和外部访问能力的约束集合。'],
        ['配置', '配置像给函数预先设定参数。公式不变，但参数不同，图像和输出会明显不同。', '严格地说，配置是运行时行为的参数化描述。'],
        ['安全', '安全像不等式约束。你不是只关心最优解，还要保证所有可行解都落在安全区域内。', '严格地说，安全机制是对代理行为加入的一组风险边界与审计条件。'],
        ['模型', '模型选择像选解题工具：心算快但不适合难题，复杂题可能要用更强的公式和更长的推导。', '严格地说，模型是具有特定上下文窗口、推理能力和工具调用风格的求解器。'],
        ['工作流', '工作流像标准解题模板。先审题，再列式，再求解，再验算。', '严格地说，工作流是多个步骤之间按依赖关系构成的执行图。'],
        ['记忆', '记忆像你在数学习题本上积累的错题本。新题并不直接等于旧题，但旧经验会影响下一次求解。', '严格地说，记忆是跨线程保留、可被后续任务调用的持久化上下文。'],
        ['插件', '插件像给函数增加外部变量来源。原来只能用题目内数据，现在可以调用外部表格和工具。', '严格地说，插件是把外部能力封装为标准接口，供代理在推理过程中调用。'],
    );
    for my $rule (@rules) {
        return ($rule->[1], $rule->[2]) if index($text, $rule->[0]) >= 0;
    }
    return (
        '把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。',
        '严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。'
    );
}

sub chapter_profile {
    my ($title) = @_;
    my %p = (
        intro => '这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。',
        bridge => '阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。',
    );
    if ($title =~ /概述$/ || $title =~ /Quickstart|快速入门|概述/) {
        $p{intro} = '这一章属于入门部分，作用是先把 Codex 是什么、能做什么、应该从哪里开始用讲清楚。';
        $p{bridge} = '如果你还没有建立整体印象，这一章最重要；后面的很多概念都会默认你已经知道这些背景。';
    } elsif ($title =~ /提示/) {
        $p{intro} = '这一章讲怎样和 Codex 对话。表面上是在写提示词，实际上是在给代理规定目标、约束和验收标准。';
        $p{bridge} = '这部分看起来简单，但它决定了后面几乎所有任务的质量。';
    } elsif ($title =~ /子代理/) {
        $p{intro} = '这一章讲子代理，也就是把一个大任务拆给多个代理分别处理，再把结果汇总回来。';
        $p{bridge} = '如果你已经能理解“主线程”和“上下文”这两个词，这一章就会非常自然。';
    } elsif ($title =~ /沙盒|审批|安全/) {
        $p{intro} = '这一章讲的是边界。Codex 不是纯聊天工具，它会读文件、改文件、跑命令，所以必须先讲清楚它能做到哪里。';
        $p{bridge} = '只要把“能力”和“权限”分开理解，这类章节就不会难。';
    } elsif ($title =~ /工作流/) {
        $p{intro} = '这一章不是解释单个按钮，而是在讲怎样把 Codex 放进真实任务流程中。';
        $p{bridge} = '可以把它理解成“从会问问题，到会做事情”的过渡章节。';
    } elsif ($title =~ /模型/) {
        $p{intro} = '这一章讲如何选择模型与推理强度，本质上是在做效果、速度和成本之间的平衡。';
        $p{bridge} = '它不是只给你型号清单，而是在解释不同任务为什么要用不同求解器。';
    } elsif ($title =~ /自动化/) {
        $p{intro} = '这一章讲如何把重复任务交给 Codex 自动执行，让它不只是一次性回应，而是能持续工作。';
        $p{bridge} = '理解自动化时，关键不是“怎么点按钮”，而是“什么任务值得自动化”。';
    } elsif ($title =~ /记忆/) {
        $p{intro} = '这一章讲记忆，也就是 Codex 如何在多次任务之间保留对你有帮助的信息。';
        $p{bridge} = '这部分容易和线程上下文混淆，读的时候要注意区分“当前对话中的信息”和“跨任务保留的信息”。';
    }
    return \%p;
}

sub is_hard_concept {
    my ($title) = @_;
    return $title =~ /提示|自定义|记忆|编年史|沙盒|子代理|工作流|模型|网络安全|安全|审批|规则|钩子|AGENTS|MCP|插件|技能|自动化|工作树|远程连接|SDK|服务器/;
}

sub summarize_para {
    my ($text, $limit) = @_;
    $text = clean_inline($text);
    $limit ||= 120;
    return $text if length($text) <= $limit;
    return substr($text, 0, $limit) . '…';
}

sub implementation_refs_for_text {
    my ($text) = @_;
    my @refs;
    my %seen;
    my @rules = (
        [
            qr/子代理|代理线程|并行代理|spawn|委派|fork/i,
            [
                md_link('Codex', '/config/workspace/codex/codex-rs/core/src/codex.rs:285'),
                md_link('CodexThread', '/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37'),
                md_link('ThreadManager::fork_thread', '/config/workspace/codex/codex-rs/core/src/thread_manager.rs:375'),
                md_link('agent/control', '/config/workspace/codex/codex-rs/core/src/agent/control.rs:1'),
                md_link('spawn.rs', '/config/workspace/codex/codex-rs/core/src/spawn.rs:1'),
                md_link('StateRuntime::create_agent_job', '/config/workspace/codex/codex-rs/state/src/runtime.rs:917'),
            ],
        ],
        [
            qr/线程|会话|历史|上下文|恢复|resume|rollout/i,
            [
                md_link('CodexThread', '/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37'),
                md_link('ThreadManager', '/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120'),
                md_link('context_manager', '/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1'),
                md_link('message_history', '/config/workspace/codex/codex-rs/core/src/message_history.rs:1'),
                md_link('rollout/mod', '/config/workspace/codex/codex-rs/core/src/rollout/mod.rs:1'),
                md_link('StateRuntime::list_threads', '/config/workspace/codex/codex-rs/state/src/runtime.rs:306'),
            ],
        ],
        [
            qr/沙盒|审批|权限|网络访问|read-only|workspace-write|danger-full-access|批准/i,
            [
                md_link('sandboxing/mod', '/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38'),
                md_link('SandboxManager', '/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291'),
                md_link('config/permissions', '/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9'),
                md_link('linux-sandbox', '/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18'),
                md_link('linux_run_main', '/config/workspace/codex/codex-rs/linux-sandbox/src/linux_run_main.rs:76'),
                md_link('windows-sandbox', '/config/workspace/codex/codex-rs/windows-sandbox-rs/src/lib.rs:240'),
                md_link('request_command_approval', '/config/workspace/codex/codex-rs/core/src/codex.rs:2576'),
                md_link('request_patch_approval', '/config/workspace/codex/codex-rs/core/src/codex.rs:2637'),
            ],
        ],
        [
            qr/工具|tool|执行命令|shell|exec|apply_patch|write_stdin/i,
            [
                md_link('tools/orchestrator', '/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43'),
                md_link('tools/router', '/config/workspace/codex/codex-rs/core/src/tools/router.rs:1'),
                md_link('tools/registry', '/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1'),
                md_link('unified_exec/mod', '/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74'),
                md_link('exec crate', '/config/workspace/codex/codex-rs/exec/src/lib.rs:1'),
                md_link('apply_patch bridge', '/config/workspace/codex/codex-rs/core/src/apply_patch.rs:1'),
                md_link('shell-command', '/config/workspace/codex/codex-rs/shell-command/src/lib.rs:1'),
            ],
        ],
        [
            qr/技能|skill|SKILL|技能脚本/i,
            [
                md_link('SkillsManager', '/config/workspace/codex/codex-rs/core/src/skills/manager.rs:26'),
                md_link('skills/loader', '/config/workspace/codex/codex-rs/core/src/skills/loader.rs:1'),
                md_link('skills/injection', '/config/workspace/codex/codex-rs/core/src/skills/injection.rs:1'),
                md_link('skills/permissions', '/config/workspace/codex/codex-rs/core/src/skills/permissions.rs:1'),
                md_link('skills crate', '/config/workspace/codex/codex-rs/skills/src/lib.rs:1'),
            ],
        ],
        [
            qr/MCP|资源模板|resource|工具服务器|server/i,
            [
                md_link('mcp_connection_manager', '/config/workspace/codex/codex-rs/core/src/mcp_connection_manager.rs:546'),
                md_link('mcp_tool_call', '/config/workspace/codex/codex-rs/core/src/mcp_tool_call.rs:1'),
                md_link('core/mcp/mod', '/config/workspace/codex/codex-rs/core/src/mcp/mod.rs:1'),
                md_link('mcp-server/lib', '/config/workspace/codex/codex-rs/mcp-server/src/lib.rs:51'),
                md_link('codex_tool_runner', '/config/workspace/codex/codex-rs/mcp-server/src/codex_tool_runner.rs:59'),
            ],
        ],
        [
            qr/记忆|编年史|memories|长期上下文/i,
            [
                md_link('memories/mod', '/config/workspace/codex/codex-rs/core/src/memories/mod.rs:1'),
                md_link('memories/storage', '/config/workspace/codex/codex-rs/core/src/memories/storage.rs:1'),
                md_link('memories/phase1', '/config/workspace/codex/codex-rs/core/src/memories/phase1.rs:1'),
                md_link('memories/phase2', '/config/workspace/codex/codex-rs/core/src/memories/phase2.rs:1'),
                md_link('state runtime memories', '/config/workspace/codex/codex-rs/state/src/runtime/memories.rs:1'),
                md_link('state model memories', '/config/workspace/codex/codex-rs/state/src/model/memories.rs:1'),
            ],
        ],
        [
            qr/模型|推理|reasoning|model/i,
            [
                md_link('ModelsManager', '/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55'),
                md_link('model_info', '/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1'),
                md_link('model_presets', '/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1'),
                md_link('supported_models', '/config/workspace/codex/codex-rs/app-server/src/models.rs:10'),
            ],
        ],
        [
            qr/配置|config|toml|覆盖|requirements|约束/i,
            [
                md_link('config/state', '/config/workspace/codex/codex-rs/config/src/state.rs:118'),
                md_link('config/constraint', '/config/workspace/codex/codex-rs/config/src/constraint.rs:51'),
                md_link('config/config_requirements', '/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78'),
                md_link('config/overrides', '/config/workspace/codex/codex-rs/config/src/overrides.rs:7'),
                md_link('config/diagnostics', '/config/workspace/codex/codex-rs/config/src/diagnostics.rs:36'),
                md_link('core/config/service', '/config/workspace/codex/codex-rs/core/src/config/service.rs:1'),
            ],
        ],
        [
            qr/自动化|后台任务|定时|cron|收件箱|Triage|云任务/i,
            [
                md_link('StateRuntime::create_agent_job', '/config/workspace/codex/codex-rs/state/src/runtime.rs:917'),
                md_link('StateRuntime::report_agent_job_item_result', '/config/workspace/codex/codex-rs/state/src/runtime.rs:1337'),
                md_link('cloud-tasks App', '/config/workspace/codex/codex-rs/cloud-tasks/src/app.rs:47'),
                md_link('cloud-tasks CLI', '/config/workspace/codex/codex-rs/cloud-tasks/src/cli.rs:7'),
                md_link('cloud-tasks run_main', '/config/workspace/codex/codex-rs/cloud-tasks/src/lib.rs:732'),
            ],
        ],
        [
            qr/工作树|worktree|git/i,
            [
                md_link('git_info', '/config/workspace/codex/codex-rs/core/src/git_info.rs:1'),
                md_link('undo task', '/config/workspace/codex/codex-rs/core/src/tasks/undo.rs:1'),
                md_link('review prompts', '/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22'),
                md_link('commit_attribution', '/config/workspace/codex/codex-rs/core/src/commit_attribution.rs:1'),
            ],
        ],
        [
            qr/应用|IDE|CLI|transport|websocket|消息处理|前端|桌面/i,
            [
                md_link('app-server run_main', '/config/workspace/codex/codex-rs/app-server/src/lib.rs:295'),
                md_link('CodexMessageProcessor', '/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399'),
                md_link('transport', '/config/workspace/codex/codex-rs/app-server/src/transport.rs:73'),
                md_link('thread_state', '/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1'),
                md_link('codex-cli entry', '/config/workspace/codex/codex-cli/bin/codex.js:1'),
            ],
        ],
        [
            qr/审阅|review|代码审查/i,
            [
                md_link('review_prompts', '/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22'),
                md_link('tasks/review', '/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1'),
                md_link('app-server review tests', '/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1'),
            ],
        ],
        [
            qr/提示|prompts|自定义提示|AGENTS|项目文档/i,
            [
                md_link('custom_prompts', '/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9'),
                md_link('project_doc', '/config/workspace/codex/codex-rs/core/src/project_doc.rs:134'),
                md_link('instructions/user_instructions', '/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1'),
            ],
        ],
        [
            qr/状态|持久化|数据库|日志|archive|归档/i,
            [
                md_link('StateRuntime', '/config/workspace/codex/codex-rs/state/src/runtime.rs:63'),
                md_link('log_db', '/config/workspace/codex/codex-rs/state/src/log_db.rs:47'),
                md_link('extract/apply_rollout_item', '/config/workspace/codex/codex-rs/state/src/extract.rs:15'),
                md_link('state_db', '/config/workspace/codex/codex-rs/core/src/state_db.rs:1'),
            ],
        ],
        [
            qr/钩子|hook|通知/i,
            [
                md_link('Hooks', '/config/workspace/codex/codex-rs/hooks/src/registry.rs:14'),
                md_link('Hook types', '/config/workspace/codex/codex-rs/hooks/src/types.rs:34'),
                md_link('user_notification', '/config/workspace/codex/codex-rs/hooks/src/user_notification.rs:31'),
            ],
        ],
        [
            qr/搜索|网页|internet|web search/i,
            [
                md_link('web_search', '/config/workspace/codex/codex-rs/core/src/web_search.rs:18'),
                md_link('network_policy_decision', '/config/workspace/codex/codex-rs/core/src/network_policy_decision.rs:1'),
                md_link('network-proxy', '/config/workspace/codex/codex-rs/network-proxy/src/lib.rs:1'),
            ],
        ],
        [
            qr/认证|登录|auth|api key/i,
            [
                md_link('auth', '/config/workspace/codex/codex-rs/core/src/auth.rs:1'),
                md_link('auth/storage', '/config/workspace/codex/codex-rs/core/src/auth/storage.rs:1'),
                md_link('login crate', '/config/workspace/codex/codex-rs/login/src/lib.rs:1'),
                md_link('cloud-tasks auth helper', '/config/workspace/codex/codex-rs/cloud-tasks/src/util.rs:62'),
            ],
        ],
    );

    for my $rule (@rules) {
        my ($pattern, $rule_refs) = @$rule;
        next unless $text =~ $pattern;
        for my $ref (@$rule_refs) {
            next if $seen{$ref}++;
            push @refs, $ref;
        }
    }
    return @refs;
}

sub append_inline_refs {
    my ($text, $max_refs) = @_;
    $max_refs ||= 4;
    my @refs = implementation_refs_for_text($text);
    return $text unless @refs;
    my $limit = @refs < $max_refs ? scalar(@refs) : $max_refs;
    my @picked = @refs[0 .. $limit - 1];
    return $text . "（实现：". join('、', @picked) . "）";
}

sub extract_body {
    my ($page) = @_;
    my $raw = slurp($page);
    my ($page_title) = $raw =~ /^title:\s*"(.*)"\s*$/m;
    $page_title ||= $page;
    my $body = $raw;
    $body =~ s/^---\n.*?\n---\n//s;
    $body =~ s/^.*?复制页面//s if $body =~ /复制页面/s;
    $body =~ s/^.*?(Codex 是 OpenAI 用于软件开发的编码代理。)/$1/s if $body =~ /Codex 是 OpenAI 用于软件开发的编码代理。/s;
    $body =~ s/^.*?(每个ChatGPT计划都包括Codex。)/$1/s if $body =~ /每个ChatGPT计划都包括Codex。/s;
    my @lines = split /\n/, $body;
    my @sections;
    my $heading = '正文';
    my @paras;
    my @buffer;
    my $flush = sub {
        my @cleaned = grep { $_ ne '' } map { clean_inline($_) } @paras;
        if (@cleaned) {
            push @sections, { heading => $heading, paras => [@cleaned] };
        }
        @paras = ();
    };
    for my $line (@lines) {
        next if $line =~ /^\s*复制\s*$/;
        next if $line =~ /^\s*选择一个选项\s*$/;
        next if $line =~ /^\s*搜索/;
        next if $line =~ /^\s*主要导航\s*$/;
        next if $line =~ /^\s*主导航\s*$/;
        next if $line =~ /^\s*文档\s+用例\s*$/;
        next if $line =~ /^\s*文档\s+使用案例\s*$/;
        next if $line =~ /^\s*worktreesmcpnoninteractivesandbox\s*$/;
        if ($line =~ /^(##+)\s+(.+)$/) {
            if (@buffer) {
                push @paras, join(' ', @buffer);
                @buffer = ();
            }
            $flush->();
            $heading = $2;
            next;
        }
        next if $line =~ /^\s*!\[/;
        next if $line =~ /^\s*\[.*https?:/;
        next if $line =~ /复制!?\[/;
        if ($line =~ /^\s*$/) {
            if (@buffer) {
                push @paras, join(' ', @buffer);
                @buffer = ();
            }
            next;
        }
        if ($line =~ /^\s*-\s+/) {
            if (@buffer) {
                push @paras, join(' ', @buffer);
                @buffer = ();
            }
            push @paras, $line;
            next;
        }
        push @buffer, $line;
    }
    push @paras, join(' ', @buffer) if @buffer;
    $flush->();
    return ($page_title, @sections);
}

sub section_to_text {
    my ($heading, $paras_ref) = @_;
    my @paras = grep { $_ !~ /^```/ } @$paras_ref;
    my @clean = map { my $x = clean_inline($_); $x =~ s/^\-\s+//; $x } @paras;
    @clean = grep { $_ ne '' } @clean;
    my @out;
    push @out, "### $heading";
    if (@clean == 1) {
        push @out, append_inline_refs(summarize_para($clean[0], 220), 4);
        return join("\n", @out);
    }
    if (@clean >= 2) {
        my $first = summarize_para($clean[0], 180);
        my $second = summarize_para($clean[1], 180);
        push @out, append_inline_refs($first, 4);
        push @out, "";
        push @out, "继续往下看，这一节还强调了两件事：";
        push @out, "- " . append_inline_refs($second, 4);
        my $limit = @clean < 4 ? scalar(@clean) : 4;
        for my $i (2 .. $limit - 1) {
            last if $i > $#clean;
            push @out, "- " . append_inline_refs(summarize_para($clean[$i], 150), 4);
        }
        return join("\n", @out);
    }
    return join("\n", @out);
}

sub chapter_content {
    my ($chapter_no, $display_title, $page_title, $source_url, $sections_ref) = @_;
    my @sections = @$sections_ref;
    my $joined = $display_title . ' ' . $page_title;
    for my $i (0 .. $#sections) {
        last if $i > 2;
        my @p = @{ $sections[$i]{paras} };
        $joined .= ' ' . join(' ', @p[0 .. ($#p < 1 ? $#p : 1)]) if @p;
    }
    my ($analogy, $definition) = choose_analogy($joined);
    my $profile = chapter_profile($display_title . ' ' . $page_title);
    my @takeaways;
    for my $i (0 .. $#sections) {
        last if $i > 2;
        my $heading = clean_heading($sections[$i]{heading});
        my @p = @{ $sections[$i]{paras} };
        next unless @p;
        my $first = clean_inline($p[0]);
        my $line = $heading ne '正文' ? "`$heading`：$first" : $first;
        $line = substr($line, 0, 100) . '…' if length($line) > 100;
        push @takeaways, $line;
    }
    push @takeaways, '本章主要介绍这一功能的用途、边界和典型使用方式。' unless @takeaways;

    my @out;
    push @out, sprintf("# 第%02d章 %s", $chapter_no, $display_title);
    push @out, "";
    push @out, "> 原始页面：[$page_title]($source_url)";
    push @out, "";
    push @out, $profile->{intro};
    push @out, "";
    push @out, $profile->{bridge};
    push @out, "";
    if (is_hard_concept($display_title . ' ' . $page_title)) {
        push @out, "## 数学类比";
        push @out, $analogy;
        push @out, "";
        push @out, "## 严谨定义";
        push @out, $definition;
        push @out, "";
    }
    push @out, "## 本章先抓重点";
    push @out, map { "- $_" } @takeaways[0 .. ($#takeaways < 2 ? $#takeaways : 2)];
    push @out, "";
    push @out, "## 正文整理";
    for my $i (0 .. $#sections) {
        last if $i > 4;
        push @out, section_to_text(clean_heading($sections[$i]{heading}), $sections[$i]{paras});
        push @out, "";
    }
    push @out, "## 小结";
    push @out, "读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。";
    push @out, "";
    return join("\n", @out);
}

make_path($book_dir);
my @nav = parse_nav();
my %seen;
my @manifest;
my $chapter_no = 1;

for my $item (@nav) {
    next unless defined $item->{url};
    next if $seen{$item->{url}}++;
    my $page = page_path_from_url($item->{url});
    next unless -f $page;
    my ($page_title, @sections) = extract_body($page);
    my $slug = slug_from_url($item->{url});
    my $filename = sprintf('%02d-%s.md', $chapter_no, $slug);
    my $content = chapter_content($chapter_no, $item->{title}, $page_title, $item->{url}, \@sections);
    write_file("$book_dir/$filename", $content);
    push @manifest, [$chapter_no, $item->{section}, $item->{title}, $filename];
    $chapter_no++;
}

my @readme = (
    '# Codex 通俗书',
    '',
    '这套书根据 `docs/official-zh/pages` 中的官方中文页面整理而成，保持原导航顺序，同时把表达方式改成更适合入门读者的书籍体例。',
    '',
    '这次整理额外补了一层“实现映射”：尽量把书里提到的业务观点，对应回仓库里的 crate、子模块、类、结构体和关键函数。',
    '',
    '阅读方法：',
    '1. 先看“开始使用”和“概念”，建立整体坐标系。',
    '2. 再根据你实际使用的入口选择 `App`、`IDE`、`CLI` 或 `Cloud`。',
    '3. 配置、安全、自动化三部分建议结合自己的项目边读边试。',
    '',
    '系统架构总览：',
    '- `codex/codex-rs/core`：主业务编排层，线程、工具、记忆、模型、技能、MCP、审批都在这里汇总。',
    '- `codex/codex-rs/app-server`：App / IDE 的通信与消息处理入口。',
    '- `codex/codex-rs/config` 与 `codex/codex-rs/core/src/config`：配置模型、约束和加载流程。',
    '- `codex/codex-rs/state`：线程、日志、agent job、记忆等持久化状态。',
    '- `codex/codex-rs/linux-sandbox`、`codex/codex-rs/windows-sandbox-rs`、`codex/codex-rs/shell-escalation`：本地权限边界与沙盒执行。',
    '- `codex/codex-rs/cloud-tasks`：云任务与后台任务的任务视图、状态和交互入口。',
    '- `codex/codex-rs/mcp-server`、`codex/codex-rs/core/src/mcp_*`：MCP 工具接入与调用链。',
    '- `codex/sdk/typescript`：外部程序调用 Codex 的 TypeScript SDK。',
    '',
    '## 目录',
    '',
);

my $current_section = '';
for my $row (@manifest) {
    my ($no, $section, $title, $filename) = @$row;
    if ($section ne $current_section) {
        $current_section = $section;
        push @readme, "### $section";
    }
    push @readme, sprintf("- [第%02d章 %s](./%s)", $no, $title, $filename);
}

write_file("$book_dir/README.md", join("\n", @readme) . "\n");
