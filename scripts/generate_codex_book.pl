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
    my @paras = @$paras_ref;
    my @out;
    push @out, "### $heading";
    push @out, "先说直白版：";
    my $count = 0;
    for my $para (@paras) {
        next if $para =~ /^```/;
        if ($para =~ /^\s*-\s+(.+)$/) {
            push @out, "- " . clean_inline($1);
        } else {
            push @out, clean_inline($para);
        }
        $count++;
        last if $count >= 4;
    }
    push @out, "";
    push @out, "把它理解成一个更严谨的过程：";
    my $n = 1;
    $count = 0;
    for my $para (@paras) {
        next if $para =~ /^```/;
        $para = clean_inline($para);
        $para =~ s/^\-\s+//;
        push @out, "$n. $para";
        $n++;
        $count++;
        last if $count >= 4;
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
    my @takeaways;
    for my $i (0 .. $#sections) {
        last if $i > 2;
        my $heading = $sections[$i]{heading};
        my @p = @{ $sections[$i]{paras} };
        next unless @p;
        my $first = clean_inline($p[0]);
        my $line = $heading ne '正文' ? "`$heading`：$first" : $first;
        $line = substr($line, 0, 72) . '。' if length($line) > 72;
        push @takeaways, $line;
    }
    push @takeaways, '本章主要介绍这一功能的用途、边界和典型使用方式。' unless @takeaways;

    my @out;
    push @out, sprintf("# 第%02d章 %s", $chapter_no, $display_title);
    push @out, "";
    push @out, "> 原始页面：[$page_title]($source_url)";
    push @out, "";
    push @out, "## 本章目标";
    push @out, "这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。";
    push @out, "";
    push @out, "## 先用一个高中数学类比";
    push @out, $analogy;
    push @out, "";
    push @out, "## 严谨定义";
    push @out, $definition;
    push @out, "";
    push @out, "## 你读完应该抓住什么";
    push @out, map { "- $_" } @takeaways;
    push @out, "";
    push @out, "## 分步理解";
    for my $i (0 .. $#sections) {
        last if $i > 4;
        push @out, section_to_text($sections[$i]{heading}, $sections[$i]{paras});
        push @out, "";
    }
    push @out, "## 实战视角";
    push @out, "如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。";
    push @out, "";
    push @out, "## 给高中水平读者的最后一句话";
    push @out, "不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。";
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
    '目标读者：',
    '- 会 Python。',
    '- 用过 LangChain 或知道 tool / memory / agent 这些词。',
    '- 还不太会把 AI Agent 当成完整工程系统来使用。',
    '- 喜欢通过高中数学的类比来建立直觉。',
    '',
    '阅读方法：',
    '1. 先看“开始使用”和“概念”，建立整体坐标系。',
    '2. 再根据你实际使用的入口选择 `App`、`IDE`、`CLI` 或 `Cloud`。',
    '3. 配置、安全、自动化三部分建议结合自己的项目边读边试。',
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
